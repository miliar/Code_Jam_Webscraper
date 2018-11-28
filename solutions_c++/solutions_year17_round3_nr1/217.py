#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
#include<array>
#include<cassert>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())


const double pi = acos(-1.);

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);


	int t;
	cin>>t;
	rep(_t, t){
		int n,k;
		int r[1000], h[1000];

		cin>>n>>k;
		rep(i, n)cin >> r[i] >> h[i];
		double ans=0;

		rep(i,n){
			int maxr = r[i];
			vector<long long> v;
			rep(j,n){
				if (j==i)continue;
				v.push_back((long long)r[j]*h[j]);
			}
			sort(all(v));
			reverse(all(v));
			double x = pi*r[i] * r[i];
			x += 2*pi*accumulate(v.begin(),v.begin()+(k-1), 0LL);
			x += 2*pi*(long long)r[i] * h[i];
			ans = max(ans,x);
		}
		printf("Case #%d: %.6f\n",_t+1,ans);
	}


	return 0;
}