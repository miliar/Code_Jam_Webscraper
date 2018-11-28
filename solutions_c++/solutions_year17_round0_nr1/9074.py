#include<bits/stdc++.h>

using namespace std;

#define std::cout cout;
#define std::cin cin;

int main()
{
	int i,j,t,cases,len,k,c,m,mn,f,ff;
	char s[1001];
	freopen("A-large.in","r",stdin);
	freopen("problem1 large.out","w",stdout);
	scanf("%d",&cases);
	for(t=1;t<=cases;t++)
    {
	cin>>s;
	cin>>k;
    len=strlen(s);
    c=0;
    f=0;
    m=2*len;
    while(m>0)
    {
    for(i=0;i<=(len-k);i++)
    {
        if(s[i]=='-')
        {
            for(j=i;j<(i+k);j++)
            {
                if(s[j]=='-')
                {
                    s[j]='+';
                }
                else if(s[j]=='+')
                {
                    s[j]='-';
                }
            }
            c++;
        }
    }
    for(i=len-1;i>=(k-1);i--)
    {
        if(s[i]=='-')
        {
            for(j=i;j>(i-k);j--)
            {
                if(s[j]=='-')
                {
                    s[j]='+';
                }
                else if(s[j]=='+')
                {
                    s[j]='-';
                }
            }
            c++;
        }
    }
    m--;
    }
    for(i=0;i<len;i++)
    {
        if(s[i]=='+')
        {
            f=1;
        }
        else
        {
            f=0;
            break;
        }
        if(f==0)
            break;
    }
    if(f==0)
    {
        printf("Case #%d: IMPOSSIBLE\n",t);
    }
    else if(f==1)
    {
        printf("Case #%d: %d\n",t,c);
    }
    }
	return 0;
}
