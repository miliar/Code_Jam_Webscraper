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

int main(){
	string a;
	int ans,x,n,k,m;
	
	cin>>m;
	rep(j,m){
		cin>>a;
		cin>>k;
		n = a.size();
		//cout<<k<<endl;
		cout<<"Case #"<<j+1<<": ";
		ans=0;
		for(x=0;x+k-1<n;x++){
			if(a[x]=='-'){
				ans++;
				for(int i=0;i<k;i++){
					if(a[x+i]=='-')
						a[x+i]= '+';
					else
						a[x+i] = '-';
				}
			}
			//cout<<a<<endl;
		}
		while(a[x]=='+'&& x<n)
			x++;
		if(x<n)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<ans<<endl;
	}
	return 0;
}