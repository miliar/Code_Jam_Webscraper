#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int tc,panjang,k,total;
char input[1005];
char balik(char a){
	if(a=='-')
		return '+';
	return '-';
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("outputFillperBig.out","w",stdout);
	scanf("%d",&tc);
	for(int test=1;test<=tc;test++)
	{
		scanf("%s %d",&input,&k);
		panjang=strlen(input);
		total=0;
		for(int i=panjang-1;i>=k-1;i--)
		{
			if(input[i]=='+')
				continue;
			//cout<<"flip di "<<i<<endl;
			total++;
			for(int j=i-k+1;j<=i;j++)
				input[j]=balik(input[j]);
		}
		bool ans=true;
		for(int i=0;i<panjang;i++)
		{
			if(input[i]=='-')
			{
				ans=false;
				break;
			}
		}
		//cout<<input<<endl;
		printf("Case #%d: ",test);
		if(!ans)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",total);
			
	}
}
