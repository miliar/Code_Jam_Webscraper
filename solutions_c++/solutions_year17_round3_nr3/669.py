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
#include<iomanip>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define EPS 1e-6
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
	cout << fixed << setprecision(6);
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;cin>>t;
	int cs = 1;
	while(t--){
		int n,k;cin>>n>>k;
		double as; cin>>as;
		vector<double> data;
		FOR(i,n){
			double a;cin>>a;
			data.pb(a);
		}
		sort(data.begin(),data.end(),greater<double>());
		double l = 0.00, r = 1.00;
		FOR(j,100){
			double mid = (l+r)/2;
			double tmp = 0;
			FOR(i,n){
				if(data[i]<mid){
					tmp += mid-data[i];
				}
			}
			if(tmp > as)r=mid;
			else l=mid;
		}
		double ans = 1;
		FOR(i,n){
			if(data[i]<l){
				ans*=l;
			}else ans*=data[i];
		}
		cout << "Case #" << cs++ << ": " << ans << endl;
	} 
	return 0;
}

