#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

using namespace std;

int T;


int main() {
	ifstream fin("A-large.in", ifstream::in);
	ofstream fout("result.out", ofstream::out);
	fin >> T;
	//cin >> T;
	string S;
	int K;
	for(int i = 0; i < T; ++i) {
		fin >> S >> K;
        //cin >> S >> K;
        cout << S << " " << K << endl;
        int count = 0;
        int j = 0;
        for (; j + K <= S.size(); ++j) {
            if (S[j] == '-') {
                for (int k = 0; k < K; ++k) {
                    S[j + k] = (S[j + k] == '-') ? '+' : '-';
                }
                ++count;
            }
        }
        for (; j < S.size(); ++j) {
            if (S[j] == '-') {
                count = -1;
                break;
            }
        }
        if (count < 0) {
            cout << "Case #" << (i+1) << ": " <<  "IMPOSSIBLE" << endl;
            fout << "Case #" << (i+1) << ": " <<  "IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << (i+1) << ": " <<  count << endl;
            fout << "Case #" << (i+1) << ": " <<  count << endl;
        }
	}

	return 0;
}
