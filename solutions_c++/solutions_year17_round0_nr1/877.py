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

bool run(
	string S,
	int flipsize, 
	int& flips) 
{
	if (flipsize > S.size() && S[0] == '-') return false;
	
	for(int i = 0; i <= S.size()-flipsize; ++i) {
		if (S[i] == '+') continue;
		++flips;
		for (int j = i; j < i + flipsize; ++j) {
			S[j] = ((S[j] == '-') ? '+' : '-');
		}
	}
	for (int i = S.size()-flipsize + 1; i < S.size(); ++i) {
		if (S[i] == '-') return false;
	}

	return true;
}

void test() {
	string S;
	cin >> S;

	int n;
	cin >> n;

	int F = 0;
	bool result = run(S,n,F);

	if (!result) {
		cout << "IMPOSSIBLE";
	} else {
		cout << F;
	}
	
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
