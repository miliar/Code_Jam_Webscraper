#include<bits/stdc++.h>
using namespace std;
int main(){

	int t,N,D,i,j,d[1005],sp[1005],p;
	double tt,tm,ss;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(p=1 ;p<=t ;p++){

		scanf("%d %d",&D,&N);
		tt = 0.0;
		for(i=1 ;i<=N ;i++){
			scanf("%d %d",&d[i],&sp[i]);
			ss = (double)(D-d[i])/sp[i];
			//cout<<ss<<endl;
			tt = max(tt,ss);

		}
		cout<<setprecision(10)<<"Case #"<<p<<": "<<(double)(D/(double)tt)<<endl;

		/*double l = 1.0;
		double r = 100000.0;
		double mid;
		double res;
		//cout<<tt<<endl;
		while(l <= r){

			mid = (l+r)/2;
			tm = D/mid;
			if(tm >= tt){
				l = mid + 1.0;
				res = mid;
				//cout<<tm<<endl;
			}
			else
				r = mid - 1.0;
		}
		//cout<<tm<<endl;
		//cout<<setprecision(6)<<"Case #"<<p<<": "<<res<<endl;*/

	}


}
