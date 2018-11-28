#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("outt.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		printf("Case #%d: ",T);
		char s[1001];
		int n,cnt=0,len;
		bool f=1,a[1000];
		scanf("%s%d",s,&n);
		len=strlen(s);
		for(int i=0;i<len;i++)
			if(s[i]=='+')a[i]=1;
			else a[i]=0;
		for(int i=0;i<=len-n;i++)
			if(!a[i]){
				cnt++;
				for(int j=i;j<i+n;j++)
					a[j]=!a[j];
			}
		for(int i=len-n+1;i<len;i++)
			if(!a[i])f=0,i=len;
		if(!f)puts("IMPOSSIBLE");
		else printf("%d\n",cnt);
	}

}

