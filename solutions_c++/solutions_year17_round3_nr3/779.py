#include <bits/stdc++.h>

using namespace std;

int n,m;
double a[110];
double u;
int f[1500];


int main(){
	int T;
	scanf("%d", &T);
	for (int ti=1;ti<=T;ti++){
		scanf("%d%d",&n,&m);
		cin >> u;
		for (int i=0;i<n;i++) cin >> a[i];
		sort(a,a+n);
		double ans=1;
		//cout << n<<" "<<m<<endl;
		if (n==1){
			ans=min(a[0]+u, ans);
		}else{
			//for (int i=0;i<n;i++) cout<<a[i]<<endl;
			//return 0;
			for (int i=0;i<n-1;i++){
				double delta = a[i+1]-a[i];
				if (delta>1e-6){
					if (delta*(i+1)<=u){
						u-=delta*(i+1);
						for (int j=0;j<=i;j++) a[j] = a[i+1];
					}else{
						for (int j=0;j<=i;j++)
							a[j]+=u*1.0/(i+1);
						u=0;
					}
				}
				//for (int j=0;j<n;j++) cout<<a[j]<<endl;
			}
			//for (int i=0;i<n;i++) cout<<a[i]<<endl;
			for (int i=0;i<n;i++){
				a[i]+=u*1.0/n;
				a[i]=min(1.0 ,a[i]);
				ans*=a[i];
			}
		}
		printf("Case #%d: %.10f\n", ti, ans);
	}
	return 0;
}