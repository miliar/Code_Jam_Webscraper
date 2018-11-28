#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void rotate (string& S, int idx, int K)
{
    for (int i = 0; i < K; ++i) {
        S[i+idx] == '+' ? S[i+idx] = '-' : S[i+idx] = '+';
    }
}

int solve(string S, int K)
{
    if (K > S.size())
        return -1;

    int result = 0;
    for (int i = 0; i < S.size(); ++i) {
        //cout <<i<<" "<<S<<endl;
        if (S[i] == '-') {
            if (S.size() - i >= K) {
                rotate(S, i, K);
                ++result;
            } else {
                return -1;
            }
        }
    }
    return result;
}

int main()
{
    int T, K;
    string S;

    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fin >> T;
    for (int i = 0; i < T; ++i) {
        fin >> S >> K;
        int res =  solve(S, K);
        fout << "Case #" << i+1 <<": ";
        if (res == -1) {
            fout << "IMPOSSIBLE" << endl;
        } else {
            fout << res << endl;
        }
    }
    return 0;
}

