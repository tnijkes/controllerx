from const import Light, TypeActionsMapping
from core import LightController


class HueDimmerController(LightController):
    # Different states reported from the controller:
    # on-press, on-hold, on-hold-release, up-press, up-hold,
    # up-hold-release, down-press, down-hold, down-hold-release,
    # off-press, off-hold, off-hold-release

    def get_z2m_actions_mapping(self) -> TypeActionsMapping:
        return {
            "on-press": Light.ON,
            "on-hold": Light.HOLD_COLOR_UP,
            "on-hold-release": Light.RELEASE,
            "up-press": Light.CLICK_BRIGHTNESS_UP,
            "up-hold": Light.HOLD_BRIGHTNESS_UP,
            "up-hold-release": Light.RELEASE,
            "down-press": Light.CLICK_BRIGHTNESS_DOWN,
            "down-hold": Light.HOLD_BRIGHTNESS_DOWN,
            "down-hold-release": Light.RELEASE,
            "off-press": Light.OFF,
            "off-hold": Light.HOLD_COLOR_DOWN,
            "off-hold-release": Light.RELEASE,
        }

    def get_deconz_actions_mapping(self) -> TypeActionsMapping:
        return {
            1002: Light.ON,
            1001: Light.HOLD_COLOR_UP,
            1003: Light.RELEASE,
            2002: Light.CLICK_BRIGHTNESS_UP,
            2001: Light.HOLD_BRIGHTNESS_UP,
            2003: Light.RELEASE,
            3002: Light.CLICK_BRIGHTNESS_DOWN,
            3001: Light.HOLD_BRIGHTNESS_DOWN,
            3003: Light.RELEASE,
            4002: Light.OFF,
            4001: Light.HOLD_COLOR_DOWN,
            4003: Light.RELEASE,
        }


class Niko91004LightController(LightController):
    def get_deconz_actions_mapping(self) -> TypeActionsMapping:
        return {
            1000: Light.ON,  # button_1_press
            1001: Light.SYNC,  # button_1_hold
            # 1002: "",  # button_1_release
            # 1003: "",  # button_1_release_after_hold
            2000: Light.OFF,  # button_2_press
            2001: Light.SYNC,  # button_2_hold
            # 2002: "",  # button_2_release
            # 2003: "",  # button_2_release_after_hold
            3000: Light.ON_FULL_BRIGHTNESS,  # button_3_press
            3001: Light.HOLD_BRIGHTNESS_UP,  # button_3_hold
            # 3002: "",  # button_3_release
            3003: Light.RELEASE,  # button_3_release_after_hold
            4000: Light.ON_MIN_BRIGHTNESS,  # button_4_press
            4001: Light.HOLD_BRIGHTNESS_DOWN,  # button_4_hold
            # 4002: "",  # button_4_release
            4003: Light.RELEASE,  # button_4_release_after_hold
            5000: Light.ON_FULL_COLOR_TEMP,  # button_1_3_press
            5001: Light.HOLD_COLOR_UP,  # button_1_3_hold
            # 5002: "",  # button_1_3_release
            5003: Light.RELEASE,  # button_1_3_release_after_hold
            6000: Light.ON_MIN_COLOR_TEMP,  # button_2_4_press
            6001: Light.HOLD_COLOR_DOWN,  # button_2_4_hold
            # 6002: "",  # button_2_4_release
            6003: Light.RELEASE,  # button_2_4_release_after_hold
        }
