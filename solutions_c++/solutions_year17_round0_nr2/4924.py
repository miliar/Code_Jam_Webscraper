#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <sstream>

#define FOR(i, a, b) for(int i = a; i < b; i++)
#define FORD(i, a, b) for(int i = a; i > b; i--)

using namespace std;

int T;
long long N;
string N_str;

int main()
{
    ifstream fin;
    fin.open("B-large.in");
    ofstream fout;
    fout.open("output-large.txt");

    fin >> T;

    FOR (i, 0, T) {
        fin >> N;
        stringstream ss;
        ss << N;
        N_str = ss.str();

        //Forward propagation until decrease in digit
        int j;
        for(j = 0; j < N_str.size() - 1; j++) {
            if (N_str[j] > N_str[j + 1]) {
                break;
            }
        }

        //Backpropagation
        //cout << "j = " << j << endl;
        if (j < N_str.size() - 1) {
            int k;
            for(k = j; k > 0; k--) {
                if (N_str[k - 1] < N_str[k]) {
                    break;
                }
            }

           // cout << "k = " << k << endl;
            N_str[k] = N_str[k] - 1; //implicitly using char numbers
            FOR(l, k + 1, N_str.size()) {
                N_str[l] = '9';
            }
        }

        istringstream iss(N_str);
        iss >> N;

        fout << "Case #" << i + 1 << ": " << N << endl;
    }

    return 0;
}
