#include<iostream>
#include<cstring>
#include<cstdio>
#include<map>
#include<utility>
#include<vector>

#include<set>
using namespace std;

int main()
{int T,t=0 ;
char s[1009];
 scanf("%d",&T) ;
for(int x1=0;x1<T;x1++)
{int i,j,k,n,a,b;
 long long int ans=0;
 bool flag=false;
 scanf("%s",&s) ;
 n=strlen(s);
 scanf("%d",&k) ;
 i=0;
 while(i<n)
 {
        if(s[i]=='+')
        i++;
        else
        {
        if(i+k<=n)
        {
        for(j=i;j<(i+k);j++)
        {
            if(s[j]=='+')
            s[j]='-';
            else
            s[j]='+';
        }
        ans++;
        }
        i++;
        }
 }
 for(i=0;i<n;i++)
 {
  if(s[i]=='-')
        {flag=true;
        break;
        }
 }

 if(flag)
    printf("Case #%d: IMPOSSIBLE\n",x1+1) ;
 else
    printf("Case #%d: %lld\n",x1+1,ans) ;
}
  return 0;
}
