import os

def create_levels54_keymap():
    # Miryoku mapping for a generic 3x5+3 layout (Colemak Mod-DH)
    # The layout we extracted from miryoku_layer_alternatives.h
    layers = {
        "Base": [
            "&kp Q",             "&kp W",             "&kp E",             "&kp R",             "&kp T",             "&kp Y",             "&kp U",             "&kp I",             "&kp O",             "&kp P",
            "&mt LGUI A",        "&mt LALT S",        "&mt LCTRL D",       "&mt LSHFT F",       "&kp G",             "&kp H",             "&mt LSHFT J",       "&mt LCTRL K",       "&mt LALT L",        "&mt LGUI SQT",
            "&lt 6 Z",           "&mt RALT X",        "&kp C",             "&kp V",             "&kp B",             "&kp N",             "&kp M",             "&kp COMMA",         "&mt RALT DOT",      "&lt 6 SLASH",
            "&none",             "&none",             "&lt 5 ESC",         "&lt 1 SPACE",       "&lt 4 TAB",         "&lt 3 RET",         "&lt 2 BSPC",        "&lt 7 DEL",         "&none",             "&none"
        ],
        "Nav": [
            "&bootloader",       "&none",             "&none",             "&to 0",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",
            "&kp LGUI",          "&kp LALT",          "&kp LCTRL",         "&kp LSHFT",         "&none",             "&caps_word",        "&kp LEFT",          "&kp DOWN",          "&kp UP",            "&kp RIGHT",
            "&none",             "&kp RALT",          "&to 2",             "&to 1",             "&none",             "&kp INS",           "&kp HOME",          "&kp PG_DN",         "&kp PG_UP",         "&kp END",
            "&none",             "&none",             "&none",             "&none",             "&none",             "&kp RET",           "&kp BSPC",          "&kp DEL",           "&none",             "&none"
        ],
        "Num": [
            "&kp LBKT",          "&kp N7",            "&kp N8",            "&kp N9",            "&kp RBKT",          "&none",             "&to 0",             "&none",             "&none",             "&bootloader",
            "&kp SEMI",          "&kp N4",            "&kp N5",            "&kp N6",            "&kp EQUAL",         "&none",             "&kp LSHFT",         "&kp LCTRL",         "&kp LALT",          "&kp LGUI",
            "&kp GRAVE",         "&kp N1",            "&kp N2",            "&kp N3",            "&kp BSLH",          "&none",             "&to 2",             "&to 1",             "&kp RALT",          "&none",
            "&none",             "&none",             "&kp DOT",           "&kp N0",            "&kp MINUS",         "&none",             "&none",             "&none",             "&none",             "&none"
        ],
        "Sym": [
            "&kp LBRC",          "&kp AMPS",          "&kp ASTRK",         "&kp LPAR",          "&kp RBRC",          "&none",             "&to 0",             "&none",             "&none",             "&bootloader",
            "&kp COLON",         "&kp DLLR",          "&kp PRCNT",         "&kp CARET",         "&kp PLUS",          "&none",             "&kp LSHFT",         "&kp LCTRL",         "&kp LALT",          "&kp LGUI",
            "&kp TILDE",         "&kp EXCL",          "&kp AT",            "&kp HASH",          "&kp PIPE",          "&none",             "&to 3",             "&to 4",             "&kp RALT",          "&none",
            "&none",             "&none",             "&kp LPAR",          "&kp RPAR",          "&kp UNDER",         "&none",             "&none",             "&none",             "&none",             "&none"
        ],
        "Mouse": [
            "&bootloader",       "&none",             "&none",             "&to 0",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",
            "&kp LGUI",          "&kp LALT",          "&kp LCTRL",         "&kp LSHFT",         "&none",             "&none",             "&none",             "&none",             "&none",             "&none",
            "&none",             "&kp RALT",          "&to 3",             "&to 4",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",
            "&none",             "&none",             "&none",             "&none",             "&none",             "&mkp RCLK",         "&mkp LCLK",         "&mkp MCLK",         "&none",             "&none"
        ],
        "Media": [
            "&bootloader",       "&none",             "&none",             "&to 0",             "&none",             "&rgb_ug RGB_TOG",   "&rgb_ug RGB_EFF",   "&rgb_ug RGB_HUI",   "&rgb_ug RGB_SAI",   "&rgb_ug RGB_BRI",
            "&kp LGUI",          "&kp LALT",          "&kp LCTRL",         "&kp LSHFT",         "&none",             "&ext_power EP_TOG", "&kp C_PREV",        "&kp C_VOL_DN",      "&kp C_VOL_UP",      "&kp C_NEXT",
            "&none",             "&kp RALT",          "&to 7",             "&to 5",             "&none",             "&out OUT_TOG",      "&bt BT_SEL 0",      "&bt BT_SEL 1",      "&bt BT_SEL 2",      "&bt BT_SEL 3",
            "&none",             "&none",             "&none",             "&none",             "&none",             "&kp C_STOP",        "&kp C_PP",          "&kp C_MUTE",        "&none",             "&none"
        ],
        "Button": [
            "&none",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",
            "&kp LGUI",          "&kp LALT",          "&kp LCTRL",         "&kp LSHFT",         "&none",             "&none",             "&kp LSHFT",         "&kp LCTRL",         "&kp LALT",          "&kp LGUI",
            "&none",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",             "&none",
            "&none",             "&none",             "&mkp MCLK",         "&mkp LCLK",         "&mkp RCLK",         "&mkp RCLK",         "&mkp LCLK",         "&mkp MCLK",         "&none",             "&none"
        ],
        "Fun": [
            "&kp F12",           "&kp F7",            "&kp F8",            "&kp F9",            "&kp PSCRN",         "&none",             "&to 0",             "&none",             "&none",             "&bootloader",
            "&kp F11",           "&kp F4",            "&kp F5",            "&kp F6",            "&kp SLCK",          "&none",             "&kp LSHFT",         "&kp LCTRL",         "&kp LALT",          "&kp LGUI",
            "&kp F10",           "&kp F1",            "&kp F2",            "&kp F3",            "&kp PAUSE_BREAK",   "&none",             "&to 7",             "&to 5",             "&kp RALT",          "&none",
            "&none",             "&none",             "&kp K_APP",         "&kp SPACE",         "&kp TAB",           "&none",             "&none",             "&none",             "&none",             "&none"
        ]
    }

    # Physical keys numbering for levels54 (54 keys total)
    # The current mapping in levels54 has 6 columns x 4 rows + 3 thumb keys per split
    # For a total of 12 + 12 + 12 + 12 + 6 = 54 keys
    # Example mapping: 12 keys per row (6 left, 6 right)
    
    # Let's map the 40 items in Miryoku to the 54 items in levels54.
    # Miryoku mapping array:
    # 00 01 02 03 04    05 06 07 08 09
    # 10 11 12 13 14    15 16 17 18 19
    # 20 21 22 23 24    25 26 27 28 29
    # 30 31 32 33 34    35 36 37 38 39
    
    # levels54 mapping array (12 keys per row x 4 rows + 6 thumb keys = 54):
    # 00 01 02 03 04 05      06 07 08 09 10 11 (Numbers row)
    # 12 13 14 15 16 17      18 19 20 21 22 23 (Top row)
    # 24 25 26 27 28 29      30 31 32 33 34 35 (Middle row)
    # 36 37 38 39 40 41      42 43 44 45 46 47 (Bottom row)
    #          48 49 50      51 52 53          (Thumb row)
    
    keymap_str = """#include <behaviors.dtsi>
#include <dt-bindings/zmk/bt.h>
#include <dt-bindings/zmk/keys.h>
#include <dt-bindings/zmk/pointing.h>
#include <dt-bindings/zmk/rgb.h>
#include <dt-bindings/zmk/ext_power.h>
#include <dt-bindings/zmk/outputs.h>

/ {
    keymap {
        compatible = "zmk,keymap";
"""

    # Corne mapping means the outermost columns (pinky) are &none, and the top row is &none.
    # We want the 3x5+3 to sit in the same relative position on levels54 as it does on Corne.
    # In our current script, we used columns 1-5 and 6-10 (0-indexed).
    #
    # Let's adjust the mapping to place the 3x5 blocks.
    # We will use columns 1, 2, 3, 4, 5 (for left half) and 6, 7, 8, 9, 10 (for right half).
    # Wait, our current mapping already leaves the outermost columns (0 and 11) as &none! 
    # Current: [13-17] (left) and [18-22] (right)
    # 
    # Let's verify levels54 physical layout:
    # 00 01 02 03 04 05      06 07 08 09 10 11 (Numbers row) - Top
    # 12 13 14 15 16 17      18 19 20 21 22 23 (Top row)
    # 24 25 26 27 28 29      30 31 32 33 34 35 (Middle row)
    # 36 37 38 39 40 41      42 43 44 45 46 47 (Bottom row)
    #          48 49 50      51 52 53          (Thumb row)
    #
    # For a Corne (3x6+3), the layout uses 3 rows of 6 columns per half. 
    # Miryoku maps its 3x5 layout to the *inner* 5 columns of the Corne!
    # That means the *outermost* columns of the Corne (the ones furthest from the center) are populated, while the *innermost* columns (closest to center) are populated.
    # Let's look at `miryoku_zmk/miryoku/mapping/42/corne.h` again:
    # XXX  K00  K01  K02  K03  K04       K05  K06  K07  K08  K09  XXX
    # XXX is the OUTERMOST column (pinky). This means Miryoku on Corne leaves the far LEFT and far RIGHT columns empty.
    # BUT levels54 is 4x6+3.
    # Our current generated map:
    # &none        &none        &none        &none        &none        &none        &none        &none        &none        &none        &none        &none       
    # &none        &kp Q        &kp W        &kp E        &kp R        &kp T        &kp Y        &kp U        &kp I        &kp O        &kp P        &none       
    # &none        &mt A        &mt S        &mt D        &mt F        &kp G        &kp H        &mt J        &mt K        &mt L        &mt SQT      &none       
    # &none        &lt Z        &mt X        &kp C        &kp V        &kp B        &kp N        &kp M        &kp COMMA    &mt DOT      &lt SLASH    &none       
    #                                     &lt DEL      &lt BSPC     &lt RET      &lt TAB      &lt SPACE    &lt ESC   
    # This IS EXACTLY how Miryoku maps to Corne! (The outer columns 12, 23, 24, 35, 36, 47 are empty).
    # Wait, the user might refer to the fact that standard Corne has the outermost pinky column populated, and leaves the INNER index column empty instead?
    # Let's check `miryoku_zmk_temp/miryoku/mapping/42/corne.h` again.
    # It explicitly defines:
    # XXX  K00  K01  K02  K03  K04       K05  K06  K07  K08  K09  XXX
    # This leaves the outer pinky columns (XXX) empty.
    
    # Wait, some users prefer mapping the 3x5 so that the outer pinkies ARE used, and the inner index columns are left empty.
    # Or, the user's issue might be the thumb keys! 
    # Corne has 3 thumb keys. levels54 has 3 thumb keys.
    # Or maybe the QWERTY layout generated previously using `MIRYOKU_ALTERNATIVES_BASE_QWERTY` was slightly different than the standard "corne" mapping.
    
    # Let me actually map it to the exact "outer pinky used" mapping if that's what they mean.
    # If standard Corne is 6 columns: [0, 1, 2, 3, 4, 5], inner indexing would skip 5. 
    # Let's shift it so the outer columns ARE used, and inner columns (5 and 6) are skipped.
    
    for layer_name, layer_keys in layers.items():
        levels54_keys = ["&none"] * 54
        
        # Row 1 (Top letter row) -> maps to keys 12-16, 19-23
        # Leaving the inner columns (17, 18) empty.
        levels54_keys[12] = layer_keys[0]; levels54_keys[13] = layer_keys[1]; levels54_keys[14] = layer_keys[2]; levels54_keys[15] = layer_keys[3]; levels54_keys[16] = layer_keys[4]
        levels54_keys[19] = layer_keys[5]; levels54_keys[20] = layer_keys[6]; levels54_keys[21] = layer_keys[7]; levels54_keys[22] = layer_keys[8]; levels54_keys[23] = layer_keys[9]
        
        # Row 2 (Home row) -> maps to keys 24-28, 31-35
        # Leaving the inner columns (29, 30) empty.
        levels54_keys[24] = layer_keys[10]; levels54_keys[25] = layer_keys[11]; levels54_keys[26] = layer_keys[12]; levels54_keys[27] = layer_keys[13]; levels54_keys[28] = layer_keys[14]
        levels54_keys[31] = layer_keys[15]; levels54_keys[32] = layer_keys[16]; levels54_keys[33] = layer_keys[17]; levels54_keys[34] = layer_keys[18]; levels54_keys[35] = layer_keys[19]
        
        # Row 3 (Bottom letter row) -> maps to keys 36-40, 43-47
        # Leaving the inner columns (41, 42) empty.
        levels54_keys[36] = layer_keys[20]; levels54_keys[37] = layer_keys[21]; levels54_keys[38] = layer_keys[22]; levels54_keys[39] = layer_keys[23]; levels54_keys[40] = layer_keys[24]
        levels54_keys[43] = layer_keys[25]; levels54_keys[44] = layer_keys[26]; levels54_keys[45] = layer_keys[27]; levels54_keys[46] = layer_keys[28]; levels54_keys[47] = layer_keys[29]
        
        # Thumb row -> maps to keys 48-50, 51-53
        # In Miryoku thumb keys are K32, K33, K34 and K35, K36, K37
        levels54_keys[48] = layer_keys[32]; levels54_keys[49] = layer_keys[33];  levels54_keys[50] = layer_keys[34]
        levels54_keys[51] = layer_keys[35]; levels54_keys[52] = layer_keys[36]; levels54_keys[53] = layer_keys[37]

        # Formatting physical layout string
        row1 = " ".join(f"{k:12}" for k in levels54_keys[0:12])
        row2 = " ".join(f"{k:12}" for k in levels54_keys[12:24])
        row3 = " ".join(f"{k:12}" for k in levels54_keys[24:36])
        row4 = " ".join(f"{k:12}" for k in levels54_keys[36:48])
        row5 = "                                    " + " ".join(f"{k:12}" for k in levels54_keys[48:54])

        keymap_str += f"""
        {layer_name.lower()}_layer {{
            display-name = "{layer_name}";
            bindings = <
{row1}
{row2}
{row3}
{row4}
{row5}
            >;
        }};
"""
    keymap_str += """    };
};
"""

    keymap_path = r"G:\My Drive\Projects\Levels54\source\hectorj84\gggw-levels54\config\levels54.keymap"
    with open(keymap_path, "w") as f:
        f.write(keymap_str)
        
    print(f"Generated levels54.keymap successfully!")

if __name__ == "__main__":
    create_levels54_keymap()
