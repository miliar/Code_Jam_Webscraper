#include<bits/stdc++.h>
using namespace std;

char in[1500];

char flip(char a)
{
	if(a=='-') return '+';
	return '-';
}

int main()
{
	int ntc,k;
	scanf("%d",&ntc);
	for(int tc=1;tc<=ntc;tc++)
	{
		scanf("%s %d",in,&k);
		int len = strlen(in);
		int tot = 0;
		for(int a=0;a<=len-k;a++)
		{
			if(in[a]=='-')
			{
				tot++;
				for(int b=a;b<a+k;b++)
				{
					in[b] = flip(in[b]);
				}
			}
		}
		bool ada = true;
		for(int a=0;a<len;a++) if(in[a]=='-') ada = false;
		printf("Case #%d: ",tc);
		if(ada==false) printf("IMPOSSIBLE\n");
		else printf("%d\n",tot);
	}
}
