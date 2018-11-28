#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const string INPUT_FILE = "A-large.in";
const string OUTPUT_FILE = "A-large.txt";
const bool DEBUG_LOG = true;

string process(string toProcess) {
	string toReturn = "";
	string arguments[2];
	int arg = 0;
	string buildingString = "";
	for (int i = 0; i <= toProcess.length(); i++) {
		if (toProcess[i] == ' ' || i == toProcess.length()) {
			arguments[arg] = buildingString;
			arg++;
			buildingString = "";
		}
		else {
			buildingString += toProcess[i];
		}
	}

	string pancakeSequence = arguments[0];
	int flipperSize = stoi(arguments[1]);
	int flips = 0;
	int pos = 0;
	cout << pancakeSequence << endl;

	while (true) {
		if (pancakeSequence[pos] == '-') {
			for (int i = pos; i < pos + flipperSize; i++) {
				if (i > pancakeSequence.length()) {
					return to_string(-1);
				}
				if (pancakeSequence[i] == '-')
					pancakeSequence[i] = '+';
				else
					pancakeSequence[i] = '-';
			}
			flips++;
			pos = 0;		
		}
		pos += 1;
		if (pos > pancakeSequence.length())
			break;
	}
	cout << pancakeSequence << endl;

	if (DEBUG_LOG) {
		cout << toReturn << endl;
	}
	toReturn = to_string(flips);
	return toReturn;
}
int main() {

	ifstream inputFile;
	ofstream outputFile;
	inputFile.open(INPUT_FILE);
	outputFile.open(OUTPUT_FILE);
	string input;
	getline(inputFile, input);
	int numberOfProblems = stoi(input);
	for (int i = 0; i < numberOfProblems; i++) {
		getline(inputFile, input);
		string rawOutput = process(input);
		if (stoi(rawOutput) == -1) {
			rawOutput = "IMPOSSIBLE";
		}
		outputFile << "Case #" + to_string(i + 1) + ": " << rawOutput << endl;
	}
	outputFile.close();
	inputFile.close();
	if (DEBUG_LOG)
		cout << "Press Enter to exit";
		getchar();
}