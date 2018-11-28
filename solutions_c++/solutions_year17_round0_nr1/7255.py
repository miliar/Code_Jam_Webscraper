#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;
int min_flip(string pancakeRow, const int & flipperSize)
{
	int result = 0;
	for (int i = 0; i != pancakeRow.length(); ++i)
	{
		if (pancakeRow[i] == '+') { continue; }
		if (i + flipperSize > pancakeRow.length()) { return -1; }
		++result;
		for (int j = 0; j != flipperSize; ++j)
		{
			if (pancakeRow[i + j] == '-') { pancakeRow[i + j] = '+'; }
			else { pancakeRow[i + j] = '-'; }
		}
	}
	return result;
}
int main()
{
	const string in = "A-large.in";
	const string out = "A-large.out";
	ofstream outputFile(out);
	ifstream inputFile(in);
	if (!inputFile.is_open())
	{
		cout <<"Cannot open input file";
		outputFile.close();
		return 1;
	}
	string line;
	int case_num = 1;
	while (getline(inputFile, line))
	{
			istringstream iss(line);
			string panCakeRow;
			int flipperSize;
			if (!(iss >> panCakeRow >> flipperSize)) { continue; }
			int rc = min_flip(panCakeRow, flipperSize);
			outputFile << "Case #" << case_num++ << ": ";
			if (rc == -1) outputFile << "IMPOSSIBLE" << endl;
			else outputFile << rc << endl;
	}
	inputFile.close();
	outputFile.close();
	return 0;
}



