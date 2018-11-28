//  Bathroom Stalls
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


void readFile(string inFileName, vector<pair<long, long> >& caseList);
pair<long, long> doFunc(long N, long K);
void writeFile(string outFileName, const vector<pair<long, long> >& resultList);


int main() {
	const string inFileName = "C-large.in";
	const string outFileName = "outfileLarge.txt";
	
	vector<pair<long, long> > caseList;
    vector<pair<long, long> > resultList;
	
	readFile(inFileName, caseList);
	for (int i = 0; i < caseList.size(); i++) {
        pair<long, long> res = doFunc(caseList[i].first, caseList[i].second);
        resultList.push_back(res);
	}
	writeFile(outFileName, resultList);	
	return 0;
}

pair<long, long> doFunc(long N, long K) {
    long parts = 1;
    long divSize;
    for (; (parts << 1) <= K; parts <<= 1);
    if (K - parts < (N - (parts - 1)) % parts) {
        divSize = (N - (parts - 1)) / parts + 1;
    }
    else {
        divSize = (N - (parts - 1)) / parts;
    }
    return make_pair(divSize / 2, max(divSize / 2 - ((divSize&1)^1) , 0L));
}

void readFile(string inFileName, vector<pair<long, long> >& caseList) {
	int caseNumber;
	string line;
	ifstream inFile;
	
	inFile.open(inFileName.c_str());
	getline(inFile, line);
	caseNumber = stoi(line);
	for (int i = 0; i < caseNumber; i++) {
        getline(inFile, line);
        
        int pos = line.find(' ');
        long N = stol(line.substr(0, pos));
        long K = stol(line.substr(pos+1, line.size() - pos));
        
        caseList.push_back(make_pair(N, K));
	}
	inFile.close();
}

void writeFile(string outFileName, const vector<pair<long, long> >& resultList) {
	ofstream outFile;
    
	outFile.open(outFileName.c_str());
	for (int i = 0; i < resultList.size(); i++) {
        outFile << "Case #" << i+1 << ": " << resultList[i].first 
                << ' ' << resultList[i].second << '\n';
	}
	outFile.close();
}


