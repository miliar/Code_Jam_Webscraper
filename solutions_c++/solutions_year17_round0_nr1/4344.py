#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#define f first
#define s second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define vi vector <int>
#define ld long double
#define pii pair<int, int>
#define y1 sda
using namespace std;    
const int N = int(3e5), mod = int(1e9)  + 7; 
char s[N];
int t,k, a[N];

int main () {
	freopen("in","r",stdin);
	freopen("out", "w", stdout);
	scanf("%d",&t);
	for(int tt = 1; tt <= t; tt++){
		printf("Case #%d: ", tt);
		scanf("\n%s %d",s + 1,&k);
		int n = strlen(s + 1);
		int res = 0;
		int ans = 0;
		for(int i = 1; i <= n - k + 1; i++){
			if(i >= k) res -= a[i - k];
			if(!(s[i] == '-' && res % 2 == 1) && !(s[i] == '+'&& res % 2 == 0)){
				res++;	
				a[i] = 1;
				ans++;
			}
			else a[i] = 0;
		}
		bool ok = 1;
		for(int i = n - k + 2; i <= n; i++){
			if(i >= k) res -= a[i - k];
			if(!(s[i] == '-' && res % 2 == 1) && !(s[i] == '+'&& res % 2 == 0)){
				ok = 0;
			}
		}
		if(!ok) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}


return 0;
}