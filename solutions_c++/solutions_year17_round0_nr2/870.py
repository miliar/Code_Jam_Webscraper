#include <cfloat>
#include <climits>
#include <cmath>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

string run(string S)
{
	if (S.size() == 1) return S;
	for (int i = S.size()-1; i > 0; i--) {
		if (S[i-1] > S[i]) {
			for (int j = i; j < S.size(); ++j) S[j] = '9';
			S[i-1] = S[i-1] - 1;
		}
	}
	for (int i = 0; i < S.size()-1; i++) {
		if (S[i] != '0') {
			if (i > 0) {
				S.erase(0,i);
			}
			break;
		}
	}
	return S;
}

void test() {
	string S;
	cin >> S;
	string result = run(S);
	cout << result;	
}	

int main() {
	int T;
	cin >> T;
	for(int i = 1; i<=T; i++) {
		cout << "Case #" << i << ": ";
		test();	
		cout << endl;
	}
	return 0;
}
