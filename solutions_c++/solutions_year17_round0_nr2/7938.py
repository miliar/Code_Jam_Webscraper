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
    	if (S.length() == 1) {
    		cout << "Case #" << i << ": " << S << "\n";
    		continue;
		}
    	int wall = S.length() - 1;
    	for (int j = S.length() - 1; j > 0; --j) {
    		if (S[j] < S[j - 1]) {
    			wall = j - 1;
    			S[wall] = S[wall] - 1;
			}
		}
		if (wall != S.length() - 1) {
			for (int j = wall + 1; j < S.length(); ++j) {
				S[j] = '9';
			}
			int k = 0;
			while (S[k] == '0') {
				k += 1;
			}
			S = S.substr(k);
		}
    	cout << "Case #" << i << ": " << S << "\n";
	}
    return 0;
}
