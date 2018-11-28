#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
using namespace std;
int main()
{
	int T,k;
	char s[1005];
	cin>>T;
	for(int qi=1;qi<=T;qi++)
	{
		printf("Case #%d: ",qi);
		memset(s,0,sizeof(s));
		scanf("%s %d",s+1,&k);
		int n=strlen(s+1),ans=0;
		for(int i=1;i<=n;i++)
			if(s[i]=='-')
			{
				if(i+k-1>n){ans=-1;break;}
				ans++;
				for(int j=0;j<k;j++)
					s[i+j]^='+'^'-';
			}
		if(ans==-1)printf("IMPOSSIBLE\n");
		else cout<<ans<<endl;
	}
	return 0;
}