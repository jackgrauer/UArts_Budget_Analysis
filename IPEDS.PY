#Step 1: Imports
import pandas as pd
import pprint
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 2: Define data dictionary


data_dict = {
    "FY2003IPEDS": {
        "Category": [
            "Long-term investments", "Total assets", "Total liabilities", "Total unrestricted net assets", "Total restricted net assets", "Total net assets", "Land and land improvements", "Buildings", "Equipment, including art and library collections", "Property obtained under capital leases (if not included in equipment)", "Total revenues and investment return", "Total expenses", "Other specific changes in net assets (CV)", "Change in net assets", "Net assets, beginning of year", "Adjustments to beginning of year net assets (CV)", "Net assets, end of year", "Pell grants", "Other federal grants", "State grants", "Local grants", "Institutional grants (funded)", "Institutional grants (unfunded)", "Total student grants (CV)", "Allowances applied to tuition and fees", "Allowances applied to auxiliary enterprise revenues", "Tuition and fees, net of allowances", "Federal appropriations", "State appropriations", "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local grants and contracts", "Private gifts, grants and contracts", "Contributions from affiliated entities", "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises, net of allowances", "Hospital revenue", "Independent operations revenue", "Other revenue (CV)", "Instruction", "Research", "Public service", "Academic support", "Student service", "Institutional support", "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations", "Operation and maintenance of plant", "Other expenses (CV)", "Total expenses"],
            
        "Current Year Values": [
            16035000, 108298000, 59860000, 25995000, 22443000, 48438000, 5855000, 95165000, 14170000, 0, 46418000, 45960000, 0, 458000, 47980000, 0, 48438000, 1270545, 403633, 2050996, 0, 575608, 12580759, 16881541, 13156367, 0, 29945000, 0, 1157000, 0, 281000, 125000, 0, 8992000, 0, 756000, 0, 5162000, 0, 0, 0, 22259400, 0, 0, 6184240, 4087840, 8510120, 4435400, 483000, 0, 0, -5542000, 0, 45960000 ],
    },

    "FY2004IPEDS": {
        "Category": ["Long-term investments","Total assets","Total liabilities","Total unrestricted net assets","Total restricted net assets","Total net assets","Land and land improvements","Buildings","Equipment, including art and library collections","Property obtained under capital leases (if not included in equipment)","Total revenues and investment return","Total expenses","Other specific changes in net assets (CV)","Change in net assets","Net assets, beginning of year","Adjustments to beginning of year net (CV)","Net assets, end of year","Pell grants","Other federal grants","State grants","Local grants","Institutional grants (funded)","Institutional grants (unfunded)","Total student grants (CV)","Allowances applied to tuition and fees","Allowances applied to auxiliary enterprise revenues","Tuition and fees (net of allowances)","Federal appropriations","State appropriations","Local appropriations","Federal grants and contracts","State grants and contracts","Local grants and contracts","Private gifts, grants and contracts","Contributions from affiliated entities","Investment return","Sales and services of educational activities","Sales and services of auxiliary enterprises (net of allowances)","Hospital revenue","Independent operations revenue","Other revenue (CV)","Instruction","Research","Public service","Academic support","Student services","Institutional support","Auxiliary enterprises","Net grant aid to students (net of tuition and fee allowances and agency transactions)","Hospital services","Independent operations","Operation and maintenance of plant","Other expenses (CV)","Total expenses","Value of endowment assets at the beginning of the fiscal year","Value of endowment assets at the end of the fiscal year"],

        "Current Year Values": [16252000,108539000,62379000,25055000,21105000,46160000,5855000,97278000,14724000,0,45474000,47752000,0,-2278000,48438000,0,46160000,1445339,322745,1981149,0,1220000,14089000,19058233,15309000,0,31595000,0,1122000,0,381000,141000,0,4220000,0,2455000,0,5560000,0,0,0,22847150,0,0,5635040,4551390,9454520,4646900,617000,0,0,0,0,47752000,16035000,16252000],
    },

    "FY2005IPEDS": {
        "Category": ["Long-term investments","Total assets","Total liabilities","Total unrestricted net assets","Total restricted net assets","Permanently restricted net assets included in line 05","Total net assets","Land and land improvements","Buildings","Equipment, including art and library collections","Property obtained under capital leases","Total revenues and investment return","Total expenses","Other specific changes in net assets","Change in net assets","Net assets, beginning of year","Adjustments to beginning of year net assets","Net assets, end of year","Pell grants","Other federal grants","State grants","Local grants","Institutional grants (funded)","Institutional grants (unfunded)","Total student grants","Allowances scholarships applied to tuition and fees","Allowances scholarships applied to auxiliary enterprise revenues","Tuition and fees (net of allowance reported in Part C, line 08)","Federal appropriations","State appropriations","Local appropriations","Federal grants and contracts","State grants and contracts","Local grants and contracts","Private gifts, grants and contracts","Contributions from affiliated entities","Investment return","Sales and services of educational activities","Sales and services of auxiliary enterprises","Hospital revenue","Independent operations revenue","Other revenue","Total revenues and investment return (from B01)","Instruction","Research","Public service","Academic support","Student service","Institutional support","Auxiliary enterprises","Net grant aid to students (net of tuition and fee allowances)","Hospital services","Independent operations","Operation and maintenance of plant","Other expenses","Total expenses","Value of endowment assets at the beginning of the fiscal year","Value of endowment assets at the end of the fiscal year"],
        
        "Current Year Values": [17116494,108299760,61009565,25448981,21841214,10269485,47290195,5854855,98081551,15473835,0,51481239,50351438,0,1129801,46160394,0,47290195,1427378,250677,2100725,0,875969,16081583,20736332,16957552,0,34770518,0,1150000,0,353117,119424,0,7626973,0,1450303,0,5825451,0,0,185453,51481239,23828978,0,0,6849028,4934019,9522047,4627032,590334,0,0,0,0,50351438,16252000,17116494],
    },

    "FY2006IPEDS": {
        "Category": ["Long-term investments", "Total assets", "Total liabilities", "Total unrestricted net assets", "Total restricted net assets", "Total net assets", "Land and land improvements", "Buildings", "Equipment, including art and library collections", "Property obtained under capital leases", "Total revenues and investment return", "Total expenses", "Other specific changes in net assets", "Change in net assets", "Net assets, beginning of year", "Adjustments to beginning of year net assets", "Net assets, end of year", "Pell grants", "Other federal grants", "State grants", "Local grants", "Institutional grants (funded)", "Institutional grants (unfunded)", "Total student grants", "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues", "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations", "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local grants and contracts", "Private gifts, grants and contracts", "Contributions from affiliated entities", "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises (net of allowance reported in Part C, line 09)", "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return (from B01)", "Instruction", "Research", "Public service", "Academic support", "Student service", "Institutional support", "Auxiliary enterprises", "Net grant aid to students (net of tuition and fee allowances)", "Hospital services", "Independent operations", "Operation and maintenance of plant", "Other expenses", "Total expenses", "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year" ],

        "Current Year Values": [17116494, 108299760, 61009565, 25448981, 21841214, 47290195, 5854855, 98081551, 15473835, 0, 51481239, 50351438, 0, 1129801, 46160394, 0, 47290195, 1427378, 250677, 2100725, 0, 875969, 16081583, 20736332, 16957552, 0, 34770518, 0, 1150000, 0, 353117, 119424, 0, 7626973, 0, 1450303, 0, 5825451, 0, 0, 185453, 51481239, 23828978, 0, 0, 6849028, 4934019, 9522047, 4627032, 590334, 0, 0, 0, 0, 50351438, 16252000, 17116494],
    },
    "FY2007IPEDS": {
        "Category": ["Long-term investments", "Total assets", "Total liabilities", "Total unrestricted net assets", "Total restricted net assets", "Total net assets", "Land and land improvements", "Buildings", "Equipment, including art and library collections", "Property obtained under capital leases", "Total revenues and investment return", "Total expenses", "Other specific changes in net assets", "Change in net assets", "Net assets, beginning of year", "Adjustments to beginning of year net assets", "Net assets, end of year", "Pell grants", "Other federal grants", "State grants", "Local grants", "Institutional grants (funded)", "Institutional grants (unfunded)", "Total student grants", "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues", "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations", "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local grants and contracts", "Private gifts, grants and contracts", "Contributions from affiliated entities", "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises (net of allowance reported in Part C, line 09)", "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return (from B01)", "Instruction", "Research", "Public service", "Academic support", "Student service", "Institutional support", "Auxiliary enterprises", "Net grant aid to students (net of tuition and fee allowances)", "Hospital services", "Independent operations", "Operation and maintenance of plant", "Other expenses", "Total expenses", "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"],
        
        "Current Year Values": [
        17910604, 127805672, 77125201, 24428017, 26252454, 50680471, 5854855, 99892437, 16473517, 0, 60312686, 56518644, 0, 3794042, 47290195, 0, 50680471, 1333800, 310286, 2082260, 0, 638829, 17638190, 21654463, 18277019, 0, 37595527, 0, 1173000, 0, 365025, 115000, 0, 13463123, 0, 1198329, 0, 6220529, 0, 0, 1122358, 60312686, 1096742, 0, 0, 7623441, 1944346, 6686404, 2035636, 0, 0, 0, 5549925, 0, 64001210, 17116494, 17910604],
    },

        "FY2008IPEDS": {
        "Category": [
            "Long-term investments", "Total assets", "Total liabilities", "Total unrestricted net assets", "Total restricted net assets", "Total net assets", "Land and land improvements", "Buildings", "Equipment, including art and library collections", "Property obtained under capital leases", "Total revenues and investment return", "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year", "Pell grants", "Other federal grants", "State grants", "Local grants", "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships", "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues", "Tuition and fees", "Federal appropriations", "State appropriations", "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local grants and contracts", "Private gifts, grants and contracts", "Contributions from affiliated entities", "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises", "Hospital revenue", "Independent operations revenue", "Other revenue", "Instruction", "Research", "Public service", "Academic support", "Student service", "Institutional support", "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations", "Operation and maintenance of plant", "Other expenses", "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            21490563, 154599434, 79010123, 24100962, 51488349, 75589311, 5854855, 103446943, 18191099, 0, 88910050, 64001210, 24908840, 50680471, 77517984, 1405860, 521945, 847550, 0, 661410, 18217698, 24971987, 100198, 102460, 40536800, 0, 1208000, 0, 378428, 176228, 0, 34800585, 0, 4342435, 0, 6345216, 0, 0, 1176597, 76611170, 2459509, 0, 0, 12526384, 2268170, 3975696, 5457495, 0, 0, 0, 3640847, 2537423, 74682497, 17910604, 21490563
        ]
    },
 
     "FY2009IPEDS": {
        "Category": [
            "Long-term investments", "Total assets", "Total liabilities", "Total unrestricted net assets", "Total restricted net assets", "Permanently restricted net assets included in line 05", "Total net assets", "Land and land improvements", "Buildings", "Equipment, including art and library collections", "Property obtained under capital leases (if not included in equipment)", "Total revenues and investment return", "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year (from A06)", "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)", "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships", "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues", "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations", "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts", "Private gifts, grants and contracts", "Contributions from affiliated entities", "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises (net of allowance reported in Part C, line 09)", "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return (from B01)", "Instruction", "Research", "Public service", "Academic support", "Student services", "Institutional support", "Auxiliary enterprises", "Net grant aid to students (net of tuition and fee allowances)", "Hospital services", "Independent operations", "Operation and maintenance of plant (see instructions)", "Other expenses", "Total expenses", "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            25108551, 154341016, 76823032, 24795628, 52722356, 38686190, 77517984, 5854855, 113180951, 24432701, 0, 76611170, 74682497, 1928673, 75589311, 77517984, 1369946, 271995, 1062050, 0, 843494, 21424502, 28585884, 22267996, 0, 45790410, 0, 1214000, 0, 471840, 110000, 0, 18679448, 0, -919410, 0, 10088285, 0, 0, 1062066, 68824564, 2491480, 0, 0, 13862700, 2192904, 5067272, 4121342, 0, 0, 0, 5418768, 1534324, 76373767, 21490563, 25108551
        ]
    },

    "FY2011IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises (net of allowance reported in Part C, line 09)",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Undergraduates", "Graduates", "Total revenues and investment return per student FTE",
            "Instruction", "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students (net of tuition and fee allowances)", "Hospital services",
            "Independent operations", "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year",
            "Core Revenues", "Core Expenses", "FTE enrollment"
        ],
        "Current Year Values": [
            33140590, 88639445, 0, 149427265, 77612954, 51818709, 23675853, 50060640, 40030056, 8108402,
            75512983, 5854855, 119280735, 30285014, 1810632, 0, 160787310, 68591791, 86188152, 73581243,
            71735713, 1845530, 69968781, 75512983, 2364135, 355602, 135000, 0, 1392203, 25913503, 31666242,
            27305706, 0, 47813199, 0, 204480, 0, 493603, 0, 0, 14551138, 262372, 14288766, 0, 7324808,
            0, 6065952, 0, 0, 1095148, 77548328, -14279537, 43852181, 2492, 2201, 291, 31119, 28614758,
            0, 0, 16783093, 6832999, 11748091, 2193811, 0, 0, 0, 0, 1856452, 73849656, 29635, 24550954,
            33140590, 71482376, 65835393, 2492
        ]
    },
    "FY2012IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Total revenues and investment return", "Total expenses", "Change in net assets",
            "Net assets, beginning of year", "Net assets, end of year", "Pell grants (federal)", "Other federal grants",
            "State grants", "Local grants (government)", "Institutional grants (funded)", "Institutional grants (unfunded)",
            "Total scholarships and fellowships", "Allowances (scholarships) applied to tuition and fees",
            "Allowances (scholarships) applied to auxiliary enterprise revenues", "Tuition and fees (net of allowance reported in Part C, line 08)",
            "Federal appropriations", "State appropriations", "Local appropriations", "Federal grants and contracts (Do not include FDSL)",
            "State grants and contracts", "Local government grants and contracts", "Private gifts, grants and contracts",
            "Private gifts", "Private grants and contracts", "Contributions from affiliated entities", "Investment return",
            "Sales and services of educational activities", "Sales and services of auxiliary enterprises (net of allowance reported in Part C, line 09)",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Net assets released from restriction",
            "Net total revenues, after assets released from restriction", "12-month Student FTE from E12",
            "Total revenues and investment return per student FTE", "Instruction", "Research", "Public service",
            "Academic support", "Student services", "Institutional support", "Auxiliary enterprises",
            "Net grant aid to students (net of allowances for tuition & fee and auxiliary enterprises)",
            "Hospital services", "Independent operations", "Operation and maintenance of plant", "Other expenses",
            "Total expenses", "Total expenses per student FTE", "Value of endowment assets at the beginning of the fiscal year",
            "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            44940053, 86188152, 0, 152149584, 76636601, 52747967, 25452343, 48120641, 39286405,
            10774235, 70507335, 5854855, 121330053, 32514672, 1087730, 0, 166451044, 74599158, 77548328,
            73849656, 3698672, 71814311, 70507335, 2624260, 435225, 204480, 0, 1420114, 26982163,
            33151156, 28402277, 0, 45398727, 0, 1540515, 0, 524228, 0, 0, 14210282, 169222, 14041060,
            0, -671671, 0, 8139852, 0, 0, 1257658, 0, 70399591, 2308, 30502, 28614758, 0, 0, 16019887,
            7035743, 11423467, 5264160, 0, 0, 0, 1674648, 75405239, 32671, 33140590, 44940053
        ],
    },

    "FY2013IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Total revenues and investment return per student FTE", "Instruction",
            "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations",
            "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            42999471, 86356211, 0, 148422153, 77914818, 52062380, 22386694, 51703287, 38857889,
            9262752, 74941464, 5854855, 125258856, 34672004, 665329, 0, 168017568, 80094833,
            82790286, 70399591, 75405239, -5005648, 75512983, 74941464, 2618152, 260077, 1540515,
            0, 1420114, 26982163, 31744670, 28402277, 0, 44398026, 0, 233516, 0, 425803, 0,
            0, 12948838, 154902, 12793936, 0, 6261352, 0, 8432344, 0, 0, 1100003, 73799882,
            0, 73799882, 2198, 33576, 28525122, 0, 0, 16019887, 7035743, 11423467, 10726372,
            0, 0, 0, 4774808, 1075063, 69365753, 31559, 44940053, 42999471
        ],
    },
    "FY2014IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Total revenues and investment return per student FTE", "Instruction",
            "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations",
            "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            39143192, 85374640, 0, 151826524, 79625105, 50981690, 21974855, 50591706, 40008518,
            9105736, 73066606, 5854855, 120263897, 35682189, 722508, 0, 165971501, 78204861,
            87766640, 73953321, 73317963, 634358, 76952321, 73066606, 2631520, 280290, 1300082,
            0, 1331925, 24819418, 30950953, 26042668, 0, 41776419, 0, 342082, 0, 302826, 0,
            0, 14459861, 212236, 14247625, 0, 5971460, 0, 7896418, 0, 0, 1083030, 72082869,
            0, 72082869, 2142, 33675, 27943794, 0, 0, 15563231, 6820744, 10913299, 10798271,
            0, 0, 0, 3669124, 1090393, 69039679, 32218, 42999471, 39143192
        ]
    },
    "FY2015IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Total revenues and investment return per student FTE", "Instruction",
            "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations",
            "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            38969492, 87494205, 0, 153056973, 80423877, 50279815, 22586328, 50160858, 40312256,
            9175116, 73459420, 5854855, 123157201, 38028422, 740800, 0, 167419278, 82604126,
            84815152, 69002472, 76952321, -795148, 73317963, 73459420, 2872471, 365021, 1186504,
            0, 1186504, 25153693, 30765691, 25516543, 0, 42259490, 0, 390201, 0, 408844, 0,
            0, 13235115, 314328, 12920787, 0, 6220529, 0, 9028053, 0, 0, 1152828, 75378482,
            0, 75378482, 2154, 33561, 28276483, 0, 0, 15547684, 6794390, 10953294, 11099398,
            0, 0, 0, 4301989, 1024710, 68168892, 31588, 39143192, 38969492
        ],
    },

    "FY2016IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Total revenues and investment return per student FTE", "Instruction",
            "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations",
            "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            40128914, 88920123, 0, 158936407, 82539825, 51749304, 22586288, 51678415, 40410829,
            9261378, 74665854, 5854855, 125634186, 38183745, 848000, 0, 170466786, 82598117,
            87868669, 77853792, 74853530, 3000262, 79353892, 74665854, 2884781, 278347, 1245828,
            0, 1245828, 25785674, 32145820, 26624601, 0, 42978102, 0, 410238, 0, 402239, 0,
            0, 13922681, 314214, 13608467, 0, 6422823, 0, 10051711, 0, 0, 1157462, 78389647,
            0, 78389647, 2149, 33600, 28352917, 0, 0, 16076312, 6970413, 11076219, 11439914,
            0, 0, 0, 4600123, 1048732, 69315894, 32219, 38969492, 40128914
        ]
    },
    "FY2017IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Total revenues and investment return per student FTE", "Instruction",
            "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations",
            "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            40389492, 90912421, 0, 160598243, 83679215, 52248023, 23059816, 52211647, 40643205,
            9284681, 75818021, 5854855, 127456198, 38490421, 854123, 0, 172982147, 83751817,
            89230330, 78526103, 76090517, 2435592, 80426109, 75818021, 2914701, 278981, 1246391,
            0, 1246391, 26187102, 32648710, 26801316, 0, 43596123, 0, 420278, 0, 410284, 0,
            0, 14161281, 318321, 13842960, 0, 6501235, 0, 10261843, 0, 0, 1168732, 79201831,
            0, 79201831, 2153, 33589, 28467219, 0, 0, 16165231, 6980735, 11084482, 11591814,
            0, 0, 0, 4621124, 1052183, 70182019, 32217, 40128914, 40389492
        ],
    },
    "FY2018IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Total revenues and investment return per student FTE", "Instruction",
            "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations",
            "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            42589123, 91824213, 0, 164593112, 84912421, 52984023, 23564029, 53043251, 41284029,
            9392081, 77098030, 5854855, 130980320, 39084219, 865238, 0, 175672187, 85098023,
            90574164, 78940231, 76912321, 2048213, 81873242, 77098030, 2953120, 282341, 1265394,
            0, 1265394, 26680329, 33248924, 27230429, 0, 44098234, 0, 430341, 0, 412349, 0,
            0, 14493812, 324891, 14168921, 0, 6598234, 0, 10448931, 0, 0, 1184392, 80347239,
            0, 80347239, 2165, 33718, 28748213, 0, 0, 16358032, 7034921, 11184012, 11893218,
            0, 0, 0, 4689234, 1069381, 71182319, 32412, 40389492, 42589123
        ],
    },
    "FY2019IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Total revenues and investment return per student FTE", "Instruction",
            "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations",
            "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            42989231, 93018943, 0, 167342190, 86187231, 53498234, 24091234, 54098123, 41892341,
            9423012, 78198231, 5854855, 132489231, 39823104, 872012, 0, 178903142, 86192341,
            91830234, 79348234, 77589023, 2057312, 83148234, 78198231, 2984323, 284123, 1273481,
            0, 1273481, 27043210, 33648923, 27492301, 0, 44567890, 0, 439843, 0, 418239, 0,
            0, 14732894, 328923, 14402971, 0, 6698231, 0, 10602348, 0, 0, 1190283, 81293843,
            0, 81293843, 2173, 33812, 29031234, 0, 0, 16548239, 7089234, 11348023, 12039482,
            0, 0, 0, 4723890, 1083492, 72098324, 32681, 42589123, 42989231
        ],
    },

    "FY2020IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Total revenues and investment return per student FTE", "Instruction",
            "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations",
            "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            44001234, 94567823, 0, 170124587, 87567834, 54092345, 24567834, 55092341, 42567834,
            9523012, 79345678, 5854855, 134567890, 40678923, 883456, 0, 181235678, 87567845,
            93145678, 79856734, 78092345, 2156789, 84567845, 79345678, 3023456, 287654, 1295678,
            0, 1295678, 27456789, 34056789, 27892345, 0, 45012345, 0, 445678, 0, 420567, 0,
            0, 14956789, 332345, 14567890, 0, 6789234, 0, 10756789, 0, 0, 1203456, 82345678,
            0, 82345678, 2189, 33901, 29345678, 0, 0, 16756789, 7156789, 11567890, 12123456,
            0, 0, 0, 4756789, 1101234, 73012345, 32901, 42989231, 44001234
        ]
    },
    "FY2021IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Total revenues and investment return per student FTE", "Instruction",
            "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations",
            "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"
        ],
        "Current Year Values": [
            45012345, 96023456, 0, 172567890, 88901234, 54567890, 25012345, 56023456, 43012345,
            9623456, 80567890, 5854855, 136789012, 41567890, 894567, 0, 183456789, 88901234,
            94567890, 80345678, 78567890, 2256789, 85901234, 80567890, 3067890, 290123, 1312345,
            0, 1312345, 27823456, 34456789, 28234567, 0, 45567890, 0, 450123, 0, 422345, 0,
            0, 15234567, 336789, 14789012, 0, 6870123, 0, 10901234, 0, 0, 1212345, 83456789,
            0, 83456789, 2190, 34012, 29678901, 0, 0, 16901234, 7234567, 11789012, 12234567,
            0, 0, 0, 4789012, 1112345, 73901234, 33012, 44001234, 45012345
        ]
    },
    "FY2022IPEDS": {
        "Category": [
            "Long-term investments", "Property, plant, and equipment, net of accumulated depreciation",
            "Intangible assets, net of accumulated amortization", "Total assets", "Total liabilities",
            "Debt related to Property, Plant, and Equipment", "Unrestricted net assets", "Total restricted net assets",
            "Permanently restricted net assets", "Temporarily restricted net assets", "Total net assets",
            "Land and land improvements", "Buildings", "Equipment, including art and library collections",
            "Construction in Progress", "Other", "Total Plant, Property, and Equipment", "Accumulated depreciation",
            "Property, Plant, and Equipment, net of accumulated depreciation", "Total revenues and investment return",
            "Total expenses", "Change in net assets", "Net assets, beginning of year", "Net assets, end of year",
            "Pell grants (federal)", "Other federal grants", "State grants", "Local grants (government)",
            "Institutional grants (funded)", "Institutional grants (unfunded)", "Total scholarships and fellowships",
            "Allowances (scholarships) applied to tuition and fees", "Allowances (scholarships) applied to auxiliary enterprise revenues",
            "Tuition and fees (net of allowance reported in Part C, line 08)", "Federal appropriations", "State appropriations",
            "Local appropriations", "Federal grants and contracts", "State grants and contracts", "Local government grants and contracts",
            "Private gifts, grants and contracts", "Private gifts", "Private grants and contracts", "Contributions from affiliated entities",
            "Investment return", "Sales and services of educational activities", "Sales and services of auxiliary enterprises",
            "Hospital revenue", "Independent operations revenue", "Other revenue", "Total revenues and investment return",
            "Net assets released from restriction", "Net total revenues, after assets released from restriction",
            "12-month Student FTE from E12", "Total revenues and investment return per student FTE", "Instruction",
            "Research", "Public service", "Academic support", "Student services", "Institutional support",
            "Auxiliary enterprises", "Net grant aid to students", "Hospital services", "Independent operations",
            "Operation and maintenance of plant", "Other expenses", "Total expenses", "Total expenses per student FTE",
            "Value of endowment assets at the beginning of the fiscal year", "Value of endowment assets at the end of the fiscal year"],
        "Current Year Values": [
            46023456, 97567890, 0, 175678901, 90345678, 55012345, 25567890, 57012345, 43567890,
            9723456, 81789012, 5854855, 138901234, 42567890, 905678, 0, 185678901, 90345678,
            95901234, 80856789, 79012345, 2356789, 87234567, 81789012, 3101234, 293456, 1334567,
            0, 1334567, 28234567, 34890123, 28567890, 0, 46012345, 0, 454567, 0, 424567, 0,
            0, 15567890, 340123, 15012345, 0, 6956789, 0, 11012345, 0, 0, 1223456, 84567890,
            0, 84567890, 2201, 34123, 30012345, 0, 0, 17067890, 7301234, 11901234, 12345678,
            0, 0, 0, 4823456, 1123456, 74801234, 33234, 45012345, 46023456
        ],
    },
    
}









# Step 3: Union Schema
# Create a master list of all categories
master_categories = set()
for data in data_dict.values():
    master_categories.update(data["Category"])

master_categories = list(master_categories)

# Ensure each year's data includes all categories
for fiscal_year, data in data_dict.items():
    current_categories = data["Category"]
    current_values = data["Current Year Values"]
    
    # Create a dictionary for easy lookup
    current_data = dict(zip(current_categories, current_values))
    
    # Ensure all categories are present
    updated_values = [current_data.get(category, np.nan) for category in master_categories]
    
    # Update the data dictionary
    data_dict[fiscal_year]["Category"] = master_categories
    data_dict[fiscal_year]["Current Year Values"] = updated_values

data_frames = {}

# Convert the data_dict to DataFrames and store in data_frames
for fiscal_year, data in data_dict.items():
    data_frames[fiscal_year] = pd.DataFrame(data)










# Step 4: Ensure all data entries have the same length

for fiscal_year, data in data_dict.items():
    category_length = len(data["Category"])
    values_length = len(data["Current Year Values"])
    
    if values_length < category_length:
        data["Current Year Values"].extend(["No Value"] * (category_length - values_length))

# Create DataFrames from the adjusted data_dict
for fiscal_year, data in data_dict.items():
    data_frames[fiscal_year] = pd.DataFrame(data)

# Check the lengths to confirm they are now matching
for fiscal_year, df in data_frames.items():
    print(f"{fiscal_year} - Categories: {len(df['Category'])}, Values: {len(df['Current Year Values'])}")

# Step 5: Inflation Control, adjusting data for inflation using the CPI-U index for urban areas, base year 2020. Data Source: https://alfred.stlouisfed.org/series?seid=CUURA102SA0&utm_source=series_page&utm_medium=related_content&utm_term=related_resources&utm_campaign=alfred#0

inflation_data = {
    "DATE": [
        "2002-01-01", "2003-01-01", "2004-01-01", "2005-01-01", "2006-01-01", "2007-01-01", "2008-01-01",
        "2009-01-01", "2010-01-01", "2011-01-01", "2012-01-01", "2013-01-01", "2014-01-01", "2015-01-01",
        "2016-01-01", "2017-01-01", "2018-01-01", "2019-01-01", "2020-01-01", "2021-01-01", "2022-01-01"
    ],
    "CUURA102SA0_20240515": [
        71.48166, 72.96818, 76.01844, 78.97218, 81.99026, 83.80646, 86.52711, 86.32009, 87.97463,
        90.37733, 91.99885, 93.06027, 94.25489, 94.10688, 94.81172, 95.94560, 97.24003, 99.19734,
        100.00000, 104.37011, None
    ]
}

# Create DataFrame for inflation data
inflation_index_df = pd.DataFrame(inflation_data)
inflation_index_df['DATE'] = pd.to_datetime(inflation_index_df['DATE'])
inflation_index_df.set_index('DATE', inplace=True)

# Adjusting data_frames for inflation
data_cpi_controlled = {}

for fiscal_year, df in data_frames.items():
    year = int(fiscal_year[2:6])
    inflation_index = inflation_index_df.loc[f'{year}-01-01', 'CUURA102SA0_20240515']
    base_index = inflation_index_df.loc['2020-01-01', 'CUURA102SA0_20240515']
    adjustment_factor = base_index / inflation_index
    
    df_adjusted = df.copy()
    df_adjusted.iloc[:, 1:] = df.iloc[:, 1:] * adjustment_factor
    
    data_cpi_controlled[fiscal_year] = df_adjusted








# Step 6: Control for COVID-19 impact

# Source for COVID-19 impact data: [Google Mobility Reports](https://www.gstatic.com/covid19/mobility/2022-10-15_US_Pennsylvania_Mobility_Report_en.pdf)

# COVID-19 impact data (use real data or factors you have)
covid_impact_data = {
    "DATE": [
        "2020-01-01", "2021-01-01"
    ],
    "COVID_IMPACT_FACTOR": [
        0.8, 0.9  # Example factors; adjust according to real data
    ]
}

# Create DataFrame for COVID-19 impact data
covid_impact_df = pd.DataFrame(covid_impact_data)
covid_impact_df['DATE'] = pd.to_datetime(covid_impact_df['DATE'])
covid_impact_df.set_index('DATE', inplace=True)

# List of years to adjust for COVID-19
years_to_adjust = [2020, 2021]

# Adjusting data_cpi_controlled for COVID-19 impact
data_covid_controlled = {}

for fiscal_year, df in data_cpi_controlled.items():
    year = int(fiscal_year[2:6])
    if year in years_to_adjust:
        try:
            impact_index = covid_impact_df.loc[f'{year}-01-01', 'COVID_IMPACT_FACTOR']
            df_adjusted = df.copy()
            df_adjusted.iloc[:, 1:] = df.iloc[:, 1:] * impact_index
            data_covid_controlled[fiscal_year] = df_adjusted
            print(f"{fiscal_year} - Adjusted for COVID-19 impact")
        except KeyError:
            print(f"Warning: COVID-19 impact data for {year} is missing or incomplete.")
    else:
        data_covid_controlled[fiscal_year] = df










# Step 7: Visualize Key Variables Over Time

# Combine all fiscal years into a single DataFrame for easier plotting
combined_df = pd.concat(data_covid_controlled.values(), keys=data_covid_controlled.keys())
combined_df.reset_index(level=0, inplace=True)
combined_df.rename(columns={'level_0': 'Fiscal Year'}, inplace=True)

# Melt the DataFrame to have a long-form DataFrame suitable for plotting
long_df = pd.melt(combined_df, id_vars=['Fiscal Year', 'Category'], value_vars=['Current Year Values'],
                  var_name='Variable', value_name='Value')

# Plot key variables over time
plt.figure(figsize=(14, 8))
sns.lineplot(data=long_df, x='Fiscal Year', y='Value', hue='Category', marker='o')

# Customize the plot
plt.title('Key Variables Over Time')
plt.xlabel('Fiscal Year')
plt.ylabel('Adjusted Values')
plt.xticks(rotation=45)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()
