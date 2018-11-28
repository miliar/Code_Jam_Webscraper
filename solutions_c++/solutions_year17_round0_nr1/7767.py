
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <stdio.h>
#include <string.h>

using namespace std;

ifstream input("A-large.in");
ofstream output("A-large.out");

bool verifyInput() {
    if (!input.is_open()) {
    	cout << "input file not open " << endl;
    	return false;
    }
	if (!input.good()) {
		cout << "input not good " << endl;
		return false;
	}
	return true;
}

int main() {

	string line;
    int lineNumber = 1;

    if (!verifyInput()) {
    	return 0;
    }
	// jump over first line number of test cases
	getline(input, line);
	int flips = 0;
	//output << "Output\n\n";
	int K=0;
	int latestK=0;
	while(!input.eof())
	{
		getline(input, line);
		if(line == "") break;


		for (int k=0; k<(int)line.length(); k++) {
			if (line.at(k) == '+' || line.at(k) == '-' || line.at(k) == ' ')
				continue;
			else {
				string strK = line.substr(k,line.length()-1);
				K = atoi(strK.c_str());
				latestK = k;
				break;
			}
		}
		string panc = line.substr(0, line.length() - 2 - (line.length() - latestK -1));
		int nPancakes = panc.length();
		flips = 0;

		for (int i=0; i+K <= nPancakes; i++) {
			if (panc.at(i) == '-') {
				for (int j=0; j<K; j++) {
					if (j == K-1)
						flips++;
					char current = panc.at(i+j);
					if (current == '+') {
						panc.replace(i+j, 1, "-");
					}
					else {
						panc.replace(i+j, 1, "+");
					}
				}
			}
		}

		int a = K;
		bool impossible = false;
		for (a=1; a<=K; a++) {
			if (panc.at(nPancakes-a) == '-') {
				impossible = true;
			}
		}

		// check the end
		if (impossible) {
			output << "Case #" << lineNumber << ": IMPOSSIBLE" << endl;
		}
		else {
			output << "Case #" << lineNumber << ": " << flips << endl;

		}
		lineNumber++;
	}
	return 0;
}
