/*
Input

The first line of the input gives the number of test cases, T.

T test cases follow.

Each consists of one line with a string S and an integer K.

S represents the row of pancakes: each of its characters is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up).



Output

For each test case, output one line containing
Case #x: y
, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it.


Limits

1 ≤ T ≤ 100.
Every character in S is either + or -.
2 ≤ K ≤ length of S.
*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <string.h>
#include <float.h>

#include <iostream>
#include <fstream>

typedef struct {
	double t;
	double overhang;
	char facing_up;
	} intersection;


int main(int argc, char** argv) {
	int T, K, ncase;
	ncase = 0;
	std::string S;
	std::string line;
	//std::ifstream myfile ("a_test.txt");
	std::ifstream myfile ("A-large.in");
	if(myfile.is_open()) {
		//getline(myfile, line);
		myfile >> T;
		//std::cout << "T : " << T << std::endl;
		getline(myfile, line);
		while(getline(myfile, S, ' ')) {
			ncase++;
			int l = 0;
			while((S[l] == '+') || (S[l] == '-')) l++;
			//std::cout << std::endl;
			//std::cout << S << std::endl;
			////std::cout << "S-size : " << l << std::endl;
			myfile >> K;
			//std::cout << "K : " << K << std::endl;
			getline(myfile, line);
			////std::cout << line << std::endl;
			int inversions = 0;
			/*
			char current = S[l-1];
			for(int i = 1; i < K; i++) {
				if(S[l-1-i] == current) continue;
				current = S[l-1-i];
				inversions++;
				}
			*/
			bool possible = (inversions <= 1);
			if(!possible) {
				//std::cout << "NOT POSSIBLE" << std::endl;
				std::cout << "Case #" << ncase << ": IMPOSSIBLE" << std::endl;
				}
			else {
				//std::cout << "poss" << std::endl;
				int moves = 0;

				/*
				if(inversions == 1) {
					inversions = 0;
					current = S[l-1];
					for(int i = 1; i < K; i++) {
						if(S[l-1-i] == current) continue;
						for(int j = 0; j < K; j++) S[l-1-i-j] = (S[l-1-i-j] == '+') ? '-' : '+';
						moves++;
						break;
						}
					}
				*/

				for(int i = 0; i < l; i++) {
					if(S[i] == '+') continue;
					moves++;
					if(i+K-1 >= l) {
						//std::cout << "WARNING!!!!" << std::endl;
						possible = false;
						break;
						}
					for(int j = 0; j < K; j++) S[i+j] = (S[i+j] == '+') ? '-' : '+';
					}
				//std::cout << "moves : " << moves << std::endl;
				if(possible) std::cout << "Case #" << ncase << ": " << moves << std::endl;
				else std::cout << "Case #" << ncase << ": IMPOSSIBLE" << std::endl;
				}
			}
		myfile.close();
		}
	else std::cout << "Unable to open file" << std::endl;
	return 0;
	}
