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

double side(double r,double h){
	return 2*r*PHI*h;
}

double area(double r){
	return r*r*PHI;
}

double dp[1005][1005];
vii data;
int n,k;
double rec(int idx,int ch){
	if(ch==0)return 0;
	if(idx==n)return 0;
	if(dp[idx][ch]!=0)return dp[idx][ch];
	double plus = side(data[idx].fi,data[idx].se);
	if (ch==k) plus+= area(data[idx].fi);
	return dp[idx][ch] = max(rec(idx+1,ch),rec(idx+1,ch-1)+plus);
}

bool cmp(ii a,ii b){
	if(a.fi==b.fi)return a.se > b.se;
	return a.fi>b.fi;
}

int main(){
	base();
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;cin>>t;
	int cs = 1;
	cout << fixed << setprecision(6);
	while(t--){
		cin>>n>>k;
		memset(dp,0,sizeof(dp));
		data.clear();
		FOR(i,n){
			int a,b;cin>>a>>b;
			data.pb(ii(a,b));
		}
		sort(data.begin(),data.end(),cmp);
		cout <<"Case #" << cs++ << ": " << rec(0,k) << endl;
	} 
	return 0;
}

