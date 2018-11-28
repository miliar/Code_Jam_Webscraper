#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int pancakeFlip(std::string cookingSetup);

int main()
{
	ifstream inStream;
	inStream.open("A-large.in");
	ofstream outStream;
	outStream.open("A-solution.out");

	if (inStream.is_open())
	{
		int caseNo = 1;
		string inputLine;
		getline(inStream, inputLine);
		while (getline(inStream, inputLine))
		{
			string result = to_string(pancakeFlip(inputLine));
			if (result == "-1") { result = "IMPOSSIBLE"; }

			outStream << "Case #" << caseNo << ": " << result << endl;
			caseNo++;
		}
		inStream.close();
		outStream.close();
	}
	else
	{
		cout<<"stream not open"<<endl;
	}
	return 0;
}

int pancakeFlip(string cookingSetup)
{
	int pancakeNumber = cookingSetup.find_first_of(' ');
	vector<bool> pancakeState;
	int flipperSize = stoi(cookingSetup.substr(pancakeNumber + 1));
	int flipperUsage = 0;

	for (int i = 0; i < pancakeNumber; i++)
	{
		if (cookingSetup.at(i) == '+') { pancakeState.push_back(true); }
		else { pancakeState.push_back(false); }
	}
	
	for (int i = 0; i < pancakeNumber; i++)
	{
		if (pancakeState[i] == true) {}
		else if (pancakeState[i] == false && i <= pancakeNumber - flipperSize)
		{
			for (int j = 0; j < flipperSize; j++)
			{
				pancakeState[i + j] = !pancakeState[i + j];
			}
			flipperUsage++;
		}
		else
		{
			flipperUsage = -1;
		}
	}
	
	return flipperUsage;
}
