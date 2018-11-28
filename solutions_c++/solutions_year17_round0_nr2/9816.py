#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>

using namespace std;

string get_dig(int n) {
	string ret = "";
	while(n) {
		ret += (char)('0' + (n % 10));
		n /= 10;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		long n;
		cin >> n;
		long ans = 0;
		for(long i = n; i >= 0; --i) {
			bool satisfy = true;
			string dig = get_dig(i);
			for(long j = 0; j < dig.size() - 1; ++j) {
				if(dig[j+1] < dig[j]) {
					satisfy = false;
					break;
				}
			}
			if(satisfy) {
				ans = i;
				break;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}