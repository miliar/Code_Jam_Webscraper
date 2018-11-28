#include <bits/stdc++.h>

using namespace std;

#define ll long long

const int maxn = 55;

int n,k;

double u;

double p[maxn];

bool test(double x){
	double sum = 0;
	for(int i=0;i<n;i++){
		if(p[i]<x){
			sum += x-p[i];
		}
	}
	return sum<=u;
}

int main(){

	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.out","w",stdout);
	int t;
	cin>>t;
	int cas = 0;
	
	while(t--){
		cas++;
		cin>>n>>k;
		
		cin>>u;
		
		for(int i=0;i<n;i++){
			cin>>p[i];
		}
		
		int Time = 100000;
		double l = 0.0;
		double r = 1.0;
		
		double Min = 0;
		
		while(Time--){
			double mid = (l+r)/2;
			if(test(mid)){
				Min = mid;
				l = mid;
			}else{
				r = mid;
			}
		}
		
		double ans = 1;
		for(int i=0;i<n;i++){
			if(p[i]<Min){
				p[i] = Min;
			}
			ans *= p[i];
		}
		printf("Case #%d: %.6f\n",cas,ans);
	}
	return 0;
}
