// CodeJamQualificationBTidyNumbers.cpp : Defines the entry point for the console application.
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

	// declare additional variables
	const int maxNumberSize = 20;
	const int maxCountSize = 10000;
	int digitArray[maxNumberSize];
	int digitArrayRev[maxNumberSize];
	int outputArray[maxCountSize];
	long long int i = 0, j = 0, k = 0;
	int NLength = 0;
	char testChar;
	string inputStr;
	bool getChars = true;
	bool tidyNumber = false;
	clock_t startTime, currentTime;
	double elapsedSeconds;
	ifstream inputFilename;
	ofstream outputFilename;

	// initialise variables
	startTime = clock();
	for (i = 0; i < maxNumberSize; i++) {
		digitArray[i] = 0;
		digitArrayRev[i] = 0;
	}
	for (i = 0; i < maxCountSize; i++) {
		outputArray[i] = -99;				// missing value is -99
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
		for (j = 0; j < maxNumberSize; j++) {
			digitArray[j] = 0;
			digitArrayRev[j] = 0;
		}
		getChars = true;
		k = 0;
		NLength = 0;
		N = 0;
		while (getChars) {
			// read file into digitArray
			inputFilename.get(testChar);
			//cout << testChar;
			switch (testChar) {
			case '\n':
				getChars = false;
				break;
			case ' ':
				break;
			default:
				digitArrayRev[k] = int(testChar - 48);
				N *= 10;
				N += digitArrayRev[k];
				NLength++;
				k++;
			}

		}
		//need to reverse the digits
		k = 0;
		for (j = NLength - 1; j >= 0; j--) {
			digitArray[k] = digitArrayRev[j];
			k++;
		}
		// start at N and work backwards
		for (j = N; j > 0; j--) {
			tidyNumber = true;
			for (k = 1; k < NLength; k++) {
				if (digitArray[k] > digitArray[k - 1]) {
					tidyNumber = false;
					break;
				}
			}
			if (tidyNumber == true) {
				// found one
				break;
			}
			else {
				// do a check for strange values
				if (digitArray[0] == 0 && digitArray[NLength - 1] == 1 && digitArray[NLength - 2] == 1) {
					digitArray[NLength - 2] = 0;
				}
				else {
					digitArray[0] = digitArray[0] - 1;
					if (digitArray[0] < 0) {
						digitArray[0] = 9;
						digitArray[1] = digitArray[1] - 1;
						if (digitArray[1] < 0) {
							digitArray[1] = 9;
							digitArray[2] = digitArray[2] - 1;
							if (digitArray[2] < 0) {
								digitArray[2] = 9;
								digitArray[3] = digitArray[3] - 1;
								if (digitArray[3] < 0) {
									digitArray[3] = 9;
									digitArray[4] = digitArray[4] - 1;
									if (digitArray[4] < 0) {
										digitArray[4] = 9;
										digitArray[5] = digitArray[5] - 1;
										if (digitArray[5] < 0) {
											digitArray[5] = 9;
											digitArray[6] = digitArray[6] - 1;
											if (digitArray[6] < 0) {
												digitArray[6] = 9;
												digitArray[7] = digitArray[7] - 1;
												if (digitArray[7] < 0) {
													digitArray[7] = 9;
													digitArray[8] = digitArray[8] - 1;
													if (digitArray[8] < 0) {
														digitArray[8] = 9;
														digitArray[9] = digitArray[9] - 1;
														if (digitArray[9] < 0) {
															digitArray[9] = 9;
															digitArray[10] = digitArray[10] - 1;
															if (digitArray[10] < 0) {
																digitArray[10] = 9;
																digitArray[11] = digitArray[11] - 1;
																if (digitArray[11] < 0) {
																	digitArray[11] = 9;
																	digitArray[12] = digitArray[12] - 1;
																	if (digitArray[12] < 0) {
																		digitArray[12] = 9;
																		digitArray[13] = digitArray[13] - 1;
																		if (digitArray[13] < 0) {
																			digitArray[13] = 9;
																			digitArray[14] = digitArray[14] - 1;
																			if (digitArray[14] < 0) {
																				digitArray[14] = 9;
																				digitArray[15] = digitArray[15] - 1;
																				if (digitArray[15] < 0) {
																					digitArray[15] = 9;
																					digitArray[16] = digitArray[16] - 1;
																					if (digitArray[16] < 0) {
																						digitArray[16] = 9;
																						digitArray[17] = digitArray[17] - 1;
																						if (digitArray[17] < 0) {
																							digitArray[17] = 9;
																							digitArray[18] = digitArray[18] - 1;
																							if (digitArray[18] < 0) {
																								digitArray[18] = 9;
																								digitArray[19] = digitArray[19] - 1;
																								if (digitArray[19] < 0) {
																									digitArray[19] = 9;
																								}
																							}
																						}
																					}
																				}
																			}
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
		// output the last j tested
		outputArray[i] = j;
	}

	inputFilename.close();

	// output results to file and screen (include timing on screen)
	outputFilename.open("Output Text.txt", ios::trunc);
	for (i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": " << outputArray[i] << endl;
		outputFilename << "Case #" << i + 1 << ": " << outputArray[i] << "\n";
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


