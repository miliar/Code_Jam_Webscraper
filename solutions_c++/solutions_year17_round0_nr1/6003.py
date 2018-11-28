#include <iostream>
#include <cstring>
#include <cstdlib>
#include <sstream>

using namespace std;


void solve_case(string S, int K, int case_num) {
  	stringstream answer;
    int l = S.size();
    int counter = 0;
    while (l >= K) {
        --l;
        if (S[l] == '-') {
            for (int j = 0; j < K; ++j) {
                char c = S[l-j];
                S[l-j] = c == '+' ? '-' : '+';
            }
            ++counter;
        }
    }
    bool done = true;
    for (int i = 0; i < K; ++i) {
        if (S[i] == '-') done = false;
    }

    if (done) answer << counter;
    else answer << "IMPOSSIBLE";

  	cout << "Case #" << case_num+1 << ": " << answer.str() << "\n";
}


int main() {
  	int T;
  	cin >> T;
  	for (int i = 0; i < T; i++) {
  		cerr << i << "\n";

        string S;
        int K;
        cin >> S >> K;
   	 	solve_case(S, K, i);
  	}
    return 0;
}
