#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
ofstream myOutput;

bool isFrontSmaller(int in1, int in2){
	if (in1 <= in2)
		return true;
	else
		return false;
}

bool checkNum(string in){
	cout << in << endl << endl;
	int sLength = in.length() - 1;
	int i = 0;
	bool bResult = true;

	if (sLength == 0)
		return true;
		//myOutput << "Case #" << iCase << ": " << in << endl;

	bResult = isFrontSmaller(in.at(i), in.at(i + 1));

	while (bResult && i < sLength) {
		i++;

		if (i < sLength)
			bResult = isFrontSmaller(in.at(i), in.at(i + 1));
	}


	if (i == sLength)
		return true;

	return false;
}

int main(){
	string line;
	int iCases;
	int iCaseNow = 1;
	ifstream myInput("input0.txt");
	bool bChecked = true;
	int iNumber = 0;

	myOutput.open("output.txt");

	getline(myInput, line);
	istringstream str(line);

	str >> iCases;

	while (getline(myInput, line)){
		bChecked = checkNum(line);
		iNumber = stoi(line);

		while (bChecked == false){
			bChecked = checkNum(line);

			cout << "here" << endl << endl;
			iNumber = iNumber - 1;
				
			stringstream newValue;
			newValue << iNumber;

			cout << newValue.str() << endl << endl;
			bChecked = checkNum(newValue.str());

		}

//		if (bChecked)
			myOutput << "Case #" << iCaseNow << ": " << iNumber << endl;

		iCaseNow++;
	}

	myInput.close();
	myOutput.close();

	return 0;
}
