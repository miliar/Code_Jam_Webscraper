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




int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin>>t;
	rep(_t,t){
		int n,k;
		double u, p[100];
		cin>>n>>k;
		cin>>u;
		rep(i, n)cin >> p[i];

		double lb=0,ub=1;
		rep(i,100){
			double mid = (lb+ub)/2;
			double s=0;
			rep(j,n){
				if (mid > p[j])s += mid - p[j];
			}
			if (s<u)lb=mid;
			else ub=mid;
		}
		rep(i, n)p[i] = max(p[i],lb);


		double ans=1;
		rep(i, n)ans *= p[i];


		printf("Case #%d: %.6f\n", _t + 1, ans);
	}


	return 0;
}