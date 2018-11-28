//============================================================================
// Name        : acm.cpp
// Author      : shenyuan
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <string.h>
#include <ctime>
#include <limits.h>
using namespace std;

typedef long long ll;
const double pi = acos(-1.0);
const double eps = 1e-8;
//const ll INF=(_I64_MAX)/2;
//#pragma comment(linker, "/STACK:102400000,102400000")
const int inf = 0x3f3f3f3f;
#define maxx(a) memset(a, 0x3f, sizeof(a))
#define zero(a) memset(a, 0, sizeof(a))
#define FILL(a,b) memset(a, b, sizeof(a))
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define srep(i,n) for(i = 1;i <= n;i ++)
#define MP make_pair
#define fi first
#define se second
typedef pair <int, int> PII;

int main() {

    freopen( "in.txt", "r" , stdin);
     freopen ("out.txt","w", stdout);

	int t;
	string s;
	int k;
	cin>>t;
	int cas = 1;
	int i,j;
	while(t--) {
		printf("Case #%d: ",cas++);
		cin>>s>>k;
		int ans = 0;
		for (i = 0;i < s.length() - k + 1; i ++) {
			if (s[i] == '-') {
				ans ++;
				rep(j,k) {
					if (s[i+j] == '-') {
						s[i+j] = '+';
					}
					else {
						s[i+j] = '-';
					}
				}

			}
		}
		bool f = 0;
		rep(i,s.length()) {
			if (s[i] == '-') f = 1;
		}

		if (f) {
			puts("IMPOSSIBLE");
		}
		else {
			cout<<ans<<endl;
		}

	}



	return 0;
}
