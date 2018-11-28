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


void readFile(string inFileName, vector<int>& dList, vector<vector<int> >& kList, vector<vector<int> >& sList);
double doFunc(int d, const vector<int>& k, const vector<int>& s);
void writeFile(string outFileName, vector<double>& resultList);


int main() {
	const string inFileName = "A-large.in";
	const string outFileName = "outfileAlarge.txt";
	
    vector<int> dList;
    vector<vector<int> > kList;
    vector<vector<int> > sList;
    vector<double> resultList;
	
	readFile(inFileName, dList, kList, sList);
	for (int i = 0; i < dList.size(); i++) {
        resultList.push_back(doFunc(dList[i], kList[i], sList[i]));
	}
	writeFile(outFileName, resultList);	
	return 0;
}

double doFunc(int d, const vector<int>& k, const vector<int>& s) {
    double tmax = 0.0;
    double res;
    for (int i = 0; i < k.size(); i++) {
        double t = double(d - k[i])/double(s[i]);
        tmax = max(tmax, t);
    }
    res = double(d) / tmax;
    return res;
}

void readFile(string inFileName, vector<int>& dList, vector<vector<int> >& kList, vector<vector<int> >& sList) {
	int caseNumber;
	string line;
	ifstream inFile;
	
	inFile.open(inFileName.c_str());
	getline(inFile, line);
	caseNumber = stoi(line);
	for (int i = 0; i < caseNumber; i++) {
        getline(inFile, line);
        
        int pos = line.find(' ');
        int D = stoi(line.substr(0, pos));
        int N = stoi(line.substr(pos+1, line.size() - pos));
        vector<int> singleK;
        vector<int> singleS;
        dList.push_back(D);
        
        for (int j = 0; j < N; j++) {
            getline(inFile, line);
            int posJ = line.find(' ');
            int k = stoi(line.substr(0, posJ));
            int s = stoi(line.substr(posJ+1, line.size() - posJ));
            singleK.push_back(k);
            singleS.push_back(s);
        }
        
        kList.push_back(singleK);
        sList.push_back(singleS);
	}
	inFile.close();
}

void writeFile(string outFileName, vector<double>& resultList) {
	ofstream outFile;
    
	outFile.open(outFileName.c_str());
	for (int i = 0; i < resultList.size(); i++) {
        outFile << "Case #" << i+1 << ": " << setiosflags(ios::fixed) << setprecision(6) << resultList[i] << '\n';
	}
	outFile.close();
}


