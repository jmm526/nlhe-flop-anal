from enum import Enum

class FlopTags(Enum):
    # High Cards
    _A_HIGH = "A_HIGH"                              # Flop has ace high
    _K_HIGH = "K_HIGH"                              # Flop has king high
    _Q_HIGH = "Q_HIGH"                              # Flop has queen high
    _J_HIGH = "J_HIGH"                              # Flop has jack high
    _T_HIGH = "T_HIGH"                              # Flop has ten high
    _9_HIGH = "9_HIGH"                              # Flop has nine high
    _8_HIGH = "8_HIGH"                              # Flop has eight high
    _7_HIGH = "7_HIGH"                              # Flop has seven high
    _6_HIGH = "6_HIGH"                              # Flop has six high
    _5_HIGH = "5_HIGH"                              # Flop has five high
    _4_HIGH = "4_HIGH"                              # Flop has four high
    _3_HIGH = "3_HIGH"                              # Flop has three high
    _2_HIGH = "2_HIGH"                              # Flop has two high
    
    # Paired Flops
    # PAIRED Calculated Boolean
    T_PAIRED = "T_PAIRED"                           # Flop has a paired top card
    B_PAIRED = "B_PAIRED"                           # Flop has a paired bottom card
    HC_PAIRED = "HC_PAIRED"                         # Flop has a paired high card
    MC_PAIRED = "MC_PAIRED"                         # Flop has a paired middle card
    LC_PAIRED = "LC_PAIRED"                         # Flop has a paired low card

    # Paired Calculated Fields
    UNPAIRED = "UNPAIRED"                           # Flop has no paired cards
    PAIRED = "PAIRED"                               # Flop has exactly one pair
    TRIPS = "TRIPS"                                 # Flop has trips

    # Card Distribution
    _3_0_0_CD = "3_0_0_CD"                          # Flop has 3 low cards, 0 middle cards, 0 high cards
    _2_1_0_CD = "2_1_0_CD"                          # Flop has 2 low cards, 1 middle card, 0 high cards
    _2_0_1_CD = "2_0_1_CD"                          # Flop has 2 low cards, 0 middle cards, 1 high card
    _1_2_0_CD = "1_2_0_CD"                          # Flop has 1 low card, 2 middle cards, 0 high cards
    _1_1_1_CD = "1_1_1_CD"                          # Flop has 1 low card, 1 middle card, 1 high card
    _1_0_2_CD = "1_0_2_CD"                          # Flop has 1 low card, 0 middle cards, 2 high cards
    _0_3_0_CD = "0_3_0_CD"                          # Flop has 0 low cards, 3 middle cards, 0 high cards
    _0_2_1_CD = "0_2_1_CD"                          # Flop has 0 low cards, 2 middle cards, 1 high card
    _0_1_2_CD = "0_1_2_CD"                          # Flop has 0 low cards, 1 middle card, 2 high cards
    _0_0_3_CD = "0_0_3_CD"                          # Flop has 0 low cards, 0 middle cards, 3 high cards

    # 2 connected cards
    _2_GAPPER_H_2C = "2_GAPPER_H_2C"                # Flop has 2 gapper connected with high card
    _2_GAPPER_L_2C = "2_GAPPER_L_2C"                # Flop has 2 gapper connected with low card
    _1_GAPPER_H_2C = "1_GAPPER_H_2C"                # Flop has 1 gapper connected with high card
    _1_GAPPER_L_2C = "1_GAPPER_L_2C"                # Flop has 1 gapper connected with low card
    H_2C = "H_2C"                                   # Flop has 2 connected cards with high card
    L_2C = "L_2C"                                   # Flop has 2 connected cards with low card

    # 3 connected cards (straight possible)
    # STRAIGHT_POSSIBLE Calculated Boolean
    _3_CONNECTED_3C = "3_CONNECTED_3C"              # Flop has 3 connected cards (ex. 789)
    _1_GAPPER_H_3C = "1_GAPPER_H_3C"                # Flop has 1 gapper connected with high card (ex. 679)
    _1_GAPPER_L_3C = "1_GAPPER_L_3C"                # Flop has 1 gapper connected with low card (ex. 578)
    _DBL_1_GAPPER_3C = "DBL_1_GAPPER_3C"            # Flop has double 1 gapper connected with high card (ex. 579)
    _2_GAPPER_H_3C = "2_GAPPER_H_3C"                # Flop has 2 gapper connected with high card (ex. 67T)
    _2_GAPPER_L_3C = "2_GAPPER_L_3C"                # Flop has 2 gapper connected with low card (ex. 69T)

    # Suits
    RAINBOW_S = "rainbow"                         # Flop is rainbow
    TWO_TONE_S = "two-tone"                       # Flop is two tone
    MONO_TONE_S = "mono-tone"                     # Flop is mono tone

    