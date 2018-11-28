//	Mohib Manva
#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007
#define LOCAL 1
#define pb push_back
#define ll long long

ll po(ll a,ll b){
	ll x = 1,y=a;
	while(b>0){
		if(b%2){
			x = x*y;
			x %= mod;
		}
		y=y*y;
		y%=mod;
		b/=2;
	}
	return x;
}

int main(){
	if(LOCAL){
    	freopen("A-large.in","r",stdin);
    	freopen("output.txt","w+",stdout);
	}
	int T = 1;
	scanf("%d",&T);
	fprintf(stderr,"%d\n",T);
	int t = 1;
	while(T--){
		static char s[2005];
		int k;
		scanf("%s %d",s,&k);
		int n = strlen(s);
		int ans = 0;
		for(int i=0;i<=n-k;i++){
			if(s[i]=='-'){
				ans++;
				for(int j=i;j<i+k;j++){
					if(s[j]=='-'){
						s[j] = '+';
					} else
					s[j] = '-';
				}
				//printf("s:%s\n",s);
			}
		}	
		bool imp = false;
		for(int i=n-k+1;i<n;i++){
			if(s[i]=='-'){
				imp = true;
			}
		}
		printf("Case #%d: ",t);
		if(imp){
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n",ans);
		}
		t++;
	}
	return 0;	
}