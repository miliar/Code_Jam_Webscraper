/*
_____/\\\\\\\________________________/\\\\\\\\\____________/\\\\\\\\\_
___/\\\/////\\\____________________/\\\\\\\\\\\\\_______/\\\////////__
__/\\\____\//\\\__________________/\\\/////////\\\____/\\\/___________
_\/\\\_____\/\\\___/\\\____/\\\__\/\\\_______\/\\\___/\\\_____________
_\/\\\_____\/\\\__\///\\\/\\\/___\/\\\\\\\\\\\\\\\__\/\\\_____________
_\/\\\_____\/\\\____\///\\\/_____\/\\\/////////\\\__\//\\\____________
_\//\\\____/\\\______/\\\/\\\____\/\\\_______\/\\\___\///\\\__________
__\///\\\\\\\/_____/\\\/\///\\\__\/\\\_______\/\\\_____\////\\\\\\\\\_
____\///////______\///____\///___\///________\///_________\/////////__
*/
#include <iostream>	
#include <time.h>
#include <vector>
#include <stdio.h>
#include <memory.h>
#include <string>
#include <string.h>
#include <cstring>
#include <map>
#include <algorithm>
#include <bitset>
#include <queue>
#include <set>
#include <time.h>
#include <assert.h>
#include <sstream>
//#include <unordered_map>
#include <bitset>
#include <utility>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <numeric>
#include <math.h>
#include <cmath>
#include <complex>
#include <numeric>
#include <iomanip>
#if !ONLINE_JUDGE
#include "inc.h"
#endif
using namespace std;
typedef long long ll;

int n;
ll mx = 0, x;
char s[20];
void calc(int at, ll num,int last) {
	if(at == n) {
		if(num>0 && num <= x)
			mx = max(mx, num);
		return;
	}
	calc(at + 1, num, last);
	for(int i = last; i < 10; ++i)
		calc(at + 1, num * 10 + i, i);
}


int main() {
#if !ONLINE_JUDGE
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);
	decTime;
#endif

	int t;
	scanf("%d", &t);
	for(int T = 1; T <= t; ++T) {
		scanf("%s", s);
		n = strlen(s);
		string res = "";
		for(int i = 0; i < n; ++i) {
			bool flag = true;
			for(int j = i + 1; j < n && flag; ++j) {
				if(s[i] != s[j] && s[j] > s[i])
					break;
				else if(s[i] != s[j])
					flag = false;
			}
			if(flag) {
				res += s[i];
				while(i + 1 < n && s[i + 1] == s[i])
					res += s[i], ++i;
			} else {
				if(s[i] != '1')
					res += s[i] - 1;
				for(int j = i + 1; j < n; ++j)
					res += '9';
				break;
			}
		}
		printf("Case #%d: %s\n", T, res.c_str());
	}
	


#if !ONLINE_JUDGE
	//printTime;
#endif
	return 0;
}