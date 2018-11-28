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
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	
	int C;
	cin >> C;
	forn(tc, C) {
		int r, c;
		cin >> r >> c;
		vector<string> tab(r);
		forn(i, r) cin >> tab[i];
		
		int lr = -1, lc = -1;
		char lch = '?';
		forn(i, r){
			forn(j, c){
				if(tab[i][j] != '?') {
					lch = tab[i][j];
					for(int k = lc+1; k<j; k++) {
						tab[i][k] = lch;
					}
					lc = j;
				}
			}
			if(lc!=-1){
				for(int k = lc+1; k<c; k++) {
					tab[i][k] = lch;
				}
				
				for(int j = lr+1; j<i; j++) {
					tab[j] = tab[i];
				}
				lr = i;
			}
			lc = -1;
		}
		for(int j = lr+1; j<r; j++) {
			tab[j] = tab[lr];
		}
		cout << "Case #" << tc+1 << ":" << endl; 
		forn(i, r) cout << tab[i] << endl;
	}
}
