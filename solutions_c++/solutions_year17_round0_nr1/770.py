#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

int main()
{
	freopen("./in","r",stdin);
	freopen("./out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		printf("Case #%d: ",test);
		char line[1204];
		int k;
		scanf("%s%d",line,&k);
		
		int bad=0;
		int n=strlen(line);
		int res=0;
		while(1)
		{
			int i;
			for(i=0;i<n;i++)
				if(line[i]=='-')
					break;
			if(n-i<k)
			{
				if(i!=n) bad=1;
				break;
			}
			else 
			{
				res++;
				for(int j=i;j<i+k;j++)
					if(line[j]=='+')
						line[j]='-';
					else
						line[j]='+';
			}
		}
		if(bad) printf("Impossible\n");
		else
		{
			printf("%d\n",res);
		}
	}
	return 0;
}