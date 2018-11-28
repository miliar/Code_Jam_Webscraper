/*
 * abeakkas
 * Google CodeJam 2017 - Round 1B
 * Problem B
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

void solve(ofstream &fout, int n1, int n2, int n3, int m1, int m2, int m3, char c1, char c2, char c3, char mc1, char mc2, char mc3) {
    while (n1) {
        fout << c1;
        n1--;
        if (n2 > n3) {
            fout << c2;
            n2--;
            if (n1 == 0 && n3 > 0) {
                fout << c3;
                n3--;
            }
        } else {
            fout << c3;
            n3--;
        }
    }
    while (n2) {
        fout << c2;
        n2--;
        if (n3 > 0) {
            fout << c3;
            n3--;
        }
    }
}
 

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
    for(int iT = 1; iT <= T; iT++) {
        int N, R, O, Y, G, B, V;
        fin >> N >> R >> O >> Y >> G >> B >> V;

        fout << "Case #" << iT << ": ";
        if (R * 2 > N || Y * 2 > N || B * 2 > N) {
            fout << "IMPOSSIBLE";
        } else if (R >= Y && R >= B) {
            solve(fout, R, Y, B, G, V, O, 'R', 'Y', 'B', 'G', 'V', 'O'); 
        } else if (Y > R && Y >= B) {
            solve(fout, Y, R, B, V, G, O, 'Y', 'R', 'B', 'V', 'G', 'O'); 
        } else {
            solve(fout, B, Y, R, O, V, G, 'B', 'Y', 'R', 'O', 'V', 'G'); 
        }
        fout << endl;
    }
	return 0;
}
