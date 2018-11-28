#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

const string INPUT_FILE = "C-small-1-attempt1.in";
const string OUTPUT_FILE = "C-Small-1.txt";
const bool DEBUG_LOG = true;
class stall;
vector<stall> stallMap = vector<stall>();

class stall {
public:

	bool occupied = false;
	int leftDistance;
	int rightDistance;
	int minimumNumber;
	int maximumNumber;
	stall(int index,int numberOfStalls) {
		leftDistance = index - 1;
		rightDistance = numberOfStalls - 2 - index;
		Update();
	}
	void SetLeft(int bla) {
		leftDistance = bla;
	}
	void SetRight(int bla) {
		rightDistance = bla;
	}
	void Update() {

		if (rightDistance < leftDistance) {
			minimumNumber = rightDistance;
			maximumNumber = leftDistance;
		}
		else {
			minimumNumber = leftDistance;
			maximumNumber = rightDistance;
		}
	}

	void Occupy(int index,int numberOfStalls) {
		occupied = true;
		int distance = 0;
		for (int i = index + 1; i < numberOfStalls; i++) {
			if (!stallMap[i].occupied) {
				stallMap[i].SetLeft(distance + 1);
				//cout << "SET THING AT INDEX " << i << " TO " << distance << endl;
				stallMap[i].Update();
			}
			else {
				rightDistance = distance;
				break;
			}
			distance++;


		}

		distance = 0;
		for (int i = index - 1; i >= 0; i--) {
			if (!stallMap[i].occupied) {
				stallMap[i].SetRight(distance + 1);
				stallMap[i].Update();
			}
			else {

				leftDistance = distance;

				break;
			}
			distance++;
		}
		Update();

	}

};




int StallSort(int numberOfStalls) {
	int considerationIndex = 0;
	int maxMin = 0;
	for (int i = 1; i < numberOfStalls - 1; i++) {
		if (!stallMap[i].occupied) {
			if (stallMap[i].minimumNumber > maxMin) {
				maxMin = stallMap[i].minimumNumber;
				considerationIndex = i;
			}
			else {
				if (stallMap[i].minimumNumber == maxMin) {
					if (stallMap[i].maximumNumber > stallMap[considerationIndex].maximumNumber) {
						considerationIndex = i;
					}
				}
			}
		}
	}

	return considerationIndex;
}
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
	int numberOfStalls = stoi(arguments[0]) + 2;
	int numberOfPeople = stoi(arguments[1]);
	if (numberOfStalls - 2 == numberOfPeople) {
		return "0 0";
	}
	stallMap.clear();
	
	for (int i = 0; i < numberOfStalls; i++) {
		stallMap.push_back(stall(i,numberOfStalls));
	}
	
	stallMap[0].occupied = true;
	stallMap[numberOfStalls - 1].occupied = true;
	stallMap[0].Occupy(0,numberOfStalls);
	stallMap[numberOfStalls - 1].Occupy(numberOfStalls - 1,numberOfStalls);
	for (int p = 0; p < numberOfPeople; p++) {

		int placementIndex = StallSort(numberOfStalls);

		stallMap[placementIndex].Occupy(placementIndex,numberOfStalls);


		if (p == numberOfPeople - 1) {
			return to_string(stallMap[placementIndex].maximumNumber) + " " + to_string(stallMap[placementIndex].minimumNumber);
		} 
		if (p == numberOfPeople / 2) {
			cout << "50% Complete";
			cout << endl;

		}
		if (p == numberOfPeople / 4) {
			cout << "25% Complete";
			cout << endl;

		}
		if (p == (numberOfPeople / 4) * 3) {
			cout << "75% Complete";
			cout << endl;
		}
	}
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
cout << "SOLVING " << numberOfProblems << " PROBLEMS...." << endl;
for (int i = 0; i < numberOfProblems; i++) {
getline(inputFile, input);
string rawOutput = process(input);

outputFile << "Case #" + to_string(i + 1) + ": " << rawOutput << endl;
cout << "SOLVED PROBLEM " << i + 1;
cout << endl;
}
outputFile.close();
inputFile.close();
if (DEBUG_LOG)
cout << "Press Enter to exit";
getchar();
}
