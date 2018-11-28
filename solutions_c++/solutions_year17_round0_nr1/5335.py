#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
using namespace std;


int main()
{
	FILE * fin=fopen("input.in","r");
	FILE * fin2=fopen("output.out","w+");

	int t=0;
	fscanf(fin,"%d",&t);
	char ch[2002];
	int s=0;
	int r=1;

	while(t-->0)
	{
		int ans=0;
		fscanf(fin,"%s%d",ch,&s);
		int i=0;
		for(;ch[i+s-1]=='-' ||ch[i+s-1]=='+';i++)
		{
			if(ch[i]=='-')
			{
				ans++;
				for(int j=0;j<s;j++)
				{
					ch[i+j] = ch[i+j] =='-'?'+':'-';
				}
			}
		}
		
		bool f=true;
		for(;ch[i]=='-' ||ch[i]=='+';i++)
		{
			if(ch[i]=='-')
			{
				f=false;
				break;
			}
		}

		fprintf(fin2, "Case #%d: ",r);

		if(f)
		{
			fprintf(fin2, "%d\n",ans);
		}
		else
		{
			fprintf(fin2, "IMPOSSIBLE\n");
		}
		r++;

	}

	return 0;
}