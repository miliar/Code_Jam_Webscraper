#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int main()
{
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);
	int cas; cin>>cas;
	for(int casi=1;casi<=cas;casi++)
	{
		char s[23]; int i,len;
		scanf("%s",s+1); len=strlen(s+1);
		int L=1;
		for(i=2;i<=len;i++)
		{	if(s[i-1]<s[i]) L=i;
			else if(s[i-1]>s[i])
			{	s[L]--;
				for(int j=L+1;j<=len;j++) s[j]='9';
				break;
			}
		}
		printf("Case #%d: %s\n",casi,(s[1]=='0'?s+2:s+1));
	}
	return 0;
}

