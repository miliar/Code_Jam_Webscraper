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
    	freopen("B-large.in","r",stdin);
    	freopen("output.txt","w",stdout);
	}
	int T = 1;
	scanf("%d",&T);
	int t = 1;
	while(T--){
		static char str[20005];	
		scanf("%s",str);
		int n = strlen(str);
		int ind = -1;
		for(int i=1;i<n;i++){
			if(str[i]<str[i-1]){
				ind = i;
				break;
			}
		}
		printf("Case #%d: ",t++);
		if(ind==-1){
			printf("%s\n",str);
		} else {
			while(ind>0&&str[ind]<str[ind-1]){
				str[ind-1]--;
				ind--;
			}
			for(int i=ind+1;i<n;i++){
				str[i] = '9';
			}
			bool s = true;
			for(int i=0;i<n;i++){
				if(s&&str[i]=='0')
					continue;
				s = false;
				printf("%c",str[i]);
			}
			if(s){
				printf("0");
			}
			puts("");
		}
	}
	return 0;	
}