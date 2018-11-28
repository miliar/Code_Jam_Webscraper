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
	freopen("A-large.in", "r", stdin);
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
int main()
{
	file();
	fast();
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++){
		string x;
		int k;
		cin >> x >> k;
		int c = 0;
		bool ok = 1;
		for (int i = 0; i < x.size(); i++){
			if (x[i] == '-'){
				c++;
				if (i + k <=x.size()){
					for (int j = 0; j  < k; j++){
						if (x[j+i] == '-')
							x[j+i] = '+';
						else x[j+i] = '-';
					}
				}
				else {
					ok = 0;
					break;
				}
			}
		}
		for (int i = 0; i < x.size(); i++){
			if (x[i] == '-')
				ok = 0;
		}
		if (c == 0){
			cout << "Case #" << tt << ": " << 0 << endl;
		}
		else if (!ok)
			cout << "Case #" << tt << ": " << "IMPOSSIBLE" << endl;
		else cout << "Case #" << tt << ": " << c << endl;
	}
}