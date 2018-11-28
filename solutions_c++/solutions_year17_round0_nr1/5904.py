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
int T,t,i,k,len,cnt,tmp;
char str[1004];
int main()
{
	freopen("input.in","r",stdin);
	freopen("opx.txt","w",stdout);
	s(T);
	for(t=1;t<=T;t++)
	{
		ss(str);
		s(k);
		len=strlen(str);
		i=0;
		cnt=0;
		while(i<len)
		{
			while(i<len && str[i]=='+')i++;
			//cout<<"first +"<<i<<" ";
			if(i<len && len-i>=k)
			{
				tmp=k;
				int x=i;
				while(tmp--)
				{
					if(str[i]=='+')str[i]='-';
					else str[i]='+';
					i++;
				}
				i=x;
				cnt++;
			}
			else
			break;
		}
		if(i==len)
		printf("Case #%d: %d\n",t,cnt);
		else
		printf("Case #%d: IMPOSSIBLE\n",t);
	}
	return 0;
}
