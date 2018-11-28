#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long int ll;
typedef pair <int,int> pii;
typedef vector <int> vi;

#define rep(i, n) for(int i = 0; i < (n); ++i)
#define forn(i, a, b) for(int i = (a); i < (b); ++i)
#define ford(i, a, b) for(int i = (a); i >= (b); --i)
#define fore(i, a, b) forn(i, a, b + 1)
#define repa(i,n,a) for(int i = 0; i < (n); ++i) {cin>>a[i];}

#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(c) c.begin(), c.end()
#define fill(a, v) memset(a, v, sizeof(a))
#define sz(a) ((int)a.size())

#define gl(x) cin >> x
#define gi(x) scanf("%d", &x)
#define pls(x) cout << x << " "
#define pln(x) cout << x << "\n"
#define pis(x) printf("%d ", x)
#define pin(x) printf("%d\n", x)
#define pnl printf("\n")
#define dbn cerr << "\n"
#define dbg(x) cerr << #x << " : " << x << " "
#define dbs(x) cerr << x << " "
#define foreach(c, it) for(__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define fio iNULLos_base::sync_with_stdio(false),cin.tie()
#define MAX 1000000009
#define szs 200005
#define MOD 1000000007

ll max(ll a, ll b){
	if(a>b)
		return a;
	return b;
}
ll min(ll a, ll b){
	if(a<b)
		return a;
	return b;
}

int main(){
	ll t,n,a[2],x=1,k,y[2],z[2],b[2],ans=0;
	cin>>t;
	rep(j,t){
		ans=0;
		x=1;
		cin>>n>>k;
		cout<<"Case #"<<j+1<<": ";
		if(k==1){
			y[0] = max(n - (n/2)-1,0);
			y[1] = max(0,(n/2));
			cout<<max(y[0],y[1])<<" "<<min(y[0],y[1])<<endl;
		}
		else{
			b[0]=1;
			b[1]=1;
			z[0]= max((n/2) ,0);
			y[0]= max(n - z[0]-1,0);
			a[0]=z[0];
			a[1]=y[0];
			
			//cout<<".. "<<a[0]<<" "<<b[0]<<" "<<a[1]<<" "<<b[1]<<endl;
			ans = 1;
			x*=2;
			while(x+ans< k){
				z[0] = b[1];//2nd count
				z[1] = a[1];//2nd val
				y[0] = max((a[0]/2),0);
				a[1] = max(a[0]-y[0]-1,0);
				a[0] = y[0];
				b[1]=b[0];
					// if(a[0]== y[1])
					// 	b[0]*=2;
					// else{
					// 	a[1] = y[1];
					// 	b[1] = b[0];
					// }
					//y[1]= max((z[1]/2)-1,0);
					//y[0] = max(z[1]-y[1]-1,0);
					y[0] = max(z[1]/2,0);
					y[1] = max(z[1]-y[0]-1,0);
					if(y[1]==a[0]){
						b[0]+=z[0];
					}
					else if(y[1]==a[1]){
						b[1] +=z[0];
					}
					else{
						b[0]*=2;
						a[1] = y[1];
						b[1] = z[0];
					}
				
					if(y[0]==a[0]){
						b[0]+=z[0];
					}
					else if(y[0]==a[1]){
						b[1] +=z[0];
					}
				ans+=x;
				x*=2;
				//cout<<".. "<<a[0]<<" "<<b[0]<<" "<<a[1]<<" "<<b[1]<<endl;
			}
			ans = k-ans;
			//cout<<"aaaa"<<ans<<endl;
			if(b[0]>=ans){
				y[0] = max((a[0]/2),0);
				y[1] = max(a[0]-(a[0]/2)-1,0);		
			}
			else{
				y[0] = max((a[1]/2),0);
				y[1] = max(a[1]-(a[1]/2)-1,0);
			}
			cout<<max(y[0],y[1])<<" "<<min(y[0],y[1])<<endl;
		}
	}

	return 0;
}