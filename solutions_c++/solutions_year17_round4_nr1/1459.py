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



int dp[101][101][101][4];


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin>>t;
	rep(ca,t){
		int ans;
		int n,p;
		cin>>n>>p;
		int g[100];
		rep(i, n)cin >> g[i];

		/*if (p == 2){
			int cnt=0;
			rep(i, n)if (g[i]%2==1)cnt++;
			ans = n - cnt / 2;
		}
		else if (p == 3){

		}
		else{

		}*/
	
		int mod[4] = {};
		rep(i,n){
			mod[g[i]%p]++;
		}
		map<pair<array<int,4>,int>, int> dp;

		array<int, 4> arr;
		rep(i, 4)arr[i]=0;
		dp[make_pair(arr,0)]=0;
		pair<array<int, 4>, int> st();

		auto it = dp.begin();
		while (1){
			arr = it->first.first;
			int m=it->first.second;
			int v = it->second;

			rep(i, p){
				if (arr[i] + 1 <= mod[i]){
					auto a = arr;
					a[i]++;
					dp[make_pair(a, (m + i)%p)]
						= max(dp[make_pair(a, (m + i)%p)], v + (m == 0));
				}
			}
			if (++it==dp.end())break;
		}
		rep(i, 4)arr[i] = mod[i];
		ans=0;
		rep(i, p)ans = max(ans, dp[make_pair(arr,i)]);

		cout << "Case #"<<ca+1<<": "<<ans<<endl;
	}


	return 0;
}