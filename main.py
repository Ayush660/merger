from gooey import Gooey, GooeyParser
import pandas as pd

@Gooey(program_name = "merger")
def main():
    parser = GooeyParser()

    parser.add_argument("file1", widget="FileChooser",gooey_options={'wildcard':"Comma separated file (*.csv)|*.csv"}, help="Select the csv file", metavar="CSV File")
    parser.add_argument("left", action="store", help="Enter the column of csv over which you need to merge", metavar="CSV Merge Column")
    parser.add_argument("file2", widget="FileChooser",gooey_options={'wildcard':"All Excel (*.xlsx)|*.xlsx"}, help="Select the excel file", metavar="EXCEL File")
    parser.add_argument("right", action="store", help="Enter the column of excel over which you need to merge", metavar="Excel Merge Column")
    parser.add_argument("save", action="store", help="Enter the name for the merged file", metavar="Merged file name")

    args = parser.parse_args()

    f1 = args.file1.replace("\\", "\\\\")
    f2 = args.file2.replace("\\", "\\\\")

    file1_df = pd.read_csv(f1, skiprows=5)
    file1_df[args.left] = pd.to_datetime(file1_df[args.left], format='%H:%M:%S').dt.time

    file2_df = pd.read_excel(f2, usecols="A:E")
    file2_df[args.right] = pd.to_datetime(file2_df[args.right], format='%H:%M:%S').dt.time

    merged_df = pd.merge(file1_df, file2_df, left_on=args.left, right_on=args.right,how='inner')
    output_file_path = args.save+".xlsx"
    merged_df.to_excel(output_file_path, index=False)

    print("File merged succesfully and saved in the current directory")

main()