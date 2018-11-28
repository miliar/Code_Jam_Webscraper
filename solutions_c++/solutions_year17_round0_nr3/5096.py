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

set <ii> Q;
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t; cin>>t;
	rep(o,0,t){
		int n,k; cin>>n>>k;
		Q = *new set <ii>();
		Q.insert(ii(-n,0));
		int l1,l2;
		rep(i,0,k){
			ii v = *Q.begin();
			Q.erase(v);
			int len = -v.fi; int pos = v.se;
			int p = len/2;
			int ne = (len%2==0)? (pos + p -1) : (pos+p);
			int len1 = ne-pos; int len2 = len - len1-1;
			Q.insert(ii(-len1,pos)); Q.insert(ii(-len2,ne));
			if(i==k-1){
				l1 = len1;
				l2 = len2;
			}


		}

		int a1 = min(l1,l2);
		int a2 = max(l1,l2);

		cout<<"Case #"<<o+1<<": "<<a2<<" "<<a1<<endl;
		
	}
}
