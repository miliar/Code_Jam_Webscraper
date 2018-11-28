# include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int cntdigits(ll n){
	int r = 0;
	if(n==0) return 1;
	while(n>0){
		r++;
		n/=10;
	}
	return r;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		ll n;
		int a[20];
		scanf("%lld",&n);
		int d = cntdigits(n);
		for(int i=d-1;i>=0;i--){
			a[i] = n%10;
			n/=10;
		}
		int i = d-2;
		while(i>=0){
			if(a[i]>a[i+1]){
				a[i] = a[i]-1;
				for(int j=i+1;j<d;j++) a[j] = 9;
			}	
			i--;
		}
		printf("Case #%d: ",t);
		i=0;
		while(i<d && a[i]==0) i++;
		while(i<d) printf("%d",a[i++]);
		printf("\n");	
	}
	return 0;
}