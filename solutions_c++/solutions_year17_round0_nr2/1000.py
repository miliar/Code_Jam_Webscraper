#define __LOCAL__
//#define __CUSTOM_INPUT__
//#define __DEBUG__
//#define __VERBOSE__
//#define __NO_OUTPUT__

#ifdef __DEBUG__
#define debugStream cout
#else
#define debugStream if(false) cout
#endif

#ifdef __VERBOSE__
#define verboseStream cout
#else
#define verboseStream if(false) cout
#endif

#ifdef __NO_OUTPUT__
#define outputStream if(false) cout
#else
#define outputStream cout
#endif

#ifndef __LOCAL__
#define inputStream cin
#endif

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <list>
#include <limits>
#include <algorithm>
#include <utility>
#include <array>
#include <unordered_map>
#include <map>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef long long ull;

int t;
vector<string> s;

void solve(int caseNumber, string s) {
    outputStream << "Case #" << caseNumber << ": ";
    for(int i=s.size()-2; i>=0; i--) {
        if(s[i] != '0' && s[i] > s[i+1]) {
            s[i]--;
            for(int j=i+1; j<s.size(); j++) {
                s[j] = '9';
            }
        }
    }
    for(char c : s) {
        if(c != '0') {
            outputStream << c;
        }
    }
    outputStream << endl;
}

int main(int argc, char** argv) {

#ifdef __LOCAL__
    string inputFilename = "input.txt";
    if(argc > 1) {
        inputFilename = argv[1];
    }
    ifstream inputStream = ifstream(inputFilename);
#endif

#ifdef __CUSTOM_INPUT__

#else
    inputStream >> t;
    s.resize(t);
    for(int i=0; i<t; i++) {
        inputStream >> s[i];
    }
#endif

    for(int i=0; i<t; i++) {
        solve(i+1, s[i]);
    }

}