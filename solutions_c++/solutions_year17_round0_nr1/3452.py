//  Oversized Pancake Flipper
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


void readFile(string inFileName, vector<pair<string,int> >& caseList);
int doFunc(string& str, int siz);
void writeFile(string outFileName, const vector<int>& resultList);


int main() {
	const string inFileName = "A-large.in";
	const string outFileName = "outfileLarge.txt";
	
	vector<pair<string,int> > caseList;
    vector<int> resultList;
	
	readFile(inFileName, caseList);
	for (int i = 0; i < caseList.size(); i++) {
        resultList.push_back(doFunc(caseList[i].first, caseList[i].second));
	}
//	testFile(caseList, spellBookList, resultList);
	writeFile(outFileName, resultList);	
	return 0;
}

int doFunc(string& str, int siz) {
    int res = 0;
    if (str.empty()) return -1;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] != '+') {
            if (i + siz - 1 >= str.size()) return -1;
            for (int j = 0; j < siz; j++) {
                str[i+j] = str[i+j] == '+' ? '-' : '+';
            }
            res++;
        }
    }
    return res;
}

void readFile(string inFileName, vector<pair<string,int> >& caseList) {
	int caseNumber;
	string line;
	ifstream inFile;
	
	inFile.open(inFileName.c_str());
	getline(inFile, line);
	caseNumber = stoi(line);
	for (int i = 0; i < caseNumber; i++) {
        getline(inFile, line);
        
        int pos = line.find(' ');
        string s = line.substr(0, pos);
        int siz = stoi(line.substr(pos+1, line.size() - pos));
        
        caseList.push_back(make_pair(s, siz));
	}
	inFile.close();
}

void writeFile(string outFileName, const vector<int>& resultList) {
	ofstream outFile;
    
	outFile.open(outFileName.c_str());
	for (int i = 0; i < resultList.size(); i++) {
        if (resultList[i] >= 0) {
            outFile << "Case #" << i+1 << ": " << resultList[i] << '\n';
        }
        else {
            outFile << "Case #" << i+1 << ": " << "IMPOSSIBLE\n";
        }
	}
	outFile.close();
}


