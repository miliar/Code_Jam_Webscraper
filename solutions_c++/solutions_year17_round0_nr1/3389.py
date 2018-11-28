/* 
 * Work Over Your Laziness
 * 
 */

#include<iostream>
#include<stdio.h>
#include<cstdio>
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
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin>>t;
	int ctr=1;
	while(t--){
		string s;cin>>s;
		int k;cin>>k;
		int ans = 0;
		FOR(i,(int)s.length()-k+1){
			if(s[i]=='-'){
				ans++;
				FORU(j,i,i+k-1){
					if(s[j]=='-')s[j]='+';
					else s[j]='-';
				}
			}
		}
		bool cek=true;
		FOR(i,(int)s.length()){
			if(s[i]=='-'){
				cek=false;
				break;
			}
		}
		cout << "Case #" << ctr++ << ": ";
		if(!cek)cout << "IMPOSSIBLE\n";
		else cout  << ans << "\n";
	} 
	return 0;
}

