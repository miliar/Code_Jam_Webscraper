#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;

typedef long long LL;
#define pb push_back

int main () {
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; ++tt){
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for(int i = 0; i < s.length(); ++i){
			if(s[i] == '-'){
				if(i+k-1 >= s.length()){
					ans = -1; break;
				}
				++ans;
				for(int j = 0; j < k; ++j) s[i+j] = s[i+j]=='+' ? '-' : '+';
			}
		}
		printf("Case #%d: ", tt);
		if(~ans) cout << ans <<endl;
		else puts("IMPOSSIBLE");
	}
}