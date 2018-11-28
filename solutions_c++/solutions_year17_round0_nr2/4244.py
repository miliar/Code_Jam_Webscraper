/*
 * abeakkas
 * Google CodeJam 2017 - Qualification Round
 * Problem 2
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
    //fin >> noskipws;
    unsigned long long x;
    int dg[18];
    int l;
    for(int iT = 1; iT <= T; iT++) {
        fin >> x;
        l = 0;
        for (unsigned long long y = 1; y <= x; y *= 10) {
            dg[l++] = x % (10 * y) / y;
        }
        for (int i = l - 1; i >= 1; i--) {
           if (dg[i] > dg[i - 1]) {
               dg[i]--;
               if (i < l - 1) {
                   i++;
                   while (true) {
                       if (dg[i] > dg[i - 1]) {
                           dg[i]--;
                           i++;
                       } else break;
                   }
                   i--;
               }
               i--;
               while (i >= 0) {
                   dg[i] = 9;
                   i--;
               }
               break;
           }
        }
        fout << "Case #" << iT << ": ";
        if (dg[l - 1] != 0) fout << dg[l - 1];
        for (int i = l - 2; i >= 0; i--) {
            fout << dg[i];
        }
        fout << endl;
    }
	return 0;
}
