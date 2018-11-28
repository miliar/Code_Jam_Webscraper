/* ***********************************************
 	Author        : luckcul
 	Mail          : tyfdream@gmail.com
 	Created Time  : 2017-04-08 17:13:05
 	Problem       : problem
************************************************ */
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>
using namespace std;
#define INF 1000000000
typedef long long LL;
int t;
char s[55];
LL n;
LL sol(){
	int len = strlen(s);
	int index = -1;
	for(int i = 0; i < len-1; i++) {
		if(s[i] > s[i+1]) {
			index = i;
			break;
		}
	}
	if(index != -1) {
		while(1) {
			if(index == 0) {
				break;
			}
			else {
				if(s[index] > s[index-1]){
					break;
				}
				else index --;
			}
		}
		s[index] --;
		for(int i = index +1; i < len; i++) {
			s[i] = '9';
		}
	}

	n = 0;
	LL base = 1;
	for(int i = len-1; i >= 0; i-- ) {
		n += base * (s[i] - '0');
		base *= (LL)10;
	}
	return n;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif // ONLINE_JUDGE
	scanf("%d", &t);
	for(int ti = 0; ti < t; ti++) {
		// scanf("%lld", &n);
		scanf("%s", s);
		LL ans = sol();

		printf("Case #%d: ", ti+1);
		cout<<ans<<endl;
	}

	return 0;
}
