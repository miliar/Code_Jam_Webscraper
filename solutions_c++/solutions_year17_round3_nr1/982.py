#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#define pii pair<double,double>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
using namespace std;
typedef long long ll;
typedef const ll cll;

#define MX 1005
#define PI 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
//vector<int> adj[MX];

int main() {
	int i,j,k,T,C,S,f,sz;
	scanf("%i",&C);
	for(T=1;T<=C;++T) {
		cout<<"Case #"<<T<<": ";
		//code here
		int N,K;
		double x,h,sum=0;
		vector<pii> cakes;
		cin>>N>>K;
		for(i=0;i<N;++i) {
			cin>>x>>h;
			cakes.pb(mp(PI*x*x,2.0*x*h*PI));
		}
		sort(cakes.begin(),cakes.end(),
		[](const pii&a,const pii&b){
			if(fabs(a.ff-b.ff)<.00001) return a.ss>b.ss;
			return a.ff>b.ff;
		});
		
		//
		pair<pii,int> ar[MX];
		for(i=0;i<N;++i)
			ar[i]=mp(cakes[i],i);
		
		sort(ar,ar+N,
		[](const pair<pii,int>&a,const pair<pii,int>&b){
			if(fabs(a.ff.ss-b.ff.ss)<.000001) return a.ff.ff>b.ff.ff;
			return a.ff.ss>b.ff.ss;
		});
		
		double tmp;
		int cnt;
		for(i=0;i<N;++i){
			tmp=cakes[i].ff+cakes[i].ss;
			cnt=1;
			for(j=0;j<N&&cnt<K;++j) {
				if(ar[j].ff.ff>cakes[i].ff) continue; //larger face
				else if(ar[j].ss==i)		continue; //same pancake
				else {
					tmp+=ar[j].ff.ss;
					cnt++;
				}
			}
			if(tmp>sum)sum=tmp;
		}
		
		
		cout<<fixed<<setprecision(9)<<sum;
		if(T!=C) cout<<endl;
	}
}