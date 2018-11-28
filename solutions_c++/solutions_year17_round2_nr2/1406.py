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
	int cs=1;
	while(t--){
		int n;cin>>n;
		pair<int,char> col[6];
		col[0].se='R';col[1].se='O';col[2].se='Y';col[3].se='G';col[4].se='B';col[5].se='V';
		FOR(i,6)cin>>col[i].fi;
		string ans;
		cout << "Case #" << cs++ << ": ";
		bool ok=true;
		FOR(i,6){
			if(col[i].fi > n/2){ok=false;break;};
		}
		if(!ok)cout << "IMPOSSIBLE\n";
		else{
			char now = ' ';
			sort(col,col+6,greater<pair<int,char> >());
			while(n--){
				FOR(i,6){
					if(col[i].fi!=0 && col[i].se!=now){
						ans+=col[i].se;
						col[i].fi--;
						now=col[i].se;
						break;
					}
				}
				sort(col,col+6,greater<pair<int,char> >());
			}
			if(ans[ans.size()-1]==ans[0]){
				swap(ans[ans.size()-1],ans[ans.size()-2]);
			}
			cout << ans << "\n";
		}
	} 
	return 0;
}

