#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int sortInt(int iVal)
{
	int tmpVal = iVal;

	do
	{
		int currVal = tmpVal % 10;
		int prevVal = (tmpVal / 10) % 10;

		if (prevVal > currVal)
			return sortInt(iVal - 1);
		tmpVal /= 10;
	}while(tmpVal != 0);

	return iVal;
}

int main(int argc, char* argv[])
{
	ifstream inputFile;
	string line;

	inputFile.open(argv[1], ios::in);
	if (!inputFile.is_open())
	{
		cout<< "File Open Error~!"<< endl;
		return 0;
	}

	getline(inputFile, line);
	int testCnt = stoi(line);

	for (int i=0; i<testCnt; i++)
	{
		getline(inputFile, line);
		int retVal = stoi(line);
		cout<< "Case #"<< i + 1<< ": "<< sortInt(retVal)<< endl;
	}

	inputFile.close();
	
	return 0;
}
