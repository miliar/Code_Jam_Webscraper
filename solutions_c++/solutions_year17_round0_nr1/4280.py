/*
 * abeakkas
 * Google CodeJam 2017 - Qualification Round
 * Problem 1
 */
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

typedef long long ll;
typedef unsigned long long ull;

// #define pr pair<ll,ll>
// #define vpr vector<pair<ll,ll> >

// Code snippets:
// (int*)calloc(1000000, sizeof(int));
// (int*)malloc(1000000 * sizeof(int));
// cout << setprecision(20);

using namespace std; 

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cout << "Too few arguments" << std::endl;
        return 0;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    int T;
    fin >> T;
    char chs[1000];
    int l, p;
    char c;
    fin >> noskipws;
    for(int iT = 1; iT <= T; iT++) {
        l = 0;
        fin >> c;
        while(c != ' ') {
            chs[l++] = c;
            fin >> c;
        }
        fin >> p;
        bool flag = true;
        int n = 0;
        for (int i = 0; flag && i < l; i++) {
            if (chs[i] == '-') {
                n++;
                for (int j = 0; j < p; j++) {
                    if (i + j == l) {
                        flag = false;
                        break;
                    }
                    chs[i + j] = chs[i + j] == '-' ? '+' : '-';
                }
            }
        }
        fout << "Case #" << iT << ": ";
        if (flag) fout << n;
        else fout << "IMPOSSIBLE";
        fout << endl;
    }
	return 0;
}
