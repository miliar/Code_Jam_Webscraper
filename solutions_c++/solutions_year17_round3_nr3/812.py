#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
using namespace std;
typedef long long ll;
typedef const ll cll;

#define MX 100000
//vector<int> adj[MX];

int main() {
	int i,j,k,T,C,S,f,sz;
	scanf("%i",&C);
	for(T=1;T<=C;++T) {
		cout<<"Case #"<<T<<": ";
		//code here
		int n;
		double U,p;
		vector<double> ps;
		cin>>n>>k>>U;
		for(i=0;i<n;++i){
			cin>>p;
			ps.pb(p);
		}
		sort(ps.begin(),ps.end());
		
		double al=0;
		for(i=0;i<n;++i){
			if(i+1!=n){
				al=ps[i+1]-ps[i];
				if(fabs(al)<.0000001) continue;
			}
			else al=U;
			
			if(al*(i+1)<U) {
				for(j=0;j<i+1;++j) ps[j]+=al;
				U-=al*(i+1);
			}
			else {
				for(j=0;j<i+1;++j) ps[j]+=U/(i+1);
				U=0;//al*(i+1);
			}	
		}
		
		double tot=1;
		for(auto x : ps) tot*=x;
		
		cout<<fixed<<setprecision(7)<<tot;
		if(T!=C) cout<<endl;
	}
}