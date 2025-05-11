import pytest
from typing import Optional, Type, List
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.battlefields import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.packets import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.variables import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.ids import *
from smrpgpatchbuilder.datatypes.overworld_scripts.ids import *
from smrpgpatchbuilder.datatypes.dialogs.ids.dialog_ids import *
from smrpgpatchbuilder.datatypes.items.implementations import *
from smrpgpatchbuilder.datatypes.battles.ids.pack_ids import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScriptBank,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptBankTooLongException,
    IdentifierException,
    InvalidCommandArgumentException,
    InvalidOpcodeException,
    RenderException,
)

from dataclasses import dataclass


@dataclass
class Case:
    label: str
    commands_factory: callable
    expected_bytes: Optional[List[int]] = None
    exception: Optional[str] = None
    exception_type: Optional[Type] = None


test_cases = [
    #
    # Basic (no GOTOs) command tests
    #
    Case(
        "Loop 10 frames",
        commands_factory=lambda: [StartLoopNFrames(10)],
        expected_bytes=[0xD5, 0x0A, 0x00],
    ),
    Case(
        label="StartLoopNTimes",
        commands_factory=lambda: [StartLoopNTimes(127)],
        expected_bytes=[0xD4, 0x7F],
    ),
    Case(label="EndLoop", commands_factory=lambda: [EndLoop()], expected_bytes=[0xD7]),
    Case(
        label="MoveScriptToMainThread",
        commands_factory=lambda: [MoveScriptToMainThread()],
        expected_bytes=[0xFD, 0x40],
    ),
    Case(
        label="MoveScriptToBackgroundThread1",
        commands_factory=lambda: [MoveScriptToBackgroundThread1()],
        expected_bytes=[0xFD, 0x41],
    ),
    Case(
        label="MoveScriptToBackgroundThread2",
        commands_factory=lambda: [MoveScriptToBackgroundThread2()],
        expected_bytes=[0xFD, 0x42],
    ),
    Case(
        label="Pause",
        commands_factory=lambda: [
            Pause(120),
            Pause(370),
        ],
        expected_bytes=[0xF0, 0x77, 0xF1, 0x71, 0x01],
    ),
    Case(
        label="RememberLastObject",
        commands_factory=lambda: [RememberLastObject()],
        expected_bytes=[0xFD, 0x32],
    ),
    Case(
        label="ResumeBackgroundEvent",
        commands_factory=lambda: [
            ResumeBackgroundEvent(TIMER_701C),
        ],
        expected_bytes=[0x47, 0x00],
    ),
    Case(
        label="RunBackgroundEvent",
        commands_factory=lambda: [
            RunBackgroundEvent(
                event_id=E0551_ROSE_TOWN_OCCUPIED_MODS,
                return_on_level_exit=True,
                bit_6=True,
            ),
            RunBackgroundEvent(
                event_id=E0465_MUSHROOM_DERBY_BUSINESS_LOGIC,
                return_on_level_exit=True,
                run_as_second_script=True,
            ),
        ],
        expected_bytes=[0x40, 0x27, 0x62, 0x40, 0xD1, 0xA1],
    ),
    Case(
        label="RunBackgroundEventWithPause",
        commands_factory=lambda: [
            RunBackgroundEventWithPause(
                event_id=E3075_HEAL_FLASH, timer_var=TIMER_7022, bit_4=True, bit_5=True
            ),
        ],
        expected_bytes=[
            0x44,
            0x03,
            0xFC,
        ],
    ),
    Case(
        label="RunBackgroundEventWithPauseReturnOnExit",
        commands_factory=lambda: [
            RunBackgroundEventWithPauseReturnOnExit(
                event_id=E0653_MARRYMORE_SANCTUARY_CANDLE_7, timer_var=TIMER_701C
            ),
            RunBackgroundEventWithPauseReturnOnExit(
                event_id=E1543_CHEST_CAMERA_SHIFT,
                timer_var=TIMER_701C,
                bit_4=True,
                bit_5=True,
            ),
        ],
        expected_bytes=[0x45, 0x8D, 0x02, 0x45, 0x07, 0x36],
    ),
    Case(
        label="RunEventAtReturn",
        commands_factory=lambda: [RunEventAtReturn(E1727_EMPTY)],
        expected_bytes=[0xFD, 0x46, 0xBF, 0x06],
    ),
    Case(
        label="RunEventAsSubroutine",
        commands_factory=lambda: [
            RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
        ],
        expected_bytes=[0xD1, 0x03, 0x0E],
    ),
    Case(
        label="StopAllBackgroundEvents",
        commands_factory=lambda: [StopAllBackgroundEvents()],
        expected_bytes=[0xFD, 0x43],
    ),
    Case(
        label="StopBackgroundEvent",
        commands_factory=lambda: [StopBackgroundEvent(TIMER_701C)],
        expected_bytes=[0x46, 0x00],
    ),
    Case(label="Return", commands_factory=lambda: [Return()], expected_bytes=[0xFE]),
    Case(
        label="ReturnAll", commands_factory=lambda: [ReturnAll()], expected_bytes=[0xFF]
    ),
    Case(
        label="ReturnFD",
        commands_factory=lambda: [ReturnFD()],
        expected_bytes=[0xFD, 0xFE],
    ),
    Case(
        label="SetMem704XAt7000Bit",
        commands_factory=lambda: [SetMem704XAt7000Bit()],
        expected_bytes=[0xA3],
    ),
    Case(
        label="ClearMem704XAt7000Bit",
        commands_factory=lambda: [ClearMem704XAt7000Bit()],
        expected_bytes=[0xA7],
    ),
    Case(
        label="Move70107015To7016701B",
        commands_factory=lambda: [Move70107015To7016701B()],
        expected_bytes=[0xBE],
    ),
    Case(
        label="Move7016701BTo70107015",
        commands_factory=lambda: [Move7016701BTo70107015()],
        expected_bytes=[0xBF],
    ),
    Case(
        label="SetVarToConst",
        commands_factory=lambda: [
            SetVarToConst(COIN_COUNTER_1, 0),
            SetVarToConst(TIMER_701E, 64),
            SetVarToConst(PRIMARY_TEMP_7000, 524),
        ],
        expected_bytes=[0xA8, 0x3A, 0x00, 0xB0, 0x0F, 0x40, 0x00, 0xAC, 0x0C, 0x02],
    ),
    Case(
        label="ReadFromAddress",
        commands_factory=lambda: [ReadFromAddress(0x91D2)],
        expected_bytes=[0x5C, 0xD2, 0x91],
    ),
    Case(
        label="Set7000To7FMemVar",
        commands_factory=lambda: [Set7000To7FMemVar(0xF8C0)],
        expected_bytes=[0xFD, 0xAC, 0xC0, 0x00],
    ),
    Case(
        label="SetBit",
        commands_factory=lambda: [SetBit(EXP_STAR_BIT_6)],
        expected_bytes=[0xA1, 0xE3],
    ),
    Case(
        label="ClearBit",
        commands_factory=lambda: [ClearBit(EXP_STAR_BIT_4)],
        expected_bytes=[0xA5, 0x23],
    ),
    Case(
        label="Set0158Bit3Offset",
        commands_factory=lambda: [Set0158Bit3Offset(0x0158)],
        expected_bytes=[0xFD, 0x8B, 0x00],
    ),
    Case(
        label="Set0158Bit7Offset",
        commands_factory=lambda: [
            Set0158Bit7Offset(0x015E),
        ],
        expected_bytes=[0xFD, 0x88, 0x03],
    ),
    Case(
        label="Clear0158Bit7Offset",
        commands_factory=lambda: [
            Clear0158Bit7Offset(0x0158),
        ],
        expected_bytes=[0xFD, 0x89, 0x00],
    ),
    Case(
        label="Clear7016To7018AndIsolate701AHighByteIf7018Bit0Set",
        commands_factory=lambda: [Clear7016To7018AndIsolate701AHighByteIf7018Bit0Set()],
        expected_bytes=[0xFD, 0xC6],
    ),
    Case(
        label="CopyVarToVar",
        commands_factory=lambda: [
            CopyVarToVar(from_var=X_COORD_2, to_var=Y_COORD_2),
            CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70C6),
            CopyVarToVar(from_var=GAME_OVER_COUNTER_MAYBE, to_var=PRIMARY_TEMP_7000),
            CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
            CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7032),
        ],
        expected_bytes=[
            0xBC,
            0x0B,
            0x0C,
            0xB5,
            0x26,
            0xB4,
            0x1B,
            0xBA,
            0x12,
            0xBB,
            0x19,
        ],
    ),
    Case(
        label="StoreBytesTo0335And0556",
        commands_factory=lambda: [StoreBytesTo0335And0556(0x10, 0x22)],
        expected_bytes=[0xFD, 0x90, 0x10, 0x22],
    ),
    Case(
        label="Store00To0248",
        commands_factory=lambda: [Store00To0248()],
        expected_bytes=[0xFD, 0xFC],
    ),
    Case(
        label="Store00To0334",
        commands_factory=lambda: [Store00To0334()],
        expected_bytes=[0xFD, 0x93],
    ),
    Case(
        label="Store01To0248",
        commands_factory=lambda: [Store01To0248()],
        expected_bytes=[0xFD, 0xFB],
    ),
    Case(
        label="Store01To0335",
        commands_factory=lambda: [Store01To0335()],
        expected_bytes=[0xFD, 0x92],
    ),
    Case(
        label="Store02To0248",
        commands_factory=lambda: [Store02To0248()],
        expected_bytes=[0xFD, 0xFD],
    ),
    Case(
        label="StoreFFTo0335",
        commands_factory=lambda: [StoreFFTo0335()],
        expected_bytes=[0xFD, 0x91],
    ),
    Case(
        label="Set7000ToMinecartTimer",
        commands_factory=lambda: [Set7000ToMinecartTimer()],
        expected_bytes=[0xFD, 0xB8],
    ),
    Case(
        label="StoreSetBits",
        commands_factory=lambda: [
            StoreSetBits(TEMP_7044_6),
        ],
        expected_bytes=[0xFD, 0xA8, 0x26],
    ),
    Case(
        label="SwapVars",
        commands_factory=lambda: [
            SwapVars(memory_a=TEMP_7028, memory_b=PRIMARY_TEMP_7000)
        ],
        expected_bytes=[0xBD, 0x00, 0x14],
    ),
    Case(
        label="AddConstToVar",
        commands_factory=lambda: [
            AddConstToVar(Y_COORD_2, 63744),
            AddConstToVar(PRIMARY_TEMP_7000, 2),
            AddConstToVar(TEMP_70B8, 128),
        ],
        expected_bytes=[0xB1, 0x0C, 0x00, 0xF9, 0xAD, 0x02, 0x00, 0xA9, 0x18, 0x80],
    ),
    Case(
        label="Inc",
        commands_factory=lambda: [
            Inc(GAME_OVER_COUNTER_MAYBE),
            Inc(SECONDARY_TEMP_7024),
            Inc(PRIMARY_TEMP_7000),
        ],
        expected_bytes=[0xAA, 0x1B, 0xB2, 0x12, 0xAE],
    ),
    Case(label="Dec", commands_factory=lambda: [Dec()], expected_bytes=[]),
    Case(
        label="AddVarTo7000",
        commands_factory=lambda: [AddVarTo7000()],
        expected_bytes=[],
    ),
    Case(
        label="DecVarFrom7000",
        commands_factory=lambda: [DecVarFrom7000()],
        expected_bytes=[],
    ),
    Case(
        label="GenerateRandomNumFromRangeVar",
        commands_factory=lambda: [GenerateRandomNumFromRangeVar()],
        expected_bytes=[],
    ),
    Case(
        label="SetVarToRandom",
        commands_factory=lambda: [SetVarToRandom()],
        expected_bytes=[],
    ),
    Case(
        label="CompareVarToConst",
        commands_factory=lambda: [CompareVarToConst()],
        expected_bytes=[],
    ),
    Case(
        label="Compare7000ToVar",
        commands_factory=lambda: [Compare7000ToVar()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000AndConst",
        commands_factory=lambda: [Mem7000AndConst()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000AndVar",
        commands_factory=lambda: [Mem7000AndVar()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000OrConst",
        commands_factory=lambda: [Mem7000OrConst()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000OrVar",
        commands_factory=lambda: [Mem7000OrVar()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000XorConst",
        commands_factory=lambda: [Mem7000XorConst()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000XorVar",
        commands_factory=lambda: [Mem7000XorVar()],
        expected_bytes=[],
    ),
    Case(
        label="VarShiftLeft",
        commands_factory=lambda: [VarShiftLeft()],
        expected_bytes=[],
    ),
    Case(
        label="MultiplyAndAddMem3148StoreToOffsrt7fB000PlusOutputX2",
        commands_factory=lambda: [
            MultiplyAndAddMem3148StoreToOffsrt7fB000PlusOutputX2()
        ],
        expected_bytes=[],
    ),
    Case(
        label="Xor3105With01",
        commands_factory=lambda: [Xor3105With01()],
        expected_bytes=[],
    ),
    Case(
        label="SetAsyncActionScript",
        commands_factory=lambda: [SetAsyncActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="SetSyncActionScript",
        commands_factory=lambda: [SetSyncActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="SetTempAsyncActionScript",
        commands_factory=lambda: [SetTempAsyncActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="SetTempSyncActionScript",
        commands_factory=lambda: [SetTempSyncActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="UnsyncActionScript",
        commands_factory=lambda: [UnsyncActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="SummonObjectToSpecificLevel",
        commands_factory=lambda: [SummonObjectToSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="SummonObjectToCurrentLevel",
        commands_factory=lambda: [SummonObjectToCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="SummonObjectToCurrentLevelAtMariosCoords",
        commands_factory=lambda: [SummonObjectToCurrentLevelAtMariosCoords()],
        expected_bytes=[],
    ),
    Case(
        label="SummonObjectAt70A8ToCurrentLevel",
        commands_factory=lambda: [SummonObjectAt70A8ToCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="RemoveObjectFromSpecificLevel",
        commands_factory=lambda: [RemoveObjectFromSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="RemoveObjectFromCurrentLevel",
        commands_factory=lambda: [RemoveObjectFromCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="RemoveObjectAt70A8FromCurrentLevel",
        commands_factory=lambda: [RemoveObjectAt70A8FromCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="PauseActionScript",
        commands_factory=lambda: [PauseActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="ResumeActionScript",
        commands_factory=lambda: [ResumeActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="EnableObjectTrigger",
        commands_factory=lambda: [EnableObjectTrigger()],
        expected_bytes=[],
    ),
    Case(
        label="DisableObjectTrigger",
        commands_factory=lambda: [DisableObjectTrigger()],
        expected_bytes=[],
    ),
    Case(
        label="EnableObjectTriggerInSpecificLevel",
        commands_factory=lambda: [EnableObjectTriggerInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="DisableObjectTriggerInSpecificLevel",
        commands_factory=lambda: [DisableObjectTriggerInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="EnableTriggerOfObjectAt70A8InCurrentLevel",
        commands_factory=lambda: [EnableTriggerOfObjectAt70A8InCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="DisableTriggerOfObjectAt70A8InCurrentLevel",
        commands_factory=lambda: [DisableTriggerOfObjectAt70A8InCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="StopEmbeddedActionScript",
        commands_factory=lambda: [StopEmbeddedActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="ResetCoords", commands_factory=lambda: [ResetCoords()], expected_bytes=[]
    ),
    Case(
        label="FreezeAllNPCsUntilReturn",
        commands_factory=lambda: [FreezeAllNPCsUntilReturn()],
        expected_bytes=[],
    ),
    Case(
        label="UnfreezeAllNPCs",
        commands_factory=lambda: [UnfreezeAllNPCs()],
        expected_bytes=[],
    ),
    Case(
        label="FreezeCamera",
        commands_factory=lambda: [FreezeCamera()],
        expected_bytes=[],
    ),
    Case(
        label="UnfreezeCamera",
        commands_factory=lambda: [UnfreezeCamera()],
        expected_bytes=[],
    ),
    Case(
        label="ReactivateObject70A8TriggerIfMarioOnTopOfIt",
        commands_factory=lambda: [ReactivateObject70A8TriggerIfMarioOnTopOfIt()],
        expected_bytes=[],
    ),
    Case(
        label="Set7000ToObjectCoord",
        commands_factory=lambda: [Set7000ToObjectCoord()],
        expected_bytes=[],
    ),
    Case(
        label="Set70107015ToObjectXYZ",
        commands_factory=lambda: [
            Set70107015ToObjectXYZ(NPC_0, bit_7=True),
            Set70107015ToObjectXYZ(MARIO),
        ],
        expected_bytes=[0xC7, 0x94, 0xC7, 0x00],
    ),
    Case(
        label="Set7016701BToObjectXYZ",
        commands_factory=lambda: [
            Set7016701BToObjectXYZ(MEM_70A8),
        ],
        expected_bytes=[0xC8, 0x10],
    ),
    Case(
        label="SetObjectMemoryToVar",
        commands_factory=lambda: [SetObjectMemoryToVar(SECONDARY_TEMP_7024)],
        expected_bytes=[0xD6, 0x12],
    ),
    Case(
        label="EnableControls",
        commands_factory=lambda: [
            EnableControls([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        ],
        expected_bytes=[0x35, 0xEF],
    ),
    Case(
        label="EnableControlsUntilReturn",
        commands_factory=lambda: [EnableControlsUntilReturn([B])],
        expected_bytes=[0x34, 0x80],
    ),
    Case(
        label="Set7000ToPressedButton",
        commands_factory=lambda: [Set7000ToPressedButton()],
        expected_bytes=[0xCA],
    ),
    Case(
        label="Set7000ToTappedButton",
        commands_factory=lambda: [Set7000ToTappedButton()],
        expected_bytes=[0xCB],
    ),
    Case(
        label="AddCoins",
        commands_factory=lambda: [AddCoins(PRIMARY_TEMP_7000), AddCoins(100)],
        expected_bytes=[0xFD, 0x52, 0x52, 0x64],
    ),
    Case(
        label="Dec7000FromCoins",
        commands_factory=lambda: [Dec7000FromCoins()],
        expected_bytes=[0xFD, 0x53],
    ),
    Case(
        label="AddFrogCoins",
        commands_factory=lambda: [
            AddFrogCoins(20),
        ],
        expected_bytes=[0x53, 0x14],
    ),
    Case(
        label="Dec7000FromFrogCoins",
        commands_factory=lambda: [Dec7000FromFrogCoins()],
        expected_bytes=[0xFD, 0x55],
    ),
    Case(
        label="Add7000ToCurrentFP",
        commands_factory=lambda: [Add7000ToCurrentFP()],
        expected_bytes=[0xFD, 0x56],
    ),
    Case(
        label="Dec7000FromCurrentFP",
        commands_factory=lambda: [Dec7000FromCurrentFP()],
        expected_bytes=[0x57],
    ),
    Case(
        label="Add7000ToMaxFP",
        commands_factory=lambda: [Add7000ToMaxFP()],
        expected_bytes=[0xFD, 0x57],
    ),
    Case(
        label="Dec7000FromCurrentHP",
        commands_factory=lambda: [Dec7000FromCurrentHP(MARIO)],
        expected_bytes=[0x56, 0x00],
    ),
    Case(
        label="EquipItemToCharacter",
        commands_factory=lambda: [
            EquipItemToCharacter(TroopaPin, MARIO),
        ],
        expected_bytes=[0x54, 0x00, 0x5C],
    ),
    Case(
        label="IncEXPByPacket",
        commands_factory=lambda: [IncEXPByPacket()],
        expected_bytes=[0xFD, 0x4B],
    ),
    Case(
        label="CharacterJoinsParty",
        commands_factory=lambda: [CharacterJoinsParty(TOADSTOOL)],
        expected_bytes=[0x36, 0x81],
    ),
    Case(
        label="CharacterLeavesParty",
        commands_factory=lambda: [CharacterLeavesParty(TOADSTOOL)],
        expected_bytes=[0x36, 0x01],
    ),
    Case(
        label="Store70A7ToEquipsInventory",
        commands_factory=lambda: [Store70A7ToEquipsInventory()],
        expected_bytes=[0xFD, 0x51],
    ),
    Case(
        label="AddToInventory",
        commands_factory=lambda: [
            AddToInventory(ITEM_ID),
            AddToInventory(CricketPie),
        ],
        expected_bytes=[0xFD, 0x50, 0x50, 0x82],
    ),
    Case(
        label="RemoveOneOfItemFromInventory",
        commands_factory=lambda: [
            RemoveOneOfItemFromInventory(Wallet),
        ],
        expected_bytes=[0x51, 0x81],
    ),
    Case(
        label="RestoreAllFP",
        commands_factory=lambda: [RestoreAllFP()],
        expected_bytes=[0xFD, 0x5C],
    ),
    Case(
        label="RestoreAllHP",
        commands_factory=lambda: [RestoreAllHP()],
        expected_bytes=[0xFD, 0x5B],
    ),
    Case(
        label="SetEXPPacketTo7000",
        commands_factory=lambda: [SetEXPPacketTo7000()],
        expected_bytes=[0xFD, 0x64],
    ),
    Case(
        label="Set7000ToIDOfMemberInSlot",
        commands_factory=lambda: [Set7000ToIDOfMemberInSlot(2)],
        expected_bytes=[0x38, 0x0A],
    ),
    Case(
        label="Set7000ToPartySize",
        commands_factory=lambda: [Set7000ToPartySize()],
        expected_bytes=[0x37],
    ),
    Case(
        label="StoreItemAt70A7QuantityTo7000",
        commands_factory=lambda: [StoreItemAt70A7QuantityTo7000()],
        expected_bytes=[0xFD, 0x5E],
    ),
    Case(
        label="StoreCharacterEquipmentTo7000",
        commands_factory=lambda: [
            StoreCharacterEquipmentTo7000(CHARACTER_IN_SLOT_3, Accessory)
        ],
        expected_bytes=[0xFD, 0x5D, 0x0A, 0x02],
    ),
    Case(
        label="StoreCurrentFPTo7000",
        commands_factory=lambda: [StoreCurrentFPTo7000()],
        expected_bytes=[0x58],
    ),
    Case(
        label="StoreEmptyItemInventorySlotCountTo7000",
        commands_factory=lambda: [StoreEmptyItemInventorySlotCountTo7000()],
        expected_bytes=[0x55],
    ),
    Case(
        label="StoreCoinCountTo7000",
        commands_factory=lambda: [StoreCoinCountTo7000()],
        expected_bytes=[0xFD, 0x59],
    ),
    Case(
        label="StoreItemAmountTo7000",
        commands_factory=lambda: [
            StoreItemAmountTo7000(YoshiCookie),
        ],
        expected_bytes=[0xFD, 0x58, 0x6D],
    ),
    Case(
        label="StoreFrogCoinCountTo7000",
        commands_factory=lambda: [StoreFrogCoinCountTo7000()],
        expected_bytes=[0xFD, 0x5A],
    ),
    Case(
        label="MarioGlows",
        commands_factory=lambda: [MarioGlows()],
        expected_bytes=[0xFD, 0xF9],
    ),
    Case(
        label="MarioStopsGlowing",
        commands_factory=lambda: [MarioStopsGlowing()],
        expected_bytes=[0xFD, 0xFA],
    ),
    Case(
        label="PaletteSet",
        commands_factory=lambda: [
            PaletteSet(palette_set=110, row=1, bit_0=True, bit_1=True, bit_3=True),
            PaletteSet(palette_set=89, row=7, bit_0=True),
        ],
        expected_bytes=[0x8A, 0x0B, 0x6E, 0x8A, 0x61, 0x59],
    ),
    Case(
        label="PaletteSetMorphs",
        commands_factory=lambda: [
            PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=41, row=1)
        ],
        expected_bytes=[0x89, 0xEA, 0x01, 0x29],
    ),
    Case(
        label="PauseScriptUntilEffectDone",
        commands_factory=lambda: [PauseScriptUntilEffectDone()],
        expected_bytes=[0x7F],
    ),
    Case(
        label="PixelateLayers",
        commands_factory=lambda: [
            PixelateLayers(
                layers=[LAYER_L1, LAYER_L2, LAYER_L3],
                pixel_size=9,
                duration=6,
                bit_6=True,
                bit_7=False,
            ),
        ],
        expected_bytes=[0x84, 0x97, 0x46],
    ),
    Case(
        label="PrioritySet",
        commands_factory=lambda: [
            PrioritySet(
                mainscreen=[LAYER_L3],
                subscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES],
                colour_math=[BACKGROUND, HALF_INTENSITY],
            ),
        ],
        expected_bytes=[0x81, 0x04, 0x13, 0x60],
    ),
    Case(
        label="ResetPrioritySet",
        commands_factory=lambda: [ResetPrioritySet()],
        expected_bytes=[0x82],
    ),
    Case(
        label="ScreenFlashesWithColour",
        commands_factory=lambda: [
            ScreenFlashesWithColour(YELLOW),
        ],
        expected_bytes=[0x83, 0x06],
    ),
    Case(
        label="TintLayers",
        commands_factory=lambda: [
            TintLayers(
                layers=[LAYER_L1, LAYER_L2, LAYER_L4, BACKGROUND],
                red=160,
                green=32,
                blue=32,
                speed=5,
                bit_15=True,
            ),
        ],
        expected_bytes=[0x80, 0x94, 0x90, 0x2B, 0x05],
    ),
    Case(
        label="CircleMaskExpandFromScreenCenter",
        commands_factory=lambda: [CircleMaskExpandFromScreenCenter()],
        expected_bytes=[0x7C],
    ),
    Case(
        label="CircleMaskShrinkToScreenCenter",
        commands_factory=lambda: [CircleMaskShrinkToScreenCenter()],
        expected_bytes=[0x7D],
    ),
    Case(
        label="CircleMaskShrinkToObject",
        commands_factory=lambda: [
            CircleMaskShrinkToObject(target=MARIO, width=18, speed=3, static=True),
        ],
        expected_bytes=[0x8F, 0x00, 0x12, 0x03],
    ),
    Case(
        label="StarMaskExpandFromScreenCenter",
        commands_factory=lambda: [StarMaskExpandFromScreenCenter()],
        expected_bytes=[0x7A],
    ),
    Case(
        label="StarMaskShrinkToScreenCenter",
        commands_factory=lambda: [StarMaskShrinkToScreenCenter()],
        expected_bytes=[0x7B],
    ),
    Case(
        label="FadeInFromBlack",
        commands_factory=lambda: [
            FadeInFromBlack(sync=True),
            FadeInFromBlack(sync=False),
            FadeInFromBlack(sync=True, duration=200),
            FadeInFromBlack(sync=False, duration=80),
        ],
        expected_bytes=[0x70, 0x71, 0x72, 0xC8, 0x73, 0x50],
    ),
    Case(
        label="FadeInFromColour",
        commands_factory=lambda: [
            FadeInFromColour(duration=90, colour=WHITE),
        ],
        expected_bytes=[0x78, 0x5A, 0x07],
    ),
    Case(
        label="FadeOutToBlack",
        commands_factory=lambda: [
            FadeOutToBlack(sync=False),
            FadeOutToBlack(sync=True, duration=100),
            FadeOutToBlack(sync=False, duration=50),
            FadeOutToBlack(sync=True),
        ],
        expected_bytes=[0x75, 0x76, 0x64, 0x77, 0x32, 0x74],
    ),
    Case(
        label="FadeOutToColour",
        commands_factory=lambda: [
            FadeOutToColour(duration=120, colour=WHITE),
        ],
        expected_bytes=[0x79, 0x78, 0x07],
    ),
    Case(
        label="InitiateBattleMask",
        commands_factory=lambda: [InitiateBattleMask()],
        expected_bytes=[0x7E],
    ),
    Case(
        label="SlowDownMusicTempoBy",
        commands_factory=lambda: [
            SlowDownMusicTempoBy(duration=0, change=2),
            SlowDownMusicTempoBy(duration=30, change=0),
        ],
        expected_bytes=[0x97, 0x00, 0x02, 0x97, 0x1E, 0x00],
    ),
    Case(
        label="SpeedUpMusicTempoBy",
        commands_factory=lambda: [
            SpeedUpMusicTempoBy(duration=255, change=24),
        ],
        expected_bytes=[0x97, 0xFF, 0xE8],
    ),
    Case(
        label="ReduceMusicPitchBy",
        commands_factory=lambda: [ReduceMusicPitchBy(duration=8, change=5)],
        expected_bytes=[0x98, 0x08, 0xFB],
    ),
    Case(
        label="IncreaseMusicPitchBy",
        commands_factory=lambda: [IncreaseMusicPitchBy(duration=11, change=3)],
        expected_bytes=[0x98, 0x0B, 0x03],
    ),
    Case(
        label="DeactivateSoundChannels",
        commands_factory=lambda: [
            DeactivateSoundChannels([0, 1, 2, 3]),
        ],
        expected_bytes=[0xFD, 0x94, 0x0F],
    ),
    Case(
        label="FadeInMusic",
        commands_factory=lambda: [
            FadeInMusic(M66_BOWSERS_CASTLE_2ND_TIME),
        ],
        expected_bytes=[0x92, 0x42],
    ),
    Case(
        label="FadeOutMusic",
        commands_factory=lambda: [FadeOutMusic()],
        expected_bytes=[0x93],
    ),
    Case(
        label="FadeOutMusicFDA3",
        commands_factory=lambda: [
            FadeOutMusicFDA3(),
        ],
        expected_bytes=[0xFD, 0xA3],
    ),
    Case(
        label="FadeOutMusicToVolume",
        commands_factory=lambda: [
            FadeOutMusicToVolume(duration=2, volume=96),
        ],
        expected_bytes=[0x95, 0x02, 0x60],
    ),
    Case(
        label="FadeOutSoundToVolume",
        commands_factory=lambda: [
            FadeOutSoundToVolume(duration=30, volume=100),
        ],
        expected_bytes=[0x9E, 0x1E, 0x64],
    ),
    Case(
        label="PlayMusic",
        commands_factory=lambda: [PlayMusic(M01_DODOS_COMING)],
        expected_bytes=[0xFD, 0x9E, 0x01],
    ),
    Case(
        label="PlayMusicAtCurrentVolume",
        commands_factory=lambda: [
            PlayMusicAtCurrentVolume(M23_GOT_A_STAR_PIECE_PART_1),
        ],
        expected_bytes=[0x90, 0x17],
    ),
    Case(
        label="PlayMusicAtDefaultVolume",
        commands_factory=lambda: [
            PlayMusicAtDefaultVolume(M02_MUSHROOM_KINGDOM),
        ],
        expected_bytes=[0x91, 0x02],
    ),
    Case(
        label="PlaySound",
        commands_factory=lambda: [
            PlaySound(sound=SO150_EXIT_TO_WORLD_MAP, channel=6),
            PlaySound(sound=SO006_RUNNING_WATER, channel=4),
        ],
        expected_bytes=[0x9C, 0x96, 0xFD, 0x9C, 0x06],
    ),
    Case(
        label="PlaySoundBalance",
        commands_factory=lambda: [
            PlaySoundBalance(sound=SO068_MALLOW_YELLING_AT_CROCO, balance=64)
        ],
        expected_bytes=[0x9D, 0x44, 0x40],
    ),
    Case(
        label="PlaySoundBalanceFD9D",
        commands_factory=lambda: [
            PlaySoundBalanceFD9D(sound=SO021_RUMBLING, balance=192),
        ],
        expected_bytes=[0xFD, 0x9D, 0x15, 0xC0],
    ),
    Case(
        label="SlowDownMusic",
        commands_factory=lambda: [SlowDownMusic()],
        expected_bytes=[0xFD, 0xA4],
    ),
    Case(
        label="SpeedUpMusicToDefault",
        commands_factory=lambda: [SpeedUpMusicToDefault()],
        expected_bytes=[0xFD, 0xA5],
    ),
    Case(
        label="StopMusic", commands_factory=lambda: [StopMusic()], expected_bytes=[0x94]
    ),
    Case(
        label="StopMusicFD9F",
        commands_factory=lambda: [StopMusicFD9F()],
        expected_bytes=[0xFD, 0x9F],
    ),
    Case(
        label="StopMusicFDA0",
        commands_factory=lambda: [StopMusicFDA0()],
        expected_bytes=[0xFD, 0xA0],
    ),
    Case(
        label="StopMusicFDA1",
        commands_factory=lambda: [StopMusicFDA1()],
        expected_bytes=[0xFD, 0xA1],
    ),
    Case(
        label="StopMusicFDA2",
        commands_factory=lambda: [StopMusicFDA2()],
        expected_bytes=[0xFD, 0xA2],
    ),
    Case(
        label="StopMusicFDA6",
        commands_factory=lambda: [StopMusicFDA6()],
        expected_bytes=[0xFD, 0xA6],
    ),
    Case(
        label="StopSound", commands_factory=lambda: [StopSound()], expected_bytes=[0x9B]
    ),
    Case(
        label="AppendDialogAt7000ToCurrentDialog",
        commands_factory=lambda: [
            AppendDialogAt7000ToCurrentDialog(closable=True, sync=False),
            AppendDialogAt7000ToCurrentDialog(closable=False, sync=True),
        ],
        expected_bytes=[0x63, 0xA0, 0x63, 0x00],
    ),
    Case(
        label="CloseDialog",
        commands_factory=lambda: [CloseDialog()],
        expected_bytes=[0x64],
    ),
    Case(
        label="PauseScriptResumeOnNextDialogPageA",
        commands_factory=lambda: [PauseScriptResumeOnNextDialogPageA()],
        expected_bytes=[0xFD, 0x60],
    ),
    Case(
        label="PauseScriptResumeOnNextDialogPageB",
        commands_factory=lambda: [PauseScriptResumeOnNextDialogPageB()],
        expected_bytes=[0xFD, 0x61],
    ),
    Case(
        label="RunDialog",
        commands_factory=lambda: [
            RunDialog(
                dialog_id=DI0519_MUSHROOM_INNKEEPER,
                above_object=MEM_70A8,
                closable=False,
                sync=False,
                multiline=True,
                use_background=True,
            ),
            RunDialog(
                dialog_id=DI0614_EMPTY,
                above_object=NPC_14,
                closable=True,
                sync=True,
                multiline=True,
                use_background=False,
            ),
            RunDialog(
                dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE,
                above_object=BOWSER,
                closable=True,
                sync=False,
                multiline=False,
                use_background=False,
            ),
        ],
        expected_bytes=[
            0x60,
            0x07,
            0x82,
            0xD0,
            0x60,
            0x66,
            0x22,
            0x62,
            0x60,
            0x0C,
            0xA2,
            0x02,
        ],
    ),
    Case(
        label="RunDialogForDuration",
        commands_factory=lambda: [
            RunDialogForDuration(dialog_id=DI1128_EMPTY, duration=1, sync=False),
            RunDialogForDuration(dialog_id=DI1180_MALLOW_JOINS, duration=1, sync=True),
            RunDialogForDuration(dialog_id=DI1186_EMPTY, duration=0, sync=False),
        ],
        expected_bytes=[0x62, 0x68, 0xA4, 0x62, 0x9C, 0x24, 0x62, 0xA2, 0x84],
    ),
    Case(
        label="UnsyncDialog",
        commands_factory=lambda: [UnsyncDialog()],
        expected_bytes=[0x65],
    ),
    Case(
        label="EnterArea",
        commands_factory=lambda: [
            EnterArea(
                room_id=R002_BOWSERS_KEEP_OUTSIDE_MARIO_ENTERS_AT_BEGINNING_OF_GAME,
                face_direction=SOUTHWEST,
                x=7,
                y=18,
                z=0,
                run_entrance_event=True,
            ),
            EnterArea(
                room_id=R006_MARRYMORE_INN_2F,
                face_direction=NORTHEAST,
                x=15,
                y=52,
                z=1,
                z_add_half_unit=True,
            ),
            EnterArea(
                room_id=R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN,
                face_direction=SOUTH,
                x=29,
                y=46,
                z=0,
                show_banner=True,
            ),
        ],
        expected_bytes=[
            0x68,
            0x02,
            0x80,
            0x07,
            0x12,
            0x60,
            0x68,
            0x06,
            0x00,
            0x0F,
            0xB4,
            0xE1,
            0x68,
            0xAB,
            0x09,
            0x1D,
            0x2E,
            0x40,
        ],
    ),
    Case(
        label="ApplyTileModToLevel",
        commands_factory=lambda: [
            ApplyTileModToLevel(
                use_alternate=True, room_id=R096_ROSE_TOWN_INN_2F, mod_id=1
            ),
            ApplyTileModToLevel(
                use_alternate=False, room_id=R052_MUSHROOM_KINGDOM_INN_2F, mod_id=0
            ),
        ],
        expected_bytes=[0x6A, 0x60, 0x82, 0x6A, 0x34, 0x00],
    ),
    Case(
        label="ApplySolidityModToLevel",
        commands_factory=lambda: [
            ApplySolidityModToLevel(
                permanent=False, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0
            ),
            ApplySolidityModToLevel(
                permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=3
            ),
        ],
        expected_bytes=[0x6B, 0x54, 0x00, 0x6B, 0x53, 0x86],
    ),
    Case(
        label="ExitToWorldMap",
        commands_factory=lambda: [
            ExitToWorldMap(area=OW27_BOOSTER_HILL, bit_6=True, bit_7=True),
        ],
        expected_bytes=[0x4B, 0x1B, 0xC0],
    ),
    Case(
        label="Set7000ToCurrentLevel",
        commands_factory=lambda: [Set7000ToCurrentLevel()],
        expected_bytes=[0xC3],
    ),
    Case(
        label="DisplayIntroTitleText",
        commands_factory=lambda: [
            DisplayIntroTitleText(KING_BOWSER, y=6),
        ],
        expected_bytes=[0xFD, 0x66, 0x06, 0x02],
    ),
    Case(
        label="ExorCrashesIntoKeep",
        commands_factory=lambda: [ExorCrashesIntoKeep()],
        expected_bytes=[0xFD, 0xF8],
    ),
    Case(
        label="RunMenuOrEventSequence",
        commands_factory=lambda: [
            RunMenuOrEventSequence(SC15_ENTER_GATE_TO_SMITHY_FACTORY),
        ],
        expected_bytes=[0x4F, 0x0F],
    ),
    Case(
        label="OpenSaveMenu",
        commands_factory=lambda: [OpenSaveMenu()],
        expected_bytes=[0xFD, 0x4A],
    ),
    Case(
        label="OpenShop",
        commands_factory=lambda: [
            OpenShop(SH02_ROSE_TOWN_ARMOR),
        ],
        expected_bytes=[0x4C, 0x02],
    ),
    Case(
        label="PauseScriptIfMenuOpen",
        commands_factory=lambda: [PauseScriptIfMenuOpen()],
        expected_bytes=[0x5B],
    ),
    Case(
        label="ResetAndChooseGame",
        commands_factory=lambda: [ResetAndChooseGame()],
        expected_bytes=[0xFB],
    ),
    Case(
        label="ResetGame", commands_factory=lambda: [ResetGame()], expected_bytes=[0xFC]
    ),
    Case(
        label="RunEndingCredits",
        commands_factory=lambda: [RunEndingCredits()],
        expected_bytes=[0xFD, 0x67],
    ),
    Case(
        label="RunEventSequence",
        commands_factory=lambda: [
            RunEventSequence(scene=SC16_RUN_WORLD_MAP_EVENT_SEQUENCE, value=2),
        ],
        expected_bytes=[0x4E, 0x10, 0x02],
    ),
    Case(
        label="RunLevelupBonusSequence",
        commands_factory=lambda: [RunLevelupBonusSequence()],
        expected_bytes=[0xFD, 0x65],
    ),
    Case(
        label="RunMenuTutorial",
        commands_factory=lambda: [
            RunMenuTutorial(TU02_HOW_TO_SWITCH),
        ],
        expected_bytes=[0xFD, 0x4C, 0x02],
    ),
    Case(
        label="RunMolevilleMountainIntroSequence",
        commands_factory=lambda: [RunMolevilleMountainIntroSequence()],
        expected_bytes=[0xFD, 0x4F],
    ),
    Case(
        label="RunMolevilleMountainSequence",
        commands_factory=lambda: [RunMolevilleMountainSequence()],
        expected_bytes=[0xFD, 0x4E],
    ),
    Case(
        label="RunStarPieceSequence",
        commands_factory=lambda: [
            RunStarPieceSequence(8),
        ],
        expected_bytes=[0xFD, 0x4D, 0x08],
    ),
    Case(
        label="StartBattleAtBattlefield",
        commands_factory=lambda: [
            StartBattleAtBattlefield(
                PACK0198_TOADSTOOL_CLONE_HENCHMAN, BF21_KERO_SEWERS
            ),
        ],
        expected_bytes=[0x4A, 0xC6, 0x00, 0x15],
    ),
    Case(
        label="StartBattleWithPackAt700E",
        commands_factory=lambda: [StartBattleWithPackAt700E()],
        expected_bytes=[0x49],
    ),
    #
    # Tests with GOTOs
    #
    Case(
        "Basic GOTO",
        commands_factory=lambda: [
            StopSound(),
            Set7000ToTappedButton(identifier="jmp_here"),
            Jmp(destinations=["jmp_here"]),
        ],
        expected_bytes=[0x9B, 0xCB, 0xD2, 0x03, 0x00],
    ),
    Case(
        "Should fail if GOTO destination doesn't match anything",
        commands_factory=lambda: [
            StopSound(),
            Set7000ToTappedButton(identifier="jmp_fails"),
            Jmp(destinations=["jmp_here"]),
        ],
        exception="couldn't find destination jmp_here",
        exception_type=IdentifierException,
    ),
    Case(
        "Should fail if GOTO finds multiple matches",
        commands_factory=lambda: [
            StopSound(),
            Set7000ToTappedButton(identifier="jmp_here"),
            Jmp(destinations=["jmp_here"]),
            Return(identifier="jmp_here"),
        ],
        exception="duplicate command identifier found: jmp_here",
        exception_type=IdentifierException,
    ),
    Case(
        "Should not fail if GOTO destination uses illegal override format",
        commands_factory=lambda: [
            StopSound(),
            Set7000ToTappedButton(),
            Jmp(destinations=["ILLEGAL_JUMP_0001"]),
        ],
        expected_bytes=[0x9B, 0xCB, 0xD2, 0x01, 0x00],
    ),
    Case(
        label="If0210Bits012ClearDoNotJump",
        commands_factory=lambda: [
            If0210Bits012ClearDoNotJump(["end_here"]),
            Return(identifier="end_here"),
        ],
        expected_bytes=[0xFD, 0x62, 0x06, 0x00, 0xFE],
    ),
    Case(label="Jmp", commands_factory=lambda: [Jmp()], expected_bytes=[]),
    Case(
        label="JmpToEvent", commands_factory=lambda: [JmpToEvent()], expected_bytes=[]
    ),
    Case(
        label="JmpToStartOfThisScript",
        commands_factory=lambda: [JmpToStartOfThisScript()],
        expected_bytes=[],
    ),
    Case(
        label="JmpToStartOfThisScriptFA",
        commands_factory=lambda: [JmpToStartOfThisScriptFA()],
        expected_bytes=[],
    ),
    Case(
        label="JmpToSubroutine",
        commands_factory=lambda: [JmpToSubroutine()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIf316DIs3",
        commands_factory=lambda: [JmpIf316DIs3()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIf7000AllBitsClear",
        commands_factory=lambda: [JmpIf7000AllBitsClear()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIf7000AnyBitsSet",
        commands_factory=lambda: [JmpIf7000AnyBitsSet()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfBitSet", commands_factory=lambda: [JmpIfBitSet()], expected_bytes=[]
    ),
    Case(
        label="JmpIfBitClear",
        commands_factory=lambda: [JmpIfBitClear()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfLoadedMemoryIs0",
        commands_factory=lambda: [JmpIfLoadedMemoryIs0()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfLoadedMemoryIsAboveOrEqual0",
        commands_factory=lambda: [JmpIfLoadedMemoryIsAboveOrEqual0()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfLoadedMemoryIsBelow0",
        commands_factory=lambda: [JmpIfLoadedMemoryIsBelow0()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfLoadedMemoryIsNot0",
        commands_factory=lambda: [JmpIfLoadedMemoryIsNot0()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfMem704XAt7000BitSet",
        commands_factory=lambda: [JmpIfMem704XAt7000BitSet()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfMem704XAt7000BitClear",
        commands_factory=lambda: [JmpIfMem704XAt7000BitClear()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfRandom2of3",
        commands_factory=lambda: [JmpIfRandom2of3()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfRandom1of2",
        commands_factory=lambda: [JmpIfRandom1of2()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfComparisonResultIsGreaterOrEqual",
        commands_factory=lambda: [JmpIfComparisonResultIsGreaterOrEqual()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfComparisonResultIsLesser",
        commands_factory=lambda: [JmpIfComparisonResultIsLesser()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfVarEqualsConst",
        commands_factory=lambda: [JmpIfVarEqualsConst()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfVarNotEqualsConst",
        commands_factory=lambda: [JmpIfVarNotEqualsConst()],
        expected_bytes=[],
    ),
    Case(
        label="CreatePacketAtObjectCoords",
        commands_factory=lambda: [CreatePacketAtObjectCoords()],
        expected_bytes=[],
    ),
    Case(
        label="CreatePacketAt7010",
        commands_factory=lambda: [CreatePacketAt7010()],
        expected_bytes=[],
    ),
    Case(
        label="CreatePacketAt7010WithEvent",
        commands_factory=lambda: [CreatePacketAt7010WithEvent()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfMarioOnObject",
        commands_factory=lambda: [JmpIfMarioOnObject()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfMarioOnAnObjectOrNot",
        commands_factory=lambda: [JmpIfMarioOnAnObjectOrNot()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectInAir",
        commands_factory=lambda: [JmpIfObjectInAir()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectInSpecificLevel",
        commands_factory=lambda: [JmpIfObjectInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectInCurrentLevel",
        commands_factory=lambda: [JmpIfObjectInCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectNotInSpecificLevel",
        commands_factory=lambda: [JmpIfObjectNotInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectTriggerEnabledInSpecificLevel",
        commands_factory=lambda: [JmpIfObjectTriggerEnabledInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectTriggerDisabledInSpecificLevel",
        commands_factory=lambda: [JmpIfObjectTriggerDisabledInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectIsUnderwater",
        commands_factory=lambda: [JmpIfObjectIsUnderwater()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectActionScriptIsRunning",
        commands_factory=lambda: [JmpIfObjectActionScriptIsRunning()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectsAreLessThanXYStepsApart",
        commands_factory=lambda: [JmpIfObjectsAreLessThanXYStepsApart()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectsAreLessThanXYStepsApartSameZCoord",
        commands_factory=lambda: [JmpIfObjectsAreLessThanXYStepsApartSameZCoord()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfMarioInAir",
        commands_factory=lambda: [JmpIfMarioInAir()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAudioMemoryIsAtLeast",
        commands_factory=lambda: [JmpIfAudioMemoryIsAtLeast()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAudioMemoryEquals",
        commands_factory=lambda: [JmpIfAudioMemoryEquals()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfDialogOptionBSelected",
        commands_factory=lambda: [JmpIfDialogOptionBSelected()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfDialogOptionBOrCSelected",
        commands_factory=lambda: [JmpIfDialogOptionBOrCSelected()],
        expected_bytes=[],
    ),
    #
    # Embedded action queue tests
    #
    Case(
        label="ActionQueueAsync",
        commands_factory=lambda: [ActionQueueAsync()],
        expected_bytes=[],
    ),
    Case(
        label="ActionQueueSync",
        commands_factory=lambda: [ActionQueueSync()],
        expected_bytes=[],
    ),
    Case(
        label="StartAsyncEmbeddedActionScript",
        commands_factory=lambda: [StartAsyncEmbeddedActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="StartSyncEmbeddedActionScript",
        commands_factory=lambda: [StartSyncEmbeddedActionScript()],
        expected_bytes=[],
    ),
    #
    # Non-embedded action queue tests
    #
    Case(
        "NEAQ already in desired position",
        commands_factory=lambda: [
            StopSound(),
            StopSound(),
            StopSound(),
            NonEmbeddedActionQueue(
                required_offset=0x03, subscript=[A_AddConstToVar(PRIMARY_TEMP_700C, 10)]
            ),
        ],
        expected_bytes=[0x9B, 0x9B, 0x9B, 0xAD, 0x0A, 0x00],
    ),
    Case(
        "NEAQ is too early, inserts dummy commands to make up the difference",
        commands_factory=lambda: [
            StopSound(),
            NonEmbeddedActionQueue(
                required_offset=0x05, subscript=[A_AddConstToVar(PRIMARY_TEMP_700C, 10)]
            ),
        ],
        expected_bytes=[0x9B, 0x9B, 0x9B, 0x9B, 0x9B, 0xAD, 0x0A, 0x00],
    ),
    Case(
        "NEAQ should fail if it would be rendered after required offset",
        commands_factory=lambda: [
            StopSound(),
            StopSound(),
            NonEmbeddedActionQueue(
                required_offset=0x01, subscript=[A_AddConstToVar(PRIMARY_TEMP_700C, 10)]
            ),
        ],
        exception="too many commands in script 0 before non-embedded action queue",
        exception_type=ScriptBankTooLongException,
    ),
    Case(
        "background thread",
        commands_factory=lambda: [MoveScriptToBackgroundThread1()],
        expected_bytes=[0xFD, 0x41],
    ),
    #
    # Unknown command tests
    #
    Case(
        "Valid unknown command",
        commands_factory=lambda: [
            UnknownCommand(bytearray([0xCC])),
        ],
        expected_bytes=[0xCC],
    ),
    Case(
        "Unknown command with wrong length should fail",
        commands_factory=lambda: [UnknownCommand(bytearray([0x96, 0xAB]))],
        exception="opcode 0x96 expects 3 total bytes (inclusive), got 2 bytes instead",
        exception_type=InvalidCommandArgumentException,
    ),
    Case(
        "Unknown command using an assigned opcode should fail",
        commands_factory=lambda: [UnknownCommand(bytearray([0xC7, 0x90]))],
        exception="do not use UnknownCommand for opcode 0xC7, there is already a class for it",
        exception_type=InvalidCommandArgumentException,
    ),
    Case(
        "Valid unknown command (FD)",
        commands_factory=lambda: [
            UnknownCommand(bytearray([0xFD, 0xF1])),
        ],
        expected_bytes=[0xFD, 0xF1],
    ),
    Case(
        "Unknown command with wrong length should fail (FD)",
        commands_factory=lambda: [UnknownCommand(bytearray([0xFD, 0x98]))],
        exception="opcode 0xFD 0x98 expects 3 total bytes (inclusive), got 2 bytes instead",
        exception_type=InvalidCommandArgumentException,
    ),
    Case(
        "Unknown command using an assigned opcode should fail (FD)",
        commands_factory=lambda: [
            UnknownCommand(bytearray([0xFD, 0x9C, 0x01, 0x02, 0x03]))
        ],
        exception="do not use UnknownCommand for opcode 0xFD 0x9C, there is already a class for it",
        exception_type=InvalidCommandArgumentException,
    ),
]


@pytest.mark.parametrize("case", test_cases, ids=lambda case: case.label)
def test_add(case: Case):
    if case.expected_bytes is not None and len(case.expected_bytes) == 0:
        return
    if case.exception or case.exception_type:
        with pytest.raises(case.exception_type) as exc_info:
            commands = case.commands_factory()
            script = EventScript(commands)
            bank = EventScriptBank(0x1E0000, 0x1E0002, 0x1EFFFF, [script])
            bank.render()
        if case.exception:
            assert case.exception in str(exc_info.value)
    elif case.expected_bytes is not None:
        commands = case.commands_factory()
        script = EventScript(commands)
        expected_bytes = bytearray(case.expected_bytes)
        bank = EventScriptBank(
            0x1E0000, 0x1E0002, 0x1E0002 + len(expected_bytes), [script]
        )
        assert bank.render() == bytearray([0x02, 0x00]) + expected_bytes
    else:
        raise "At least one of exception or expected_bytes needs to be set"
