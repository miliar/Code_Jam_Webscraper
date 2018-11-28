/*
 * abeakkas
 * Google CodeJam 2017 - Round 1B
 * Problem C
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
    int hrange[100];
    int hspeed[100];
    int dists[100][100];
    int tdists[100][100]; // Graph distance
    double ndists[100][100];

    //fin >> noskipws;
    for(int iT = 1; iT <= T; iT++) {
        int N, Q;
        fin >> N >> Q;
        for (int i = 0; i < N; i++) {
            fin >> hrange[i] >> hspeed[i];
        }
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) {
            fin >> dists[i][j];
        }

        // Floyd Warshall
        for (int i = 0; i < N; i++) {
            tdists[i][i] = 0;
        }
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) {
            if (i != j) {
                tdists[i][j] = dists[i][j];
            }
        }
        for (int k = 0; k < N; k++) for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) {
            if (tdists[i][k] > 0 && tdists[k][j] > 0 && (tdists[i][j] > tdists[i][k] + tdists[k][j] || tdists[i][j] < 0)) {
                tdists[i][j] = tdists[i][k] + tdists[k][j];
            }
        }
/*
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) cout << tdists[i][j] << " ";
            cout << endl;
        }
*/      
        for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) {
            if (tdists[i][j] > 0 && hrange[i] >= tdists[i][j]) {
                ndists[i][j] = (double)tdists[i][j] / hspeed[i];
            } else ndists[i][j] = -1;
        }
/*
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) cout << ndists[i][j] << " ";
            cout << endl;
        }
*/
        // Floyd Warshall 2
        for (int i = 0; i < N; i++) {
            ndists[i][i] = 0;
        }
        for (int k = 0; k < N; k++) for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) {
            if (ndists[i][k] > 0 && ndists[k][j] > 0 && (ndists[i][j] > ndists[i][k] + ndists[k][j] || ndists[i][j] < 0)) {
                ndists[i][j] = ndists[i][k] + ndists[k][j];
            }
        }
/* 
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) cout << ndists[i][j] << " ";
            cout << endl;
        }
        cout << endl;
*/
        fout << "Case #" << iT << ":";
        for (int i = 0; i < Q; i++) {
            int f, t;
            fin >> f >> t;
            fout << " " << ndists[f - 1][t - 1];
        }
        fout << endl;
    }
	return 0;
}
