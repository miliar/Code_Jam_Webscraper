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
	double pi = 3.14159265359;
	rep(o,0,t){
		int c,j; cin>>c>>j;
		int sum = c+j;
		pair<int,ii> d[sum];
		int ac,aj; ac=0; aj = 0;
		rep(i,0,c){
			int a,b;
			cin>>a>>b;
			aj+= b-a;
			d[i] = make_pair(a,ii(b,1));
		}
		rep(i,0,j){
			int a,b;
			cin>>a>>b;
			ac+= b-a;
			d[i+c] = make_pair(a,ii(b,-1));
		}
		sort(d,d+c+j);
		int res = 0;
		int free=0;
		int b[c+j];
		int k=0;
		rep(i,1,c+j){
			int s = (d[i].se).se;
			int s1 = (d[i-1].se).se;
			if((s!=s1)){
				res += 1;
				free += (d[i].fi) -(d[i-1].se).fi;
			}
			else {
				b[k]= (d[i].fi) -(d[i-1].se).fi;
				if(s1==1){
					aj += b[k];
				}
				else{
					ac += b[k];
				}
				k++;

			}

		}
		if(c+j>=2){
			int s = (d[0].se).se;
			int s1 = (d[c+j-1].se).se;
			if((s!=s1)){
				res += 1;
				free += (d[0].fi) -(d[c+j-1].se).fi + 24*60;
			}
			else {
				b[k]= (d[0].fi) -(d[c+j-1].se).fi + 24*60;
				if(s1==1){
					aj += b[k];
				}
				else{
					ac += b[k];
				}
				k++;
			}
		}
		rep(i,0,k){
			
			b[i] = -b[i];
		}
		int diff = abs(aj-ac);
		
		sort(b,b+k);
		diff = max(diff-2*free,0);
		
		
		int i=0;
		while(diff>0 && i<k){
			int h = -b[i];
			res +=2;
			diff = max(diff-2*h,0);
			i++;
		}
		if(c+j==1) res =2;
		cout<<"Case #"<<o+1<<": "<<res<<endl;
		
	}
}
