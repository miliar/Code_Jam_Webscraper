#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
#include <queue>
#include <map>
#include <set>

#define FOR(i, a, b) for(int i = a; i < b; i++)

using namespace std;

int T, K;
string S;

string flip (string S, int start, int flip_length) {
    FOR (i, start, start + flip_length) {
        (S[i] == '-')? S[i] = '+' : S[i] = '-';
    }
    return S;
}

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("output-large.txt");

    fin >> T;

    FOR (i, 0, T) {
        bool possible = true;
        int num_flips = 0;
        fin >> S;
        fin >> K;
        FOR (j, 0, S.size() - K + 1) {
            if (S[j] == '-') {
                S = flip(S, j, K);
                num_flips++;
            }
        }
        FOR (j, S.size() - K + 1, S.size()) {
            if (S[j] == '-') {
                possible = false;
            }
        }

        if (possible) {
            fout << "Case #" << i + 1 << ": " << num_flips << endl;
        }
        else {
            fout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        }
    }

    return 0;
}
