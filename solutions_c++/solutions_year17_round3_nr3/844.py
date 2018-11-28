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

double p[50];
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	cout.precision(17);
	int t; cin>>t;
	double pi = 3.14159265359;
	rep(o,0,t){
		int n,k; cin>>n>>k;
		double u;
		cin>>u;
		double ma=-1;
		rep(i,0,n){
			cin>>p[i];
			if(p[i]>ma) ma =p[i];
		}
		sort(p,p+n);
		double s = p[0];
		rep(i,1,n){
			if(u<0.0000000001) break;
			double h= p[i]-s;
			double x = min(u/i,h);
			s += x;
			
			rep(j,0,i){
				p[j]=s;
			}
			u = u- i*x;
			if(u<0.0000000001) break;
		}
		
		
		rep(i,0,n){
			
		}
		if(u>0){
			rep(i,0,n){
				p[i] += u/n;
			}
		}
		double res =0;
		double f=0;
		rep(i,0,n){
			f+= log(p[i]);
		}
		res = exp(f);
		cout<<"Case #"<<o+1<<": "<<res<<endl;
		
	}
}
