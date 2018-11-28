#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

typedef long long int ll;
typedef pair<int,ll> id;
typedef pair<ll,int> di;

int main(){
	int t;
	int k,n,r,h;
	ll area;
	ll ans;
	vector<id> rA; 
	vector<di> aR;
	scanf("%d\n", &t);
	for (int _=1; _<=t; _++){
		scanf("%d %d\n", &n, &k);
		rA.clear();
		aR.clear();
		ans=0ll;
		for(int i=0; i<n; i++){
			scanf("%d %d\n", &r, &h);
			area = 2*(long)r*(long)h;
			rA.push_back(make_pair(r,area));
			aR.push_back(make_pair(area,r));
		}
		sort(rA.rbegin(),rA.rend());
		//for(int i=0; i<n; i++) printf("%d %lld\n", rA[i].first, rA[i].second);
		sort(aR.rbegin(),aR.rend());
		for(int i=0; i<=n-k; i++){
			//printf("new\n");
			r = rA[i].first;
			ll oA = rA[i].second;
			//printf("%d\n",r );
			area = pow(r,2) + rA[i].second;
			//printf("initial %lld\n",area );
			int count =0;
			bool same = false;
			for(int j=0; j<n && count<k-1; j++){
				if(aR[j].second==r && aR[j].first==oA){
					if(!same){
						same = true;
						
					}else{
						count++;
						area+=aR[j].first;
						//printf("%d\n",aR[j].second );
					}
				}
				if(aR[j].second<r){
					count++;
					area+=aR[j].first;
					//printf("%d\n",aR[j].second );
				}
			}
			ans = max(ans,area);
		}
		//printf("%lld\n",ans );
		long double an = ans * M_PI;
		printf("Case #%d: %0.10Lf\n", _, an); 
	}
}