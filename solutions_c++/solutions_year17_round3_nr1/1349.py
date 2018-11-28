#include<bits/stdc++.h>
#define PI 3.141592653589793
#define ll long long
#define MOD 1000000007
using namespace std;


int main(){	
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;cin>>t;

	for(int kase = 1; kase <= t; kase++){
		int n;cin>>n;
		int K;cin>>K;
		double r[1010], h[1010];
		double arr[1010];
		for(int i=1; i<=n; i++){
			cin>>r[i]>>h[i];	
		}
		double ans = 0;
		for(int i=1; i<=n; i++){
			double mx = r[i];
			int k = 1;
			double area = (r[i]*r[i])+(2*r[i]*h[i]);
			if(K == 1){
				ans = max(ans, area);continue;
			}
			for(int j=1; j<=n; j++){
				if(j == i)continue;
				if(mx >= r[j]){
					arr[k] = 2*r[j]*h[j];k++;
				}
			}
			if(k > K-1){
				sort(arr+1, arr+k);
				int temp = K-1, j=k-1;		
				while(temp--){area+=arr[j--];}
				ans = max(ans, area);
			}
		}
//		ans *= (22.0/7.0);
		printf("Case #%d: %0.9lf\n", kase, ans*PI);
	}	
	return 0;
}
