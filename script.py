import json
import sys
import os.path

protein_ids_prefix = 'LUKE_'

protein_data = [
  {
    "conditionComparison": "S1 - S2",
    "up.condition": "S1",
    "down.condition": "S2",
    "fdrLimit": 0.00336921246864423,
    "data": [
      {
        "GroupId": 1,
        "GroupLabel": "A0A061ACU2",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0A061ACU2',
        "GeneNames": "pezo-1",
        "Description": "Piezo-type mechanosensitive ion channel component 1",
        "QValue": 0.0001113213875,
        "FoldChange": -0.0551770099399853,
        "AdjustedPValue": 0.902516404445127,
        "PValue": 0.620461935270199,
        "ConfLow": -0.308936755456975,
        "ConfHigh": 0.198582735577004
      },
      {
        "GroupId": 7,
        "GroupLabel": "A0A0B4J2F0",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0A0B4J2F0',
        "GeneNames": "PIGBOS1",
        "Description": "Protein PIGBOS1",
        "QValue": 0.0006715916679,
        "FoldChange": 0.154339623642233,
        "AdjustedPValue": 0.911776448109943,
        "PValue": 0.647410434830348,
        "ConfLow": -0.615293130536369,
        "ConfHigh": 0.923972377820836
      },
      {
        "GroupId": 13,
        "GroupLabel": "A0A0K3AUJ9",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0A0K3AUJ9',
        "GeneNames": "prdx-2",
        "Description": "Peroxiredoxin prdx-2",
        "QValue": 0.0001113213875,
        "FoldChange": -0.176172887660552,
        "AdjustedPValue": 0.538218764136345,
        "PValue": 0.163945820488019,
        "ConfLow": -0.445186911949189,
        "ConfHigh": 0.0928411366280838
      },
      {
        "GroupId": 15,
        "GroupLabel": "A0A0U1RRE5",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0A0U1RRE5',
        "GeneNames": "NBDY",
        "Description": "Negative regulator of P-body association",
        "QValue": 0.004292254802,
        "FoldChange": -0.517674027840734,
        "AdjustedPValue": 0.646499716154827,
        "PValue": 0.243613806385724,
        "ConfLow": -1.48414359665611,
        "ConfHigh": 0.448795540974647
      },
      {
        "GroupId": 16,
        "GroupLabel": "A0A131MBU3",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0A131MBU3',
        "GeneNames": "irg-7",
        "Description": "Protein irg-7",
        "QValue": 0.0001113213875,
        "FoldChange": -0.238000708167711,
        "AdjustedPValue": 0.0240501398655104,
        "PValue": 0.00108255200292739,
        "ConfLow": -0.341752256216784,
        "ConfHigh": -0.134249160118637
      },
      {
        "GroupId": 17,
        "GroupLabel": "A0A131MCZ8",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0A131MCZ8',
        "GeneNames": "cnnm-3",
        "Description": "Metal transporter cnnm-3",
        "QValue": 0.0001113213875,
        "FoldChange": 0.0506618947873463,
        "AdjustedPValue": 0.980047659101529,
        "PValue": 0.898394204267664,
        "ConfLow": -0.861197185603416,
        "ConfHigh": 0.962520975178108
      },
      {
        "GroupId": 18,
        "GroupLabel": "A0A1C3NSL9",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0A1C3NSL9',
        "GeneNames": "ajm-1",
        "Description": "Apical junction molecule",
        "QValue": 0.0001113213875,
        "FoldChange": -0.0591068997964967,
        "AdjustedPValue": 0.813799283520483,
        "PValue": 0.447062558521999,
        "ConfLow": -0.233801975457213,
        "ConfHigh": 0.11558817586422
      },
      {
        "GroupId": 21,
        "GroupLabel": "A0A1W2PPF3",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0A1W2PPF3',
        "GeneNames": "DUXB",
        "Description": "Double homeobox protein B",
        "QValue": 0.004447326995,
        "FoldChange": 0.0440628067900448,
        "AdjustedPValue": 0.966957208387321,
        "PValue": 0.836170946619789,
        "ConfLow": -0.445131720363824,
        "ConfHigh": 0.533257333943914
      },
      {
        "GroupId": 22,
        "GroupLabel": "A0A1W2PQ73",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0A1W2PQ73',
        "GeneNames": "ERFL",
        "Description": "ETS domain-containing transcription factor ERF-like",
        "QValue": 0.004447326995,
        "FoldChange": 0.0440143719591539,
        "AdjustedPValue": 0.97818851047379,
        "PValue": 0.886989923802867,
        "ConfLow": -0.667680689927923,
        "ConfHigh": 0.755709433846231
      },
      {
        "GroupId": 25,
        "GroupLabel": "A0AV96",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0AV96',
        "GeneNames": "RBM47",
        "Description": "RNA-binding protein 47",
        "QValue": 0.0001113213875,
        "FoldChange": 0.142243082194501,
        "AdjustedPValue": 0.962205498282224,
        "PValue": 0.824095047606873,
        "ConfLow": -1.32654999435135,
        "ConfHigh": 1.61103615874035
      },
      {
        "GroupId": 27,
        "GroupLabel": "A0AVT1",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0AVT1',
        "GeneNames": "UBA6",
        "Description": "Ubiquitin-like modifier-activating enzyme 6",
        "QValue": 0.0001113213875,
        "FoldChange": 0.0513500708281427,
        "AdjustedPValue": 0.877472428235146,
        "PValue": 0.559415848205481,
        "ConfLow": -0.148234172149371,
        "ConfHigh": 0.250934313805656
      },
      {
        "GroupId": 28,
        "GroupLabel": "A0FGR8",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0FGR8',
        "GeneNames": "ESYT2",
        "Description": "Extended synaptotagmin-2",
        "QValue": 0.0001113213875,
        "FoldChange": -0.0286194176354542,
        "AdjustedPValue": 0.951227047734925,
        "PValue": 0.770905721833914,
        "ConfLow": -0.253889942261268,
        "ConfHigh": 0.196651106990359
      },
      {
        "GroupId": 31,
        "GroupLabel": "A0MZ66",
        "GroupLabelType": "ProteinAccession",
        "ProteinIds": f'{protein_ids_prefix}A0MZ66',
        "GeneNames": "SHTN1",
        "Description": "Shootin-1",
        "QValue": 0.0001113213875,
        "FoldChange": 0.10460717313245,
        "AdjustedPValue": 0.737577531964879,
        "PValue": 0.33933455790066,
        "ConfLow": -0.138106560835618,
        "ConfHigh": 0.347320907100519
      },
    ]
  }
]

json_object = json.dumps(protein_data)
 
with open(os.path.join(sys.argv[1], 'protein_viz.json'), "w") as outfile:
    outfile.write(json_object)
