#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key
#define rep(i,a,b) for(int i=a;i<b;i++)

typedef long long ll;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef list<int> li;
typedef long double ld; 
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;
typedef list<int>::iterator lit;

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	cout.precision(17);
	int t; cin>>t;
	rep(o,0,t){
		int d,n; cin>>d>>n;
		double ma = -1;
		rep(i,0,n){
			int k,s; cin>>k>>s;
			double m= (d-k)/double(s);
			if(m>ma){
				ma=m;
			}
		}
		double res = d/ma;
		cout<<"Case #"<<o+1<<": "<<res<<endl;
		
	}
}
