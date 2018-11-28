#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <string>

using namespace std;

# define pb push_back
# define mp make_pair

typedef long long ll;
typedef pair<int,int> PII;

const int maxn =  (1e5)+10;


int main()
{
	// freopen("input.txt","r",stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt","w", stdout);
	int ncase, T , D, n, k, s;
	double ans;
	ncase = 0;
	cin >> T;
	while(T --) {
		ncase++;
		ans = (1e30)+10;
		cin >> D >> n;
		for(int i = 1; i <= n; i++) {
			cin >> k >> s;
			ans = min(ans, s*1.0*(D*1.0/(D-k)));
		}
		printf("Case #%d: %.7lf\n",ncase,ans);
	}
	return 0;
}