#include<bits/stdc++.h>
using namespace std;

char in[15],ans[15];

char dec(char a)
{
	if(a=='0') return '9';
	return a-1;
}

int main()
{
	int ntc;
	scanf("%d",&ntc);
	for(int tc=1;tc<=ntc;tc++)
	{
		scanf("%s",in);
		int len = strlen(in);
		bool ada = false;
		for(int a=1;a<len;a++)
		{
			if(ada==true) in[a] = '9';
			else
			{
				if(in[a] >= in[a-1]) ;
				else
				{
					int rem = 0;
					in[a] = '9';
					for(int c=a-1;c>=0;c--)
					{
						in[c] = dec(in[c]);
						while(in[c] < in[c-1]) in[c] = dec(in[c]);
						if(in[c]!='9') break;
					}
					ada = true;
				}
			}
		}
		printf("Case #%d: ",tc);
		bool ff = true;
		for(int a=0;a<len;a++){
			if(ff==true && in[a]=='0') continue;
			ff = false;
			printf("%c",in[a]);
		}
		printf("\n");
	}
}
