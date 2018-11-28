#include <iostream>
#include <cstring>
#include <cstdlib>
#include <sstream>

using namespace std;


void solve_case(string N, int case_num) {
  	stringstream answer;
    if (N.size() == 1) {
        answer << N;
    } else {
        int last = N[N.size()-1];
        for (int i = N.size()-2; i >= 0; --i) {
            int next = N[i];
            if (next > last) {
                N[i] -= 1;
                for (int j = i+1; j < N.size(); ++j) {
                    N[j] = '9';
                }
            }
            last = N[i];
        }
        if (N[0] == '0') {
            answer << N.substr(1);
        } else {
            answer << N;
        }
    }
  	cout << "Case #" << case_num+1 << ": " << answer.str() << "\n";
}


int main() {
  	int T;
  	cin >> T;
  	for (int i = 0; i < T; i++) {
  		cerr << i << "\n";

        string N;
        cin >> N;
   	 	solve_case(N, i);
  	}
    return 0;
}
