#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <string>
#include <set>
#include <deque>
#include <cctype>
#include <bitset>
#include <regex>

using namespace std;

#define For(i, n) for(int (i) = 0; (i) < (n); (i)++)

void solve(int t){
	double d, n, k, s;
	cin >> d >> n;
	double last = -1;
	For(i, n){
		cin >> k >> s;
		last = max(last,(double)(d - k) / s);
	}

	printf("Case #%d: %.9f\n", t+1, d / last);

	return;
}

int main(){
	int T;
	cin >> T;
	For(i, T) solve(i);
	return 0;
}
