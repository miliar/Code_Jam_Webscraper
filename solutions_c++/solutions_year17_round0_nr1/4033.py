#include <bits/stdc++.h>
using namespace std;

string s;
int ans,n,k,t;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("Q1-large.out","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		ans=0;
		cin>>s>>k;
		n=s.length();
		for(int i=0;i<n-k;i++){
			if(s[i]=='-'){
				ans++;
				for(int j=i;j<i+k;j++){
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
			}
		}
		char cur=s[n-k];
		int can=1;
		for(int i=n-k+1;i<n;i++){
			if(cur!=s[i]) can=0;
		}
		if(can==0) printf("Case #%d: IMPOSSIBLE\n",tc);
		else{
			if(cur=='-') printf("Case #%d: %d\n",tc,ans+1);
			else printf("Case #%d: %d\n",tc,ans);
		}
	}
}
