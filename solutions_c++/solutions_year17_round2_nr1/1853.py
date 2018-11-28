#include <bits/stdc++.h>

#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%lld",&n)

#define pd(n) printf("%d\n",n)
#define pld(n) printf("%lld\n",n)

#define test int t; sd(t);while(t--)
#define MAXI (int)1e6 + 1

typedef long long ll;


using namespace std;

struct node{
	double kilo,speed;
};

node arr[1000];
double dp[1000];

bool compare(node A ,node B){
	return A.kilo<B.kilo;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);
	int z=1;

	test{
		printf("Case #%d: ",z++);
		double d; int n;
		cin >> d >> n;


		for(int i=0;i<n;i++){
			cin >> arr[i].kilo >> arr[i].speed;
		}
		sort(arr,arr+n,compare);

		dp[n-1]=(d-arr[n-1].kilo)/arr[n-1].speed;


		for(int i=n-2;i>=0;i--){
			dp[i]=max(dp[i+1],(d-arr[i].kilo)/arr[i].speed);
		}

		printf("%.9lf\n",d/dp[0]);
	}
}
