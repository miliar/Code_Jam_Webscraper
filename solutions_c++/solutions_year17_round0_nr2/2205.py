#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

int T;


int main() {
	ifstream fin("B-large.in", ifstream::in);
	ofstream fout("result.out", ofstream::out);
	fin >> T;
	//cin >> T;
	string N;
	vector<char> result;
	for(int i = 0; i < T; ++i) {
		fin >> N;
        //cin >> N;
        cout << N << endl;  // for debug
        result.clear();
        bool borrow = false;
        for (int j = N.size() - 1; j >= 0; --j) {
            if (borrow) {
                if (N[j] > '0') {
                    N[j] -= 1;
                    borrow = false;
                } else {
                    result.push_back('9');
                    continue;
                }
            }
            if (j == 0) {
                if (N[j] > '0')
                    result.push_back(N[j]);
                break;
            }
            if (N[j] >= N[j - 1]) {
                result.push_back(N[j]);
            } else {
                borrow = true;
                for (int k = 0; k < result.size(); ++k) {
                    result[k] = '9';
                }
                result.push_back('9');
            }
        }
        fout << "Case #" << (i+1) << ": ";
        for (int j = result.size() - 1; j >= 0; --j) {
            fout << result[j];
        }
        fout << endl;
        cout << "Case #" << (i+1) << ": ";
        for (int j = result.size() - 1; j >= 0; --j) {
            cout << result[j];
        }
        cout << endl;
	}

	return 0;
}
