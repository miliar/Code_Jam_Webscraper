#include "bits/stdc++.h"
using namespace std;


int main(int argc, char const *argv[])
{    
	 //  freopen("input1.txt","r",stdin);
  // freopen("output.txt","w",stdout);

	int t,tt=0; cin >> t;
	while(t--){
		tt++;
		int n; double d;
		cin >> d >> n;
		double dis[n],sp[n];
		for(int i=0;i<n;i++){
			cin >> dis[i] >> sp[i];
		}
		double maxTime = -1;
		for(int i=0;i<n;i++){
			double tmp = ((d-dis[i]))/sp[i];
			if(tmp>maxTime){
				 maxTime = tmp;
			}
		}
		double ans = d/maxTime;
		 printf("Case #%d: %.6lf\n",tt,ans);
	}
	return 0;
}