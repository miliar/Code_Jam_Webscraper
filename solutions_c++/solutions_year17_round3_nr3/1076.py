#include <bits/stdc++.h>

#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%lld",&n)

#define pd(n) printf("%d\n",n)
#define pld(n) printf("%lld\n",n)

#define test int t; sd(t);while(t--)
#define MAXI (int)1e6 + 1

typedef long long ll;


using namespace std;

double arr[100];
int main(){
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("A2.out","w",stdout);
	int z=1;

	test{
		printf("Case #%d: ",z++);
		int n,k;sd(n);sd(k);


		double U; cin >> U;


		for(int i=0;i<n;i++){
			cin >> arr[i];
		}


		sort(arr,arr+n);

		double temp=U;
		for(int i=1;i<n;i++){
			if(temp>=i*(arr[i]-arr[i-1])){
				temp-=i*(arr[i]-arr[i-1]);
			}
			else{
				double add=temp/(i);

				for(int j=0;j<i;j++){
					arr[j]=arr[i-1]+add;
				}
				temp=0;
				break;
			}
			//cout << temp << endl;
		}

		if(temp>0){
			double add=temp/n;

			for(int i=0;i<n;i++)arr[i]=arr[n-1]+add;


		}

		double ans=1;
		for(int i=0;i<n;i++){
			ans*=arr[i];
		}
		printf("%.8lf\n",ans);
	}

}
