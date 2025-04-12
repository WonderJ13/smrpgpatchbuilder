"""Spell definitions"""

from typing import List

from smrpgpatchbuilder.datatypes.spells.classes import (
    CharacterSpell,
    EnemySpell,
    EffectType,
    InflictFunction,
    TempStatBuff,
    Element,
    Status,
    SpellType,
)
from smrpgpatchbuilder.datatypes.spells.arguments.types.classes import DamageModifiers, TimingProperties
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (
    NO_MODIFIERS,
    X00625_MODIFIER,
    X00625_MODIFIER_WITH_MULTI_TARGETING,
    X0125_MODIFIER_WITH_MULTI_TARGETING,
    X05_MODIFIER,
)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    BUTTON_MASH,
    CHARGE_ONLY,
    MULTIPLE_BUTTON_PRESSES,
    ONE_PLUS_MORE_TARGETS_WITH_PRESSES,
    ONE_TIMING_FOR_125_DMG_ONLY,
    ONE_TIMING_FOR_125_OR_15X_DMG,
    ROTATE_1_TARGET_IF_TIMED_ALL,
    ROTATE_ONLY,
    TIME_TO_ACTIVATE_HP_READ,
    TIMED_FOR_9999_SET_ENEMY_HP_0,
    TIMED_GIVES_TARGET_DEFENSE_UP_BUFF,
    TIMED_HEALS_ALL_HP_TO_FIRST_TARGET,
    TIMED_JUMPS
)

class Jump(CharacterSpell):
    """Learnable spell definition for Jump"""

    _index: int = 0
    _fp: int = 3
    _power: int = 25
    _hit_rate: int = 100

    _title: str = "Jump"

    _anim_ptr: int = 0x35C9CE
    _desc_ptr: int = 0x3A40A3

    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _inflict: InflictFunction = InflictFunction.INC_JUMP
    _element: Element = Element.JUMP

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _quad9s: bool = False
    _hide_num: bool = False

    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False

    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []

    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 512


class FireOrb(CharacterSpell):
    """Learnable spell definition for FireOrb"""

    _index: int = 1
    _fp: int = 5
    _power: int = 20
    _hit_rate: int = 100
    _title: str = "Fire Orb"
    _anim_ptr: int = 0x35C9D2
    _desc_ptr: int = 0x3A2BDF

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.FIRE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 513


class SuperJump(CharacterSpell):
    """Learnable spell definition for SuperJump"""

    _index: int = 2
    _fp: int = 7
    _power: int = 45
    _hit_rate: int = 100
    _title: str = "Super Jump"
    _anim_ptr: int = 0x35C9D6
    _desc_ptr: int = 0x3A2C01

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.JUMP
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers: DamageModifiers = X05_MODIFIER

    _item_id: int = 514


class SuperFlame(CharacterSpell):
    """Learnable spell definition for SuperFlame"""

    _index: int = 3
    _fp: int = 9
    _power: int = 40
    _hit_rate: int = 100
    _title: str = "Super Flame"
    _anim_ptr: int = 0x35C9DA
    _desc_ptr: int = 0x3A2C26

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.FIRE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 515


class UltraJump(CharacterSpell):
    """Learnable spell definition for UltraJump"""

    _index: int = 4
    _fp: int = 11
    _power: int = 65
    _hit_rate: int = 100
    _title: str = "Ultra Jump"
    _anim_ptr: int = 0x35C9E4
    _desc_ptr: int = 0x3A2C4A

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.JUMP
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ONE_PLUS_MORE_TARGETS_WITH_PRESSES
    _damage_modifiers: DamageModifiers = X0125_MODIFIER_WITH_MULTI_TARGETING

    _item_id: int = 516


class UltraFlame(CharacterSpell):
    """Learnable spell definition for UltraFlame"""

    _index: int = 5
    _fp: int = 14
    _power: int = 60
    _hit_rate: int = 100
    _title: str = "Ultra Flame"
    _anim_ptr: int = 0x35C9E8
    _desc_ptr: int = 0x3A2C6F

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.FIRE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ONE_PLUS_MORE_TARGETS_WITH_PRESSES
    _damage_modifiers: DamageModifiers = X00625_MODIFIER_WITH_MULTI_TARGETING

    _item_id: int = 517


class Therapy(CharacterSpell):
    """Learnable spell definition for Therapy"""

    _index: int = 6
    _fp: int = 2
    _power: int = 40
    _hit_rate: int = 100
    _title: str = "Therapy"
    _anim_ptr: int = 0x35C9F2
    _desc_ptr: int = 0x3A2C92

    _check_stats: bool = False
    _ignore_defense: bool = True
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = True
    _spell_type: SpellType = SpellType.HEAL
    _effect_type: EffectType = EffectType.NULLIFY
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = False
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 518


class GroupHug(CharacterSpell):
    """Learnable spell definition for GroupHug"""

    _index: int = 7
    _fp: int = 4
    _power: int = 30
    _hit_rate: int = 100
    _title: str = "Group Hug"
    _anim_ptr: int = 0x35C9FC
    _desc_ptr: int = 0x3A2CA6

    _check_stats: bool = False
    _ignore_defense: bool = True
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = True
    _spell_type: SpellType = SpellType.HEAL
    _effect_type: EffectType = EffectType.NULLIFY
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = False
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_DMG_ONLY
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 519


class SleepyTime(CharacterSpell):
    """Learnable spell definition for SleepyTime"""

    _index: int = 8
    _fp: int = 4
    _hit_rate: int = 99
    _title: str = "Sleepy Time"
    _anim_ptr: int = 0x35CA00
    _desc_ptr: int = 0x3A2CBF

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.SLEEP]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = True
    _timing_modifiers: TimingProperties = ROTATE_1_TARGET_IF_TIMED_ALL
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 520


class ComeBack(CharacterSpell):
    """Learnable spell definition for ComeBack"""

    _index: int = 9
    _fp: int = 2
    _hit_rate: int = 100
    _title: str = "Come Back"
    _anim_ptr: int = 0x35CA07
    _desc_ptr: int = 0x3A2CD6

    _check_stats: bool = False
    _ignore_defense: bool = True
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.HEAL
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = False
    _target_party: bool = False
    _target_wounded: bool = True
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction = InflictFunction.REVIVE
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = TIMED_HEALS_ALL_HP_TO_FIRST_TARGET
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 521


class Mute(CharacterSpell):
    """Learnable spell definition for Mute"""

    _index: int = 10
    _fp: int = 3
    _hit_rate: int = 99
    _title: str = "Mute"
    _anim_ptr: int = 0x35CA11
    _desc_ptr: int = 0x3A2CF4

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.MUTE]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = True
    _timing_modifiers: TimingProperties = ROTATE_1_TARGET_IF_TIMED_ALL
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 522


class PsychBomb(CharacterSpell):
    """Learnable spell definition for PsychBomb"""

    _index: int = 11
    _fp: int = 15
    _power: int = 60
    _hit_rate: int = 100
    _title: str = "Psych Bomb"
    _anim_ptr: int = 0x35CA1B
    _desc_ptr: int = 0x3A2D0C

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = BUTTON_MASH
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 523


class Terrorize(CharacterSpell):
    """Learnable spell definition for Terrorize"""

    _index: int = 12
    _fp: int = 6
    _power: int = 10
    _hit_rate: int = 90
    _title: str = "Terrorize"
    _anim_ptr: int = 0x35CA22
    _desc_ptr: int = 0x3A2D26

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.FEAR]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ROTATE_ONLY
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 524


class PoisonGas(CharacterSpell):
    """Learnable spell definition for PoisonGas"""

    _index: int = 13
    _fp: int = 10
    _power: int = 20
    _hit_rate: int = 90
    _title: str = "Poison Gas"
    _anim_ptr: int = 0x35CA2C
    _desc_ptr: int = 0x3A2D36

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.POISON]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ROTATE_ONLY
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 525


class Crusher(CharacterSpell):
    """Learnable spell definition for Crusher"""

    _index: int = 14
    _fp: int = 12
    _power: int = 60
    _hit_rate: int = 100
    _title: str = "Crusher"
    _anim_ptr: int = 0x35CA36
    _desc_ptr: int = 0x3A2D44

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 526


class BowserCrush(CharacterSpell):
    """Learnable spell definition for BowserCrush"""

    _index: int = 15
    _fp: int = 16
    _power: int = 58
    _hit_rate: int = 100
    _title: str = "Bowser Crush"
    _anim_ptr: int = 0x35CA40
    _desc_ptr: int = 0x3A2D6D

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = BUTTON_MASH
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 527


class GenoBeam(CharacterSpell):
    """Learnable spell definition for GenoBeam"""

    _index: int = 16
    _fp: int = 3
    _power: int = 40
    _hit_rate: int = 100
    _title: str = "Geno Beam"
    _anim_ptr: int = 0x35CA47
    _desc_ptr: int = 0x3A2D87

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = CHARGE_ONLY
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 528


class GenoBoost(CharacterSpell):
    """Learnable spell definition for GenoBoost"""

    _index: int = 17
    _fp: int = 4
    _hit_rate: int = 100
    _title: str = "Geno Boost"
    _anim_ptr: int = 0x35CA4E
    _desc_ptr: int = 0x3A2DB0

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = False
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = [TempStatBuff.MAGIC_ATTACK, TempStatBuff.ATTACK]
    _inflict: InflictFunction
    _hide_num: bool = True
    _timing_modifiers: TimingProperties = TIMED_GIVES_TARGET_DEFENSE_UP_BUFF
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 529


class GenoWhirl(CharacterSpell):
    """Learnable spell definition for GenoWhirl"""

    _index: int = 18
    _fp: int = 8
    _power: int = 45
    _hit_rate: int = 100
    _title: str = "Geno Whirl"
    _anim_ptr: int = 0x35CA58
    _desc_ptr: int = 0x3A2DD8

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = TIMED_FOR_9999_SET_ENEMY_HP_0
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 530


class GenoBlast(CharacterSpell):
    """Learnable spell definition for GenoBlast"""

    _index: int = 19
    _fp: int = 12
    _power: int = 50
    _hit_rate: int = 100
    _title: str = "Geno Blast"
    _anim_ptr: int = 0x35CA62
    _desc_ptr: int = 0x3A2E05

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = CHARGE_ONLY
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 531


class GenoFlash(CharacterSpell):
    """Learnable spell definition for GenoFlash"""

    _index: int = 20
    _fp: int = 16
    _power: int = 60
    _hit_rate: int = 100
    _title: str = "Geno Flash"
    _anim_ptr: int = 0x35CA69
    _desc_ptr: int = 0x3A2E26

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = CHARGE_ONLY
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 532

class Thunderbolt(CharacterSpell):
    """Learnable spell definition for Thunderbolt"""

    _index: int = 21
    _fp: int = 2
    _power: int = 15
    _hit_rate: int = 100
    _title: str = "Thunderbolt"
    _anim_ptr: int = 0x35CA73
    _desc_ptr: int = 0x3A2E4A

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.THUNDER
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_DMG_ONLY
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 533


class HPRain(CharacterSpell):
    """Learnable spell definition for HPRain"""

    _index: int = 22
    _fp: int = 2
    _power: int = 10
    _hit_rate: int = 100
    _title: str = "HP Rain"
    _anim_ptr: int = 0x35CA7D
    _desc_ptr: int = 0x3A2E6C

    _check_stats: bool = False
    _ignore_defense: bool = True
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = True
    _spell_type: SpellType = SpellType.HEAL
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = False
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 534


class Psychopath(CharacterSpell):
    """Learnable spell definition for Psychopath"""

    _index: int = 23
    _fp: int = 1
    _hit_rate: int = 100
    _title: str = "Psychopath"
    _anim_ptr: int = 0x35CA84
    _desc_ptr: int = 0x3A2E9E

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction = InflictFunction.SCAN
    _hide_num: bool = True
    _timing_modifiers: TimingProperties = TIME_TO_ACTIVATE_HP_READ
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 535


class Shocker(CharacterSpell):
    """Learnable spell definition for Shocker"""

    _index: int = 24
    _fp: int = 8
    _power: int = 60
    _hit_rate: int = 100
    _title: str = "Shocker"
    _anim_ptr: int = 0x35CA8E
    _desc_ptr: int = 0x3A2EBC

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.THUNDER
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers: DamageModifiers = NO_MODIFIERS

    _item_id: int = 536


class Snowy(CharacterSpell):
    """Learnable spell definition for Snowy"""

    _index: int = 25
    _fp: int = 12
    _power: int = 40
    _hit_rate: int = 100
    _title: str = "Snowy"
    _anim_ptr: int = 0x35CA98
    _desc_ptr: int = 0x3A2EDE

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.ICE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = ROTATE_ONLY
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 537


class StarRain(CharacterSpell):
    """Learnable spell definition for StarRain"""

    _index: int = 26
    _fp: int = 14
    _power: int = 55
    _hit_rate: int = 100
    _title: str = "Star Rain"
    _anim_ptr: int = 0x35CAA2
    _desc_ptr: int = 0x3A2EF4

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False
    _timing_modifiers: TimingProperties = TIMED_JUMPS
    _damage_modifiers: DamageModifiers = X00625_MODIFIER

    _item_id: int = 538
    

class Drain(EnemySpell):
    """Learnable spell definition for Drain"""

    _index: int = 64
    _fp: int = 1
    _power: int = 4
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.FIRE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class LightningOrb(EnemySpell):
    """Learnable spell definition for LightningOrb"""

    _index: int = 65
    _fp: int = 2
    _power: int = 8
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.THUNDER
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Flame(EnemySpell):
    """Learnable spell definition for Flame"""

    _index: int = 66
    _fp: int = 3
    _power: int = 12
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.FIRE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Bolt(EnemySpell):
    """Learnable spell definition for Bolt"""

    _index: int = 67
    _fp: int = 4
    _power: int = 20
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.THUNDER
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Crystal(EnemySpell):
    """Learnable spell definition for Crystal"""

    _index: int = 68
    _fp: int = 5
    _power: int = 25
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.ICE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class FlameStone(EnemySpell):
    """Learnable spell definition for FlameStone"""

    _index: int = 69
    _fp: int = 6
    _power: int = 32
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.FIRE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class MegaDrain(EnemySpell):
    """Learnable spell definition for MegaDrain"""

    _index: int = 70
    _fp: int = 7
    _power: int = 40
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.FIRE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class WillyWisp(EnemySpell):
    """Learnable spell definition for WillyWisp"""

    _index: int = 71
    _fp: int = 8
    _power: int = 48
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class DiamondSaw(EnemySpell):
    """Learnable spell definition for DiamondSaw"""

    _index: int = 72
    _fp: int = 9
    _power: int = 60
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Electroshock(EnemySpell):
    """Learnable spell definition for Electroshock"""

    _index: int = 73
    _fp: int = 10
    _power: int = 72
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.THUNDER
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Blast(EnemySpell):
    """Learnable spell definition for Blast"""

    _index: int = 74
    _fp: int = 11
    _power: int = 89
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Storm(EnemySpell):
    """Learnable spell definition for Storm"""

    _index: int = 75
    _fp: int = 12
    _power: int = 108
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class IceRock(EnemySpell):
    """Learnable spell definition for IceRock"""

    _index: int = 76
    _fp: int = 13
    _power: int = 130
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.ICE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Escape(EnemySpell):
    """Learnable spell definition for Escape"""

    _index: int = 77
    _hit_rate: int = 100

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = False
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction = InflictFunction.NO_DMG
    _hide_num: bool = False


class DarkStar(EnemySpell):
    """Learnable spell definition for DarkStar"""

    _index: int = 78
    _fp: int = 20
    _power: int = 160
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = True
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Recover(EnemySpell):
    """Learnable spell definition for Recover"""

    _index: int = 79
    _fp: int = 3
    _power: int = 50
    _hit_rate: int = 100

    _check_stats: bool = False
    _ignore_defense: bool = True
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.HEAL
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = False
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class MegaRecover(EnemySpell):
    """Learnable spell definition for MegaRecover"""

    _index: int = 80
    _fp: int = 9
    _power: int = 200
    _hit_rate: int = 100

    _check_stats: bool = False
    _ignore_defense: bool = True
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.HEAL
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = False
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class FlameWall(EnemySpell):
    """Learnable spell definition for FlameWall"""

    _index: int = 81
    _fp: int = 2
    _power: int = 8
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.FIRE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class StaticE(EnemySpell):
    """Learnable spell definition for StaticE"""

    _index: int = 82
    _fp: int = 4
    _power: int = 12
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.THUNDER
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class SandStorm(EnemySpell):
    """Learnable spell definition for SandStorm"""

    _index: int = 83
    _fp: int = 6
    _power: int = 16
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.FEAR]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Blizzard(EnemySpell):
    """Learnable spell definition for Blizzard"""

    _index: int = 84
    _fp: int = 8
    _power: int = 22
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.ICE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class DrainBeam(EnemySpell):
    """Learnable spell definition for DrainBeam"""

    _index: int = 85
    _fp: int = 10
    _power: int = 26
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class MeteorBlast(EnemySpell):
    """Learnable spell definition for MeteorBlast"""

    _index: int = 86
    _fp: int = 12
    _power: int = 30
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class LightBeam(EnemySpell):
    """Learnable spell definition for LightBeam"""

    _index: int = 87
    _fp: int = 13
    _power: int = 34
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.SLEEP]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class WaterBlast(EnemySpell):
    """Learnable spell definition for WaterBlast"""

    _index: int = 88
    _fp: int = 14
    _power: int = 39
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Solidify(EnemySpell):
    """Learnable spell definition for Solidify"""

    _index: int = 89
    _fp: int = 15
    _power: int = 47
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.ICE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class PetalBlast(EnemySpell):
    """Learnable spell definition for PetalBlast"""

    _index: int = 90
    _fp: int = 16
    _power: int = 40
    _hit_rate: int = 85

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.MUSHROOM]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class AuroraFlash(EnemySpell):
    """Learnable spell definition for AuroraFlash"""

    _index: int = 91
    _fp: int = 17
    _power: int = 50
    _hit_rate: int = 85

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.SLEEP]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Boulder(EnemySpell):
    """Learnable spell definition for Boulder"""

    _index: int = 92
    _fp: int = 18
    _power: int = 72
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Corona(EnemySpell):
    """Learnable spell definition for Corona"""

    _index: int = 93
    _fp: int = 19
    _power: int = 88
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element = Element.FIRE
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class MeteorSwarm(EnemySpell):
    """Learnable spell definition for MeteorSwarm"""

    _index: int = 94
    _fp: int = 20
    _power: int = 100
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class KnockOut(EnemySpell):
    """Learnable spell definition for KnockOut"""

    _index: int = 95
    _fp: int = 15
    _power: int = 1
    _hit_rate: int = 60
    instant_ko = True

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = True
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = True
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class WeirdMushroom(EnemySpell):
    """Learnable spell definition for WeirdMushroom"""

    _index: int = 96
    _power: int = 30
    _hit_rate: int = 100

    _check_stats: bool = False
    _ignore_defense: bool = True
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.HEAL
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = True
    _target_enemies: bool = False
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class BreakerBeam(EnemySpell):
    """Learnable spell definition for BreakerBeam"""

    _index: int = 97
    _fp: int = 15
    _power: int = 80
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class Shredder(EnemySpell):
    """Learnable spell definition for Shredder"""

    _index: int = 98
    _fp: int = 8
    _hit_rate: int = 100

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.NULLIFY
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = [
        TempStatBuff.MAGIC_ATTACK,
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_DEFENSE,
        TempStatBuff.DEFENSE,
    ]
    _inflict: InflictFunction
    _hide_num: bool = True


class Sledge(EnemySpell):
    """Learnable spell definition for Sledge"""

    _index: int = 99
    _fp: int = 6
    _power: int = 50
    _hit_rate: int = 99

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class SwordRain(EnemySpell):
    """Learnable spell definition for SwordRain"""

    _index: int = 100
    _fp: int = 8
    _power: int = 80
    _hit_rate: int = 99

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class SpearRain(EnemySpell):
    """Learnable spell definition for SpearRain"""

    _index: int = 101
    _fp: int = 5
    _power: int = 60
    _hit_rate: int = 99

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class ArrowRain(EnemySpell):
    """Learnable spell definition for ArrowRain"""

    _index: int = 102
    _fp: int = 2
    _power: int = 40
    _hit_rate: int = 99

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class BigBang(EnemySpell):
    """Learnable spell definition for BigBang"""

    _index: int = 103
    _power: int = 100
    _hit_rate: int = 100

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class ChestScrow(EnemySpell):
    """Learnable spell definition for ChestScrow"""

    _index: int = 104
    _power: int = 10
    _hit_rate: int = 85

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.SCARECROW]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class ChestFear(EnemySpell):
    """Learnable spell definition for ChestFear"""

    _index: int = 105
    _power: int = 0
    _hit_rate: int = 82

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.FEAR]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = True


class ChestMute(EnemySpell):
    """Learnable spell definition for ChestMute"""

    _index: int = 106
    _power: int = 0
    _hit_rate: int = 85

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.MUTE]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = True


class ChestPoison(EnemySpell):
    """Learnable spell definition for ChestPoison"""

    _index: int = 107
    _power: int = 0
    _hit_rate: int = 85

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType = EffectType.INFLICT
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = [Status.POISON]
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = True


class ChainSaw(EnemySpell):
    """Learnable spell definition for ChainSaw"""

    _index: int = 108
    _power: int = 50
    _hit_rate: int = 90

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _quad9s: bool = False
    _target_others: bool = False
    _target_enemies: bool = True
    _target_party: bool = True
    _target_wounded: bool = False
    _target_one_party: bool = True
    _target_not_self: bool = False
    _element: Element
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []
    _inflict: InflictFunction
    _hide_num: bool = False


class SpellDoNothing(EnemySpell):
    """Learnable spell definition for SpellDoNothing"""

    _index: int = 251
    _power: int = 0
    _hit_rate: int = 100


# BigBang is not in any of these tables. It's just a bad idea.
SingleTargets = [
    Drain,
    LightningOrb,
    Flame,
    Bolt,
    Crystal,
    FlameStone,
    MegaDrain,
    WillyWisp,
    DiamondSaw,
    Electroshock,
    Blast,
    Storm,
    IceRock,
    DarkStar,
]
Heals = [Recover, MegaRecover, WeirdMushroom]
MultiTargets = [
    FlameWall,
    StaticE,
    SandStorm,
    Blizzard,
    DrainBeam,
    MeteorBlast,
    LightBeam,
    WaterBlast,
    Solidify,
    PetalBlast,
    AuroraFlash,
    Boulder,
    Corona,
    MeteorSwarm,
    KnockOut,
    Shredder,
    Sledge,
    SwordRain,
    SpearRain,
    ArrowRain,
    ChestScrow,
    ChestFear,
    ChestMute,
    ChestPoison,
    ChainSaw,
]
DoNothing = [SpellDoNothing]
Run = [Escape]

SpellsToTargets = {
    Drain.index: SingleTargets,
    LightningOrb.index: SingleTargets,
    Flame.index: SingleTargets,
    Bolt.index: SingleTargets,
    Crystal.index: SingleTargets,
    FlameStone.index: SingleTargets,
    MegaDrain.index: SingleTargets,
    WillyWisp.index: SingleTargets,
    DiamondSaw.index: SingleTargets,
    Electroshock.index: SingleTargets,
    Blast.index: SingleTargets,
    Storm.index: SingleTargets,
    IceRock.index: SingleTargets,
    DarkStar.index: SingleTargets,
    Recover.index: Heals,
    MegaRecover.index: Heals,
    WeirdMushroom.index: Heals,
    FlameWall.index: MultiTargets,
    StaticE.index: MultiTargets,
    SandStorm.index: MultiTargets,
    Blizzard.index: MultiTargets,
    DrainBeam.index: MultiTargets,
    MeteorBlast.index: MultiTargets,
    LightBeam.index: MultiTargets,
    WaterBlast.index: MultiTargets,
    Solidify.index: MultiTargets,
    PetalBlast.index: MultiTargets,
    AuroraFlash.index: MultiTargets,
    Boulder.index: MultiTargets,
    Corona.index: MultiTargets,
    MeteorSwarm.index: MultiTargets,
    KnockOut.index: MultiTargets,
    Shredder.index: MultiTargets,
    Sledge.index: MultiTargets,
    SwordRain.index: MultiTargets,
    SpearRain.index: MultiTargets,
    ArrowRain.index: MultiTargets,
    ChestScrow.index: MultiTargets,
    ChestFear.index: MultiTargets,
    ChestMute.index: MultiTargets,
    ChestPoison.index: MultiTargets,
    ChainSaw.index: MultiTargets,
    # These can really only be done by their specific casters
    BreakerBeam.index: [BreakerBeam] + MultiTargets,
    BigBang.index: [BigBang] + MultiTargets,
    SpellDoNothing.index: DoNothing,
    Escape.index: Run,
}
