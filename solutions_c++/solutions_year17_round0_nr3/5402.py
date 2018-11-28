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
	freopen("C-small-1-attempt0.in", "r", stdin);
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
		ll L, R;
		int n, k;
		cin >> n >> k;
		vector<int>v(1111);
		v[0] =v[n + 1] = 1;
		for (int i = 1; i<= k; i++){
			ll mx1 = -5, mx2 = -5, m;
			ll L1, R1;
			for (int j = 1; j <= n; j++){
				if (v[j])
					continue;
				int temp=j-1;
				while(v[temp]==0)
					temp--;
				L1 = j-temp-1;
				temp = j+1;
				while(v[temp]==0)
					temp++;
				R1 = temp - j - 1;
				if (mx1 <= min(L1, R1)){
					if (mx1 != min(L1, R1)){
						mx1 = min(L1, R1);
						L = L1,R = R1,m = j;
					}
				else if(mx2<max(L1, R1)){
					mx1 = min(L1, R1);
					mx2 = max(L1, R1);
					L = L1, R = R1, m = j;
					}
				}
			}
			v[m] = 1;
		}
		cout << "Case #" << tt << ": " <<max(L,R)<<" "<<min(L,R)<< endl;
	}
}