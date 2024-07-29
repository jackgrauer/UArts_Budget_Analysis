import pandas as pd

# Creating a dataframe from the provided budget data


# All these in thousands of dollars

FY2019BUDGET = {
    "Category": [
        "Gross tuition and fees - for credit", "Scholarships -- unfunded", "Net tuition and fees - for credit",
        "Continuing Studies & Pre-Collegiate", "Scholarships -- unfunded", "Net tuition and fees - Cont. Studies/Pre-Collegiate",
        "State grants", "Annual fund", "Federal grants", "Endowment income", "Other investment income", "Auxiliary enterprises",
        "Dining Services", "Other revenue", "Total Operating Revenue", "Instruction - for credit",
        "Instruction - Continuing Studies & Pre-Collegiate", "Academic support", "Enrollment management",
        "Student services", "Institutional support", "Auxiliary enterprises", "Dining Services",
        "Operation and maintenance of plant", "Interest expense", "Other", "Total Operating Expenses",
        "Net Operating Margin", "Principal payments", "Capital spending",
        "Total Other Cash Expenditures", "Net Cash Provided By (Used In) Operations"
    ],
    "FY 2017 Actual": [
        73431, -31443, 41988, 2002, -179, 1823, 180, 923, 290, 2126, 196, 7137, 3156, 626, 58445,
        19445, 2093, 3158, 3009, 2368, 13638, 1035, 3026, 6699, 2103, None, 56574, 1871, 2050, 2253, 4303, -2432
    ],
    "FY 2018 Budget": [
        70937, -31035, 39902, 2355, -182, 2173, 92, 725, 200, 2072, 360, 7603, 3580, 594, 57301,
        18994, 2235, 3238, 3725, 2559, 12157, 1075, 2883, 6303, 2017, None, 55186, 2115, 2115, None, 2115, 0
    ],
    "FY 2018 Projection": [
        73665, -32889, 40776, 2275, -186, 2089, 181, 725, 246, 2072, 1063, 7603, 3479, 594, 58828,
        18853, 2151, 3350, 3284, 2539, 12135, 1177, 2657, 6719, 2264, None, 55129, 3699, 1206, 1500, 2706, 993
    ],
    "FY 2019 Budget Request": [
        76648, -34863, 41785, 2288, -234, 2054, 90, 725, 195, 2055, 363, 7986, 3453, 500, 59205,
        18832, 2146, 3366, 3753, 2865, 13684, 1123, 3024, 6771, 2565, None, 58131, 1074, 887, None, 887, 188
    ]
}

FY2020BUDGET = {
    "Category": [
        "Gross tuition and fees - for credit", "Scholarships -- unfunded", "Net tuition and fees - for credit",
        "Continuing Studies & Pre-Collegiate", "Scholarships -- unfunded", "Net tuition and fees - Cont. Studies/Pre-Collegiate",
        "State grants", "Annual fund", "Federal grants", "Endowment income", "Other investment income", "Auxiliary enterprises",
        "Dining Services", "Other revenue", "Total Operating Revenue", "Instruction - for credit",
        "Instruction - Continuing Studies & Pre-Collegiate", "Academic support", "Enrollment management",
        "Student services", "Institutional support", "Auxiliary enterprises", "Dining Services",
        "Operation and maintenance of plant", "Interest expense", "Other", "Total Operating Expenses",
        "Net Operating Margin", "Principal payments", "Capital spending",
        "Total Other Cash Expenditures", "Net Cash Provided By (Used In) Operations"
    ],
    "FY 2017 Actual": [
        73431, -31443, 41988, 2002, -179, 1823, 180, 923, 290, 2126, 196, 7137, 3156, 626, 58445,
        19445, 2093, 3158, 3009, 2368, 13638, 1035, 3026, 6699, 2103, None, 56574, 1871, 2050, 2253, 4303, -2432
    ],
    "FY 2018 Actual": [
        75958, -33789, 42169, 1943, -190, 1753, 161, 729, 249, 2131, 903, 7666, 3453, 538, 59711,
        18905, 1930, 3269, 3014, 3246, 13268, 2204, 2485, 5062, 2246, None, 55629, 4143, 1206, 2979, 4185, -423
    ],
    "FY 2019 Actual": [
        80633, -36853, 43780, 2281, -310, 1971, 168, 633, 237, 2161, 378, 7677, 3533, 563, 61101,
        19021, 2003, 2806, 3180, 3833, 13655, 2355, 2888, 5013, 2565, None, 57319, 3782, 887, 14562, 4303, -10652
    ],
    "FY 2020 Request": [
        80175, -35790, 44385, 2267, -304, 1963, 161, 765, 209, 2234, 205, 7896, 3621, 573, 62012,
        19312, 2034, 2849, 3229, 3892, 13864, 2391, 2957, 5090, 2511, None, 58128, 3884, 1472, 2300, 2300, 112
    ]
}

FY2021BUDGET = {
    "Category": [
        "Gross tuition and fees - for credit", "Scholarships -- unfunded", "Net tuition and fees - for credit",
        "Continuing Studies & Pre-Collegiate", "Scholarships -- unfunded", "Net tuition and fees - Cont. Studies/Pre-Collegiate",
        "State grants", "Annual fund", "Federal grants", "Endowment income", "Other investment income", "Auxiliary enterprises",
        "Dining Services", "Other revenue", "Total Operating Revenue", "Instruction - for credit",
        "Instruction - Continuing Studies & Pre-Collegiate", "Academic support", "Enrollment management",
        "Student services", "Institutional support", "Auxiliary enterprises", "Dining Services",
        "Operation and maintenance of plant", "Interest expense", "Other", "Total Operating Expenses",
        "Net Operating Margin", "Principal payments", "Capital spending",
        "Total Other Cash Expenditures", "Net Cash Provided By (Used In) Operations"
    ],
    "FY 2020 Actual": [
        81016, -38414, 42602, 2285, -323, 1962, 170, 405, 2061, 2205, 95, 6422, 2820, 464, 59206,
        17762, 2062, 2437, 3270, 2872, 13484, 1159, 2306, 6058, 2515, None, 53925, 5281, 1472, 1931, 3403, 1878
    ],
    "FY 2021 Budget Request": [
        65437, -31748, 33689, 1179, -167, 1012, 132, 425, 171, 3128, 79, 3210, 0, 200, 42045,
        12543, 1405, 2050, 2722, 2236, 10565, 319, 327, 5564, 2455, None, 40187, 1858, 1549, None, 1549, 309
    ]
}

FY2022BUDGET  = {
    "Category": [
        "Gross tuition and fees - for credit", "Scholarships -- unfunded", "Net tuition and fees - for credit",
        "Continuing Studies & Pre-Collegiate", "Scholarships -- unfunded", "Net tuition and fees - Cont. Studies/Pre-Collegiate",
        "State grants", "Annual fund", "Federal grants", "Endowment income", "Other investment income", "Auxiliary enterprises",
        "Dining Services", "Other revenue", "Total Operating Revenue", "Instruction - for credit",
        "Instruction - Continuing Studies & Pre-Collegiate", "Academic support", "Enrollment management",
        "Student services", "Institutional support", "Auxiliary enterprises", "Dining Services",
        "Operation and maintenance of plant", "Interest expense", "Other", "Total Operating Expenses",
        "Net Operating Margin", "Principal payments", "Capital spending",
        "Total Other Cash Expenditures", "Net Cash Provided By (Used In) Operations"
    ],
    "FY 2021 Actual": [
        67277, -33966, 33311, 1305, -48, 1257, 279, 1139, 2782, 3195, 2, 3371, 118, 353, 45808,
        13282, 1280, 1769, 2688, 2119, 11458, 410, 187, 5327, 2446, None, 40967, 4841, 1549, 665, 2214, 2626
    ],
    "FY 2022 Budget Request": [
        69803, -33103, 36700, 1150, -53, 1097, 170, 700, 2620, 2711, 3, 6603, 3288, 382, 54274,
        15391, 1523, 3301, 3693, 3343, 12545, 865, 2830, 6805, 2414, None, 52709, 1565, 1531, None, 1531, 34
    ]
}

FY2023BUDGET  = {
    "Category": [
        "Gross tuition and fees - for credit", "Scholarships -- unfunded", "Net tuition and fees - for credit",
        "Continuing Studies & Pre-Collegiate", "Scholarships -- unfunded", "Net tuition and fees - Cont. Studies/Pre-Collegiate",
        "State grants", "Annual fund", "Federal grants", "Endowment income", "Other investment income", "Auxiliary enterprises",
        "Dining Services", "Other revenue", "Total Operating Revenue", "Instruction - for credit",
        "Instruction - Continuing Studies & Pre-Collegiate", "Academic support", "Enrollment management",
        "Student services", "Institutional support", "Auxiliary enterprises", "Dining Services",
        "Operation and maintenance of plant", "Interest expense", "Total Operating Expenses",
        "Net Operating Margin", "Principal payments", "Capital spending",
        "Total Other Cash Expenditures", "Net Cash Provided By (Used In) Operations",
        "Portion of proceeds from non-recurring gain on sale of Pine Hall", "Net Income"
    ],
    "FY 2022 Actual": [
        70026, -34877, 35149, 1951, -47, 1904, 173, 541, 5032, 2436, None, 6714, 3237, 412, 55598,
        14966, 1216, 2138, 2791, 2906, 13029, 1138, 2887, 6150, 2414, 49635, 5963, 1265, 1422, 2687, 3276, None, 3276
    ],
    "FY 2023 Budget Request": [
        62984, -28150, 34834, 1848, -283, 1566, 175, 650, 230, 2900, None, 5901, 3446, 388, 50090,
        15422, 1747, 3131, 3713, 3234, 12639, 1075, 2366, 6977, 2349, 52651, -2561, 1593, None, 1593, -4154, 4154, 0
    ]
}

FY2024BUDGET = {
    "Category": [
        "Gross tuition and fees - for credit", "Scholarships - unfunded", "Net tuition and fees - for credit",
        "Continuing Studies & Pre-Collegiate", "Scholarships - unfunded", "Net tuition and fees - Cont. Studies & Pre-Collegiate",
        "State grants", "Unrestricted Contributions and Annual Funds", "Federal grants", "Endowment income", "Other investment income", "Auxiliary enterprises",
        "Dining Services", "Other revenue", "Total Operating Revenue", "Instruction - for credit",
        "Instruction - Continuing Studies & Pre-Collegiate", "Academic support", "Enrollment management",
        "Student services", "Institutional support", "Auxiliary enterprises", "Dining Services",
        "Operation and maintenance of plant", "Interest expense", "Total Operating Expenses",
        "Net Operating Margin", "Principal payments", "Capital spending",
        "Total Other Cash Expenditures", "Net Cash Provided by (Used in Operations)",
        "Proceeds from non-recurring gain on sale of Pine Hall", "Net Cash Provided by (Used in Operations) after proceeds on sale of Pine Hall"
    ],
    "FY 2023 Actual": [
        61463, -27450, 34013, 1745, -251, 1494, 171, 665, 94, 2593, 237, 5714, 2618, 411, 48010,
        15586, 1362, 3121, 3421, 3158, 13963, 1061, 2986, 6745, 2349, 53752, -5742, 1326, 1889, 3215, -8957, 7274, -1683
    ],
    "FY 2024 Budget Request": [
        61418, -26834, 34584, 1518, -328, 1190, 1172, 2700, 227, 4713, 124, 6305, 3239, 411, 54664,
        16074, 1407, 3382, 3698, 3234, 13605, 1053, 2511, 6973, 2084, 54021, 643, 1500, 1000, 2500, -1857, None, -1857
    ]
}

# Step 3: Create dataframes

FY2019BUDGET = pd.DataFrame(FY2019BUDGET)
FY2020BUDGET = pd.DataFrame(FY2020BUDGET)
FY2021BUDGET = pd.DataFrame(FY2021BUDGET)
FY2022BUDGET = pd.DataFrame(FY2022BUDGET)
FY2023BUDGET = pd.DataFrame(FY2023BUDGET)
FY2024BUDGET = pd.DataFrame(FY2024BUDGET)

# Consolidate all dataframes into one
consolidated_budget = pd.concat([
    FY2019BUDGET.set_index('Category').T,
    FY2020BUDGET.set_index('Category').T,
    FY2021BUDGET.set_index('Category').T,
    FY2022BUDGET.set_index('Category').T,
    FY2023BUDGET.set_index('Category').T,
    FY2024BUDGET.set_index('Category').T
], keys=['FY2019', 'FY2020', 'FY2021', 'FY2022', 'FY2023', 'FY2024'])

# Reset index to make the dataframe more readable
consolidated_budget = consolidated_budget.reset_index().rename(columns={'level_0': 'Fiscal Year', 'index': 'Data Type'})

# Display the consolidated budget dataframe
print(consolidated_budget)
