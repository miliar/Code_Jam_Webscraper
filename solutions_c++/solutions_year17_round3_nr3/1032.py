#include<iostream> 
#include<algorithm>
#include<stdio.h>
#include<vector>
using namespace std;
void Gao(){
	int T;
	int n,k;
	//scanf("%d",&T);
	cin>>T;
	for(int tt=1;tt<=T;tt++){
		//scanf("%d %d",&n,&k);
		cin>>n>>k;
		double avail;
		vector<double>a;
		cin>>avail;
		double ep=0.0,suma=0.0;
		double ans=1.0;
		for(int i=0;i<n;i++){
			double x;
			cin>>x;
			a.push_back(x);
			suma+=x;
		}
		sort(a.begin(),a.end());
		int ok = false;
		for (int i=0;i<n;i++){
			ep = (suma+avail)/(n-i);
			if (ep>=a[i]) {
				for (int j=i;j<n;j++)
					ans *= ep;
					//printf("%.9lf\n",ans);
					ok = true;
					break;
				}
				if(ok){
					break;
				}
			suma -= a[i];
			ans *= a[i];
		}
		printf("Case #%d: %lf\n",tt,ans);
	}
}
int main(){
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("c.out","w",stdout)
	Gao();
	return 0;
} 
