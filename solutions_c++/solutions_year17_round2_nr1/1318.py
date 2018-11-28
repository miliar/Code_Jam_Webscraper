/*
 * abeakkas
 * Google CodeJam 2017 - Round 1B
 * Problem A
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
    fout << setprecision(20);
    int T;
    fin >> T;
    //fin >> noskipws;
    for(int iT = 1; iT <= T; iT++) {
        int N, D;
        fin >> D >> N;
        double tmax = 0;
        for (int i = 0; i < N; i++) {
            int K, S;
            fin >> K >> S;
            double t = (double)(D - K) / S;
            if (t > tmax) tmax = t;
        }
        fout << "Case #" << iT << ": ";
        fout << D / tmax;
        fout << endl;
    }
	return 0;
}
