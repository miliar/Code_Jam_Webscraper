#define _CRT_SECURE_NO_WARNINGS
#include<bits/stdc++.h>
#include<unordered_map>
using namespace std;
typedef	long long ll;
typedef unsigned long long ull;
#define all(v) ((v).begin()),((v).end())
#define sz(v) ((int)((v).size()))
#define PI(n) ((double)acos(n))
#define pw2(n) (1LL<<(n))
#define sfi1(v) scanf("%d",&v)
#define sfi2(v1,v2) scanf("%d%d",&v1,&v2)
#define sfi3(v1,v2,v3) scanf("%d %d %d",&v1,&v2,&v3)
int dx8[8] = { 1, -1, 0, 0, 1, 1, -1, -1 };
int dy8[8] = { 0, 0, 1, -1, 1, -1, 1, -1 };
void file()
{
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#else
	// online submission
#endif
}
void fast()
{
	std::ios_base::sync_with_stdio(0);
	cin.tie(NULL); cout.tie(NULL);
}
bool can(vector<int> v){
	for (int i = 0; i < v.size() - 1; i++){
		if (v[i] < v[i + 1]){
			return 0;
		}
	}
	return 1;
}
int main()
{
	file();
	fast();
	int t;
	cin >> t;
	int c =0;
	for (int tt = 1; tt <= t; tt++){
		ll x;
		cin >> x;
		vector<ll> rem(5000);
		int j = 0;
		c = 0;
		while (x!=0){
			c++;
			rem[j] = (x % 10);
			x /= 10;
			j++;
		}
		for (int t22 = 0; t22<1000; t22++){
			for (int k = c; k>0; k--)
				if(rem[k]>rem[k - 1]){
					rem[k]--;
					for (int a = 0; a < k; a++)
						rem[a] = 9;

					
				}
		}
		ll ans = 0;
		for (int ww = c; ww >= 0; ww--){
			ans = ans * 10 + rem[ww];
		}
		cout << "Case #" << tt << ": " << ans<< endl;
	}
}