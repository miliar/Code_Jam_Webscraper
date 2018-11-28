#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <queue>
#define rep(i,a,b) for (int i = (a); i <= (b); ++i) 
#define rep2(i,a,b) for (int i = (a); i >= (b); --i)
const int maxn = 110;
typedef long long ll;
int l, t, n, k, ans, a[maxn];
using namespace std;
string s;
int main()
{
	//freopen("AAA.txt","w",stdout);
	cin >> t;
	bool flag;
	rep (ss,1,t){
		flag = true;
		ans = 0;
		cin >> s >> k;
		l = s.size();
		rep (i,0,l-1){
			if (s[i]=='-'){
				if (i+k-1>l-1){
					printf("Case #%d: IMPOSSIBLE\n", ss);//Case #1: 3
					flag = false;
					break;
				}
				rep (j,i,i+k-1){
					if (s[j]=='-')
						s[j] = '+';
					else
						s[j] = '-';
				}
				ans ++;
			}
		}
		if (flag)
			printf("Case #%d: %d\n", ss, ans);
	}
	return 0;
}

