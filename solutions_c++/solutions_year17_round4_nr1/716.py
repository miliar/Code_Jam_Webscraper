#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> plli;
typedef pair<double, double> pdd;
typedef pair<string, int> psi;
const ll oo = 1e15;
typedef long long ll;

const int N = 200010;
const int MX = 200000;


int t, n, g[110], p;

bool block[110];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &t);
	for(int it = 1 ; it <= t ; it++){
		scanf("%d%d", &n, &p);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &g[i]);
		}
		int mx = 0;
		for(int i = 0 ; i < n ; i++){
			memset(block,0,sizeof block);
			int res = 1;
			int have = (p-(g[i]%p))%p;
			block[i] = 1;
			while(1){
				bool could = false;
				int ans = -1;
				int newHave = 1e9;
				for (int i = 0; i < n; ++i){
					if(block[i])
						continue;
					int curHave = have;
					while(curHave < g[i])
						curHave+= p;
					curHave -= g[i];
					if(newHave > curHave){
						newHave = curHave;
						ans = i;
					}
					could = true;
				}
				if(ans != -1){
					block[ans] = 1;
					if(have == 0)
						res++;
					have = newHave;
				}
				if(!could)
					break;
			}
			mx = max(mx,res);
		}
		printf("Case #%d: %d\n",it, mx);
	}
	return 0;
}