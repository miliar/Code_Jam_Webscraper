#include <iostream>
#include <string>

#define cin std::cin
#define cout std::cout
#define string std::string

int main () {
//    freopen("large_input.txt", "rt", stdin);
//    freopen("large_output.txt", "wt", stdout);
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
    	string S;
    	cin >> S;
    	int K;
    	cin >> K;
    	bool isPossible = true;
    	int count = 0;
    	for (int j = 0; j < S.length(); ++j) {
    		if (S[j] == '-') {
    			if (j + K > S.length()) {
    				isPossible = false;
    				break;
				}
    			for (int k = j; k < j + K; ++k) {
    				if (S[k] == '-') S[k] = '+';
    				else S[k] = '-';
				}
				count += 1;
			}
		}
		if (!isPossible) cout << "Case #" << i << ": IMPOSSIBLE\n";
		else cout << "Case #" << i << ": " << count << "\n";
	}
    return 0;
}
