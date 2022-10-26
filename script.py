import json
import sys
import os.path

protein_data = [
  {
    "conditionComparison": "S1 - S2",
    "up.condition": "S1",
    "down.condition": "S2",
    "fdrLimit": 0.00336921246864423,
    "data": [
      {
        "GroupId": 1,
        "GroupLabel": "AAAA",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": "AAAA",
        "GeneNames": "GNAAAA",
        "Description": "Protein AA-RON",
        "FoldChange": -0.0551770099399853,
        "AdjustedPValue": 0.902516404445127,
        "PValue": 0.7
      },
      {
        "GroupId": 7,
        "GroupLabel": "BBBB",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": "BBBB",
        "GeneNames": "GNBBBB",
        "Description": "Protein BB-BRON",
        "FoldChange": 0.154339623642233,
        "AdjustedPValue": 0.911776448109943,
        "PValue": 0.4
      }
    ]
  }
]

json_object = json.dumps(protein_data)
 
with open(os.path.join(sys.argv[1], 'protein_viz.json'), "w") as outfile:
    outfile.write(json_object)
