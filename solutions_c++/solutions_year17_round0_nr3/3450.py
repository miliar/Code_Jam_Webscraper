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
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("C-small-2-attempt0.out","w",stdout);
	int t,ctr=1;
	cin>>t;
	while(t--){
		int n,k;
		cin>>n>>k;
		priority_queue<int> pq;
		pq.push(n);
		int l,r;
		while(k--){
			int now = pq.top();pq.pop();
			now--;
			int x = now/2;
			int y = now-x;
			pq.push(x);pq.push(y);
			l=max(x,y);r=min(x,y);
		}
		cout << "Case #" << ctr++ << ": " << l << " " << r << endl;
	} 
	return 0;
}

