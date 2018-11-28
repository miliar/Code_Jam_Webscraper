//  Tidy Number
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <unordered_map>
#include <vector>

using namespace std;


void readFile(string inFileName, vector<string>& caseList);
void doFunc(string& str);
void writeFile(string outFileName, const vector<string>& resultList);


int main() {
	const string inFileName = "B-small-attempt0.in";
	const string outFileName = "outfile.txt";
	
	vector<string> caseList;
    vector<string> resultList;
	
	readFile(inFileName, caseList);
	for (int i = 0; i < caseList.size(); i++) {
        doFunc(caseList[i]);
        resultList.push_back(caseList[i]);
	}
	writeFile(outFileName, resultList);	
	return 0;
}

void doFunc(string& str) {
    if (str.size() < 2) return;
    bool isTidy = false;
    while (!isTidy) {
        isTidy = true;
        for (int i = 0; i < str.size()-1; i++) {
            if (str[i+1] < str[i]) {
                isTidy = false;
                str[i++]--;
                while (i < str.size()) {
                    str[i++] = '9';
                }
            }
        }
    }
    for (int i = 0; i < str.size()-1; i++) {
        if (str[i] != '0') {
            str = str.substr(i, str.size()-i);
            break;
        }
    }
}

void readFile(string inFileName, vector<string>& caseList) {
	int caseNumber;
	string line;
	ifstream inFile;
	
	inFile.open(inFileName.c_str());
	getline(inFile, line);
	caseNumber = stoi(line);
	for (int i = 0; i < caseNumber; i++) {
        getline(inFile, line);
        caseList.push_back(line);
	}
	inFile.close();
}

void writeFile(string outFileName, const vector<string>& resultList) {
	ofstream outFile;
	outFile.open(outFileName.c_str());
	for (int i = 0; i < resultList.size(); i++) {
        outFile << "Case #" << i+1 << ": " << resultList[i] << '\n';
	}
	outFile.close();
}


