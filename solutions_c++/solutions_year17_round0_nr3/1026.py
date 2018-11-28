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
vector<ull> n;
vector<ull> k;

void solve(int caseNumber, ull n, ull k) {
    outputStream << "Case #" << caseNumber << ": ";
    map<ull, ull, greater<ull>> m;
    m[n] = 1;
    while(true) {
        pair<ull, ull> p = *m.begin();
        ull v = p.first;
        ull c = p.second;
        m.erase(v);
        if(k <= c) {
            if(v % 2 == 0) {
                outputStream << v/2 << " " << v/2-1;
            } else {
                outputStream << v/2 << " " << v/2;
            }
            break;
        }
        k -= c;
        if(v % 2 == 0) {
            m[v/2] = m[v/2] + c;
            m[v/2-1] = m[v/2-1] + c;
        } else {
            m[v/2] = m[v/2] + 2 * c;
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
    t = 100;
    n.resize(t);
    k.resize(t);
    for(int i=0; i<t; i++) {
        n[i] = 1000000000000000000LL;
        k[i] = 1000000000000000000LL - 10000000000000000LL * i;

    }
#else
    inputStream >> t;
    n.resize(t);
    k.resize(t);
    for(int i=0; i<t; i++) {
        inputStream >> n[i] >> k[i];
    }
#endif

    for(int i=0; i<t; i++) {
        solve(i+1, n[i], k[i]);
    }

}