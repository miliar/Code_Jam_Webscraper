// CodeJamQualificationCBathroomStalls.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
// include files
#include <iostream>
#include <ctime>
#include <fstream>
#include <sstream>
using namespace std;


int main()
{
	// declare problem variables
	int T = 0;
	long long int N = 0;
	long long int K = 0;

	// declare additional variables
	const int maxSize = 10000;
	int stallArray[maxSize + 2][5];
	long long int outputArray[1000][2];
	long long int i = 0, j = 0, a = 0, b = 0;
	long long int stallCount = 0;
	long long int curMin = -1, curMax = -1, curStall = 0;
	char testChar;
	string inputStr;
	bool getChars = true;
	bool finishedN = false;
	clock_t startTime, currentTime;
	double elapsedSeconds;
	ifstream inputFilename;
	ofstream outputFilename;


	// initialise variables
	startTime = clock();
	for (i = 0; i < maxSize + 2; i++) {
		stallArray[i][0] = 0;
		stallArray[i][1] = 0;
		stallArray[i][2] = 0;
		stallArray[i][3] = 0;
		stallArray[i][4] = 0;
	}
	for (i = 0; i < 1000; i++) {
		outputArray[i][0] = 0;
		outputArray[i][1] = 0;
	}

	// open input file
	inputFilename.open("Input Text.txt");
	if (inputFilename.is_open()) {
		cout << "open" << endl;;
	}
	else {
		cout << "not open" << endl;
	}
	// find out how many lines we have
	getline(inputFilename, inputStr);
	//try converting to integer 
	stringstream myStream(inputStr);
	myStream >> T;

	for (i = 0; i < T; i++) {
		for (j = 0; j < maxSize; j++) {
			stallArray[j][0] = 0;
			stallArray[j][1] = 0;
			stallArray[j][2] = 0;
			stallArray[j][3] = 0;
			stallArray[j][4] = 0;
		}
		getChars = true;
		K = 0;
		N = 0;
		finishedN = false;
		while (getChars) {
			// read file into digitArray
			inputFilename.get(testChar);
			//cout << testChar;
			switch (testChar) {
			case '\n':
				getChars = false;
				break;
			case ' ':
				finishedN = true;
				break;
			default:
				if (finishedN == false) {
					N *= 10;
					N += int(testChar - 48);
				}
				else {
					K *= 10;
					K += int(testChar - 48);
				}
			}

		}
		//place the people into stalls
		stallArray[0][0] = 1;
		stallArray[0][1] = 0;
		stallArray[0][2] = 0;
		stallArray[0][3] = 0;
		stallArray[0][4] = 0;
 		stallArray[N + 1][0] = 1;
		stallArray[N + 1][1] = 0;
		stallArray[N + 1][2] = 0;
		stallArray[N + 1][3] = 0;
		stallArray[N + 1][4] = 0;
		for (j = 0; j < K; j++) {
			//calculate Rs and Ls
			for (a = 0; a < N + 1; a++) {
				if (stallArray[a][0] == 0) {
					stallCount = 0;
					for (b = 1; b < a; b++) {
						if (stallArray[a - b][0] == 0) {
							stallCount++;
						}
						else {
							break;
						}
					}
					stallArray[a][1] = stallCount;
					stallCount = 0;
					for (b = 1; b < N - a + 1; b++) {
						if (stallArray[a + b][0] == 0) {
							stallCount++;
						}
						else {
							break;
						}
					}
					stallArray[a][2] = stallCount;
					if (stallArray[a][1] < stallArray[a][2]) {
						stallArray[a][3] = stallArray[a][1];
						stallArray[a][4] = stallArray[a][2];
					}
					else {
						stallArray[a][3] = stallArray[a][2];
						stallArray[a][4] = stallArray[a][1];
					}
					if (stallArray[a][3] > curMin) {
						curStall = a;
						curMin = stallArray[a][3];
						curMax = stallArray[a][4];
					}
					else {
						if (stallArray[a][3] == curMin) {
							if (stallArray[a][4] > curMax) {
								curStall = a;
								curMin = stallArray[a][3];
								curMax = stallArray[a][4];
							}
						}
					}
				}
			}
			// occupy the right stall
			stallArray[curStall][0] = 1;
			curMin = -1;
			curMax = -1;
		}

		// output the last values tested
		outputArray[i][0] = stallArray[curStall][4];
		outputArray[i][1] = stallArray[curStall][3];
	}

	inputFilename.close();

	// output results to file and screen (include timing on screen)
	outputFilename.open("Output Text.txt", ios::trunc);
	for (i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": " << outputArray[i][0] << " " << outputArray[i][1] << endl;
		outputFilename << "Case #" << i + 1 << ": " << outputArray[i][0] << " " << outputArray[i][1] << "\n";
	}
	outputFilename.close();

	currentTime = clock();
	elapsedSeconds = ((currentTime - startTime) / (CLOCKS_PER_SEC / 1.0));
	cout.precision(4);
	cout << "This took: " << fixed << elapsedSeconds << " seconds to run" << endl << endl;

	cout << "Do you want another go (Y/N)? ";
	getline(cin, inputStr);

	return 0;
}


