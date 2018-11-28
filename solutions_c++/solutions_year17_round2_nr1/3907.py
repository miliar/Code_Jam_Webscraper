#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

const string INPUT_FILE = "A-large.in";
const string OUTPUT_FILE = "A-large.txt";
const bool DEBUG_LOG = true;


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
	int goalDistance = 0;
	string construction = "";
	for (int x = 0; x < input.length(); x++) {
		if (input[x] != ' ')
			construction.append(1, input[x]);
		else {
			goalDistance = stoi(construction);
			construction.resize(0);
		}
	}
	int numberOfPonies = stoi(construction);
	float slowestPonySpeed = 0;
	float slowestPonyDistance = 0;
	double slowestPonyTime = 0;
	for (int p = 0; p < numberOfPonies; p++) {
		getline(inputFile, input);
		
		int ponyPosition = 0;
		int ponySpeed = 0;
		construction.resize(0);
		for (int x = 0; x < input.length(); x++) {
			if (input[x] != ' ')
				construction.append(1,input[x]);
			else {
				ponyPosition = stoi(construction);
				construction.resize(0);
			}
		}
		ponySpeed = stoi(construction);
		double ponyTime = ((double)goalDistance - (double)ponyPosition) / (double)ponySpeed;
		cout << i << ": " << ponySpeed << endl;
	//	cout << goalDistance - ponyPosition;
		if (ponyTime > slowestPonyTime)
			slowestPonyTime = ponyTime;
	}
	double aPonyTime = (double)goalDistance / slowestPonyTime;
	outputFile << setprecision(20);
	outputFile << "CASE #" << i + 1 << ": " << aPonyTime << endl;

}
system("pause");
outputFile.close();
inputFile.close();
}
