// CodeJamQualificationAPancakeFlipper.cpp : Defines the entry point for the console application.
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
	int SLength = 0;
	int K = 0;

	// declare additional variables
	const int maxSize = 10000;
	int pancakeArray[maxSize];
	int outputArray[maxSize];
	int i = 0, j = 0, a = 0;
	int countFlips = 0;
	char testChar;
	string inputStr;
	bool getChars = true;
	bool correctWayUp = false;
	clock_t startTime, currentTime;
	double elapsedSeconds;
	ifstream inputFilename;
	ofstream outputFilename;

	// initialise variables
	startTime = clock();
	for (a = 0; a < maxSize; a++) {
		pancakeArray[a] = - 1;              // missing value is -1
		outputArray[a] = -99;				// missing value is -99
	}

	// open input file
	inputFilename.open("SampleText.txt");
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
		j = 0;
		SLength = 0;
		for (a = 0; a < maxSize; a++) {
			if (pancakeArray[a] == -1) {
				break;
			}
			pancakeArray[a] = -1;              // missing value is -1
		}
		getChars = true;
		K = 0;
		while (getChars) {
			// read file into variables converting + and - into 1 and 0
			inputFilename.get(testChar);
			//cout << testChar;
			switch (testChar) {
				case '\n':
					getChars = false;
					break;
				case '+':
					pancakeArray[j] = 1;
					j++;
					SLength++;
					break;
				case '-':
					pancakeArray[j] = 0;
					j++;
					SLength++;
					break;
				case ' ':
					break;
				default:
					if (K > 0) {
						K *= 10;
					}
					K = K + int(testChar - 48);
			}
			
		}
		// start at left hand side and convert using NOT the first 0 into 1, repeating until finished or impossible
		countFlips =  0;
		for (j = 0; j <= SLength - K; j++) {
			if (pancakeArray[j] == 0) {
				// flip K pancakes
				for (a = 0; a < K; a++) {
					pancakeArray[a + j] = 1 - pancakeArray[a + j];
				}
				countFlips++;
			}
		}
		// check if they are all right way up
		correctWayUp = true;
		for (j = 0; j < SLength; j++) {
			if (pancakeArray[j] == 0) {
				correctWayUp = false;
				break;
			}
		}
		if (correctWayUp == true) {
			outputArray[i] = countFlips;
		}
		else {
			outputArray[i] = -1;
		}

		//// repeat from right hand side to see if results match
		//countFlips = 0;
		//for (j = SLength - 1; j >= K - 1; j--) {
		//	if (pancakeArray[j] == 0) {
		//		// flip K pancakes
		//		for (a = 0; a < K; a++) {
		//			pancakeArray[j - a] = 1 - pancakeArray[j - a];
		//		}
		//		countFlips++;
		//	}
		//}
		//// check if they are all right way up
		//correctWayUp = true;
		//for (j = 0; j < SLength; j++) {
		//	if (pancakeArray[j] == 0) {
		//		correctWayUp = false;
		//		break;
		//	}
		//}
		//if (correctWayUp == true) {
		//	if (outputArray[i] > countFlips || outputArray[i] == -1) {
		//		outputArray[i] = countFlips;
		//	}
		//}
	}
	
	inputFilename.close();

	// output results to file and screen (include timing on screen)
	outputFilename.open("Output Text.txt", ios::trunc);
	for (i = 0; i < T; i++) {
		if (outputArray[i] >= 0) {
			cout << "Case #" << i+1 << ": " << outputArray[i] << endl;
			outputFilename << "Case #" << i+1 << ": " << outputArray[i] << "\n";
		}
		else {
			cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
			outputFilename << "Case #" << i+1 << ": IMPOSSIBLE" << "\n";
		}
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

