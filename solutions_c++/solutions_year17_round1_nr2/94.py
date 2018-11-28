#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <algorithm>
#define MOD 1000000007
#define forn(a, n) for(int a = 0; a<(int) (n); ++a)
#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define forall(a, all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)
#define EPS 0.000000000001
typedef long long tint;
using namespace std;

int main()
{
#ifdef ACMTUYO
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif
	int C;
	cin >> C;
	forn(tc, C) {
		int n, p;
		cin >> n >> p;
		vector<tint> q(n);
		forn(i, n) cin >> q[i];
		vector<vector<tint> > r(n, vector<tint>(p));
		vector<vector<tint> > used(n, vector<tint>(p,0));
		forn(i, n)
			forn(j, p)
				cin >> r[i][j];
		
		vector<tint> cands;
		forn(i, n)
			sort(r[i].begin(), r[i].end());
		forn(i, n)
			forn(j, p)
				cands.push_back((r[i][j]*10+11*q[i]-1)/(11*q[i]));
		sort(cands.begin(), cands.end());
		
		int ans = 0;	
		forn(i, cands.size()){
			//cout << cands[i] << endl;
			tint s = cands[i];
			vector<tint> pack;
			forn(j, n) {
				tint packed = 0;
				forn(k, p) {
					//cout << cands[i]*11*q[j] << " " << 10*r[j][k] << " " << cands[i]*9*q[j] << endl; 
					if(s*11*q[j] >= 10*r[j][k] && s*9*q[j] <= 10*r[j][k] && !used[j][k]) {
						packed = 1;
						pack.push_back(k);
						break;
					}
				}
				if(!packed) break;
			}
			if((int) pack.size() == n) {
				ans++;
				forn(j, n){
					used[j][pack[j]]=1;
				}
				s--;
			} 
		}
		cout << "Case #" << tc+1 << ": "; 
		cout << ans << endl;
	}
}
