#include <iostream>
#include <string.h>

using namespace std;

void flip(char *s,int k)
{
	for(int i=0;i<k;i++){
	if(s[i]=='+')
		s[i]='-';
	else
		s[i]='+';}
}

int main()
{
	int N;
	char s[1001];
	int k;
	scanf("%d",&N);
	for (int i=1;i<=N;i++)
	{
		memset(s,0,1000);
		scanf("%s %d",s,&k);
		int l=strlen(s);
		printf("Case #%d: ",i);
		int res=0;
		for(int j=0;j<l;j++)
		{
			if(s[j]=='-'){
				if(j+k<=l){
					flip((s+j),k);
				res++;}
				else
				{
					printf("IMPOSSIBLE\n");
					res=-1;
					break;
				}
			}
			else continue;
		}
		if(res>=0)
			printf("%d\n",res);
	}
	return 0;
}
