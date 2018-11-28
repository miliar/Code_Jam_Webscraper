#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <functional>
#include <cassert>
#include <map>
#include <set>
#include <list>
#include <iostream>

using namespace std;
typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const lli LINF = 0x3f3f3f3f3f3f3f3f;

//#define _LOCAL_DEBUG_
#ifdef _LOCAL_DEBUG_
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 
#endif

void clear() {
}

string toStr(lli x) {
	string res;
	while(x) {
		res.push_back('0' + x % 10);
		x /= 10;
	}
	return res;
}

void solve(int t) {
	lli n;
	cin >> n;
	string s = toStr(n);
	for (int i = s.size() - 2; i >= 0; i--)
		if (s[i] < s[i + 1]) {
			char c = s[i + 1];
			int lastIdx;
			for (lastIdx = i + 1; lastIdx + 1 < s.size() && s[lastIdx + 1] == c; lastIdx++);
			s[lastIdx]--;
			for (int j = 0; j < lastIdx; j++) s[j] = '9';
			break;
		}

	while (s.size() > 1 && s[s.size() - 1] == '0') s.pop_back();
	reverse(s.begin(), s.end());
	cout << "Case #" << t << ": " << s << endl;
}

int main() {
#ifdef _LOCAL_VAN
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int it = 0; it < t; it++) {
		clear();
		solve(it + 1);
	}
	return 0;
}