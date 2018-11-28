#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const string INPUT_FILE = "B-small-attempt0.in";
const string OUTPUT_FILE = "B-small-attempt0.txt";
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
	int lastNumber = stoi(toProcess);
	int tidyNumber = 0;
	for (int i = 1; i <= lastNumber; i++) {
		string number = to_string(i);
		if (number.length() == 1) {
			tidyNumber = i;
		}
		else {
			bool success = true;
			for (int x = 1; x < number.length(); x++) {
				string toConvert1 = "";
				toConvert1 += number[x];
				string toConvert2 = "";
				toConvert2 += number[x - 1];
				if (stoi(toConvert1) < stoi(toConvert2)) {
					success = false;
					break;
				}
			}
			if (success) {
				tidyNumber = i;
			}
		}
	}
	if (DEBUG_LOG) {
		cout << toReturn << endl;
	}
	
	return to_string(tidyNumber);
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