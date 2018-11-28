#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <climits>
#include <map>
#include <set>
#define lli long long int
using namespace std;

int main()
{
	int t,i,l,counter=1;
	scanf("%d",&t);
	while(t--)
	{
		char s[40];
		scanf("%s",s);
		printf("Case #%d: ",counter);
		counter++;
		l=strlen(s);
		if(l==1)
			printf("%s\n",s);
		else
		{
			int pos=l,flag=0;
			for(i=1;i<l;i++)
			{
				if(s[i]<s[i-1])
				{
					pos=i;
					break;
				}
			}
			if(pos==l){
			    printf("%s\n",s);
			}
			else
			{
			    for(i=pos;i<l;i++)
				s[i]='9';
    			int allSame=1,pos1;
    			for(i=pos-1;i>0;i--)
    			{
    			    if(s[i]!=s[i-1])
    			    {
    			        allSame=0;
    			        pos1=i;
    			        break;
    			    }
    			}
    			if(allSame)
    			{
    			    for(i=1;i<pos;i++)
    			    s[i]='9';
    			    s[0]=(char)(int(s[0])-1);
    			    if(s[0]=='0')
    			    {
    			        for(i=1;i<l;i++)
    			        cout << s[i];
    			        printf("\n");
    			    }
    			    else
    			    printf("%s\n",s);
    			}
    			else
    			{
    			    for(i=pos1+1;i<pos;i++)
    			    s[i]='9';
    			    s[pos1]=(char)(int(s[pos1])-1);
    			    printf("%s\n",s);
    			}
        	}
		}
		
	}
	return 0;
}