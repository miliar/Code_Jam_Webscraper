#include <bits/stdc++.h>
using namespace std;

char s[25];
int ans[25],val[25];
int n;
bool ok_;
void sol(int p,int v,bool f){
	if(p==n){
		ok_=true;}
	
	if(ok_){return ;}
	//cout<<ok_<<endl;
	for (int i=(f?val[p]:9);!ok_&&i>=v;i--){
		ans[p]=i;sol(p+1,i,f&&i==val[p]);
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while (T--){
		scanf("%s",s);
		//cout<<s<<endl;
		 n=strlen(s);
		 for(int i=0;i<n;i++)val[i]=s[i]-'0';
		 ok_=0;
		sol(0,0,1);
		printf("Case #%d: ",ca++);
		int i=0;
		while(ans[i]==0)i++;

		for (;i<n;i++){
			printf("%d", ans[i]);
		}
		puts("");
	}
}