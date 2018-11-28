#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<ll, ll> pl;
#define PI 2*acos(0)

int T, n, k;
ll r[1010], h[1010];
vector<pl > vpl;
vector<ll> vh;

int main(){
	scanf("%d", &T);
	//printf("%.15lf\n", PI);
	for(int cas=1; cas<=T; cas++){
		scanf("%d %d", &n, &k);	
		vpl.clear();	
		for(int i=0; i<n; i++){
			scanf("%lld %lld", &r[i], &h[i]);
			vpl.push_back(pl(r[i], i));
		}
		sort(vpl.begin(), vpl.end());
		double best = 0;
		for(int gr=n-1; gr>=0; gr--){
			double ans = 1.0*PI*vpl[gr].first*vpl[gr].first + 2.0*PI*vpl[gr].first*h[vpl[gr].second];
			vh.clear();
			for(int i=0; i<gr; i++){
				vh.push_back(h[vpl[i].second]*vpl[i].first);
			}
			sort(vh.begin(), vh.end());
			bool pos=true;
			for(int i=0; i<k-1; i++){
				if(gr-i-1>=0){
					ans += 2.0*PI*vh[gr-i-1];
				}
				else{
					pos= false;	
				}
			}
			if(pos){
				best = max(best, ans);
			}
		}	
		printf("Case #%d: %.15lf\n", cas, best);
	}
	return 0;
}
