#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#define s(n) scanf("%d", &n)
#define s2(a,b) scanf("%d %d",&a, &b)
#define ss(n) scanf("%s",n)
#define pb push_back
#define vi vector<int>
using namespace std;
int t,i,T,len;
char str[20];
int main()
{
	freopen("input.in","r",stdin);
	freopen("opx.txt","w",stdout);
	s(T);
	for(t=1;t<=T;t++)
	{
		ss(str);
		len=strlen(str);
		i=0;
		while(i<len-1)
		{
			if((str[i]-'0')>(str[i+1]-'0'))
			break;
			i++;
		}
		if(i!=(len-1))
		{
			while(i>0 && str[i]==str[i-1])
			i--;
			if(str[i]=='1')
			{
				str[i]='9';
				i++;
				while(i<len-1)
				{
					str[i]='9';
					i++;
				}
				str[i]='\0';
			}
			else
			{
				str[i]--;
				i++;
				while(i<len)
				{
					str[i]='9';
					i++;
				}
			}
		}
		printf("Case #%d: %s\n",t,str);
	}
	return 0;
}

