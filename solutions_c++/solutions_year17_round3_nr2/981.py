#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#define pii pair<int,pair<int,int>>
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
		int A,B,x,y;
		cin>>A>>B;
		vector<pii> sc;
		for(i=0;i<A;++i){
			cin>>x>>y;
			sc.pb(mp(0,mp(x,y)));
		}
		for(i=0;i<B;++i){
			cin>>x>>y;
			sc.pb(mp(1,mp(x,y)));
		}
		
		sort(sc.begin(),sc.end(),
		[](const pii&a,const pii&b){
			return a.ss.ff<b.ss.ff;
		});
		
		int t[2]={0},swaps=0,safe=0;
		vector<int> av[2];
		sz=sc.size();
		for(i=0;i<sz;++i){
			if(sc[i].ff!=sc[(i+1)%sz].ff){
				safe+=(sc[(i+1)%sz].ss.ff-sc[i].ss.ss+1440)%1440;//allocate safe space
				swaps++;
			}
			else {
				t[sc[i].ff]+=(sc[(i+1)%sz].ss.ff-sc[i].ss.ss+1440)%1440;
				av[sc[i].ff].pb((sc[(i+1)%sz].ss.ff-sc[i].ss.ss+1440)%1440);
			}
			t[sc[i].ff]+=sc[i].ss.ss-sc[i].ss.ff;
		}
		if(t[0]==t[1]) cout << swaps;
		else {
			int rem = abs(t[0]-720);
			if(safe>rem) cout << swaps;
			else {
				rem-=safe;
				int todo=(t[0]<t[1])?1:0;
				sort(av[todo].begin(),av[todo].end(),greater<int>());
				i=0;
				while(rem>0&&i<av[todo].size()) {
					rem-=av[todo][i++];
					swaps+=2;
				}
				cout << swaps;
			}
		}
		//cout <<" :"<< t[0]<<" "<<t[1]<<","<<safe;
		if(T!=C) cout<<endl;
	}
}