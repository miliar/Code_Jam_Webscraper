/* 
 * Work Over Your Laziness
 * 
 */

#include<iostream>
#include<stdio.h>
#include<vector>
#include<utility>
#include<map>
#include<algorithm>
#include<string>
#include<string.h>
#include<queue>
#include<stack>
#include<cmath>
#include<set>
#include<sstream>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PHI 2.0*acos(0.0)
#define FOR(i,j) for (int (i) = 0;(i) < (j);(i)++)
#define FORU(i,j,k) for (int (i) = (j);(i) <= (k);(i)++)
#define FORD(i,j,k) for (int (i) = (j);(i) >= (k);(i)--)

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef pair<ii,int> iii;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ii> vii;

inline void out(int a){
	printf("%d\n",a);
}
inline void out(int a,int b){
	printf("%d %d\n",a,b);
}
inline void outf(double a){
	printf("%3.lf\n",a);
}
inline void outf(double a,double b){
	printf("%3.lf %3.lf\n",a,b);
}
inline void base(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
}

int main(){
	base();
	freopen("B-small-attempt1.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;cin>>t;
	int cs = 1;
	while(t--){
		int c,j;cin>>c>>j;
		vii tc,tj;
		FOR(i,c){
			int a,b;cin>>a>>b;
			tc.pb(ii(a,b));
		}
		FOR(i,j){
			int a,b;cin>>a>>b;
			tj.pb(ii(a,b));
		}
		cout << "Case #" << cs++ << ": ";
		if(c==1||j==1) cout << 2 << endl;
		else if(c==2){
			sort(tc.begin(),tc.end());
			if(tc[1].se-tc[0].fi <= 720 || tc[0].se-tc[1].fi+1440 <= 720) cout << 2 << endl;
			else cout << 4 << endl;
		}else if(j==2){
			sort(tj.begin(),tj.end());
			if(tj[1].se-tj[0].fi <= 720 || tj[0].se-tj[1].fi+1440 <= 720) cout << 2 << endl;
			else cout << 4 << endl;
		}
	} 
	return 0;
}

