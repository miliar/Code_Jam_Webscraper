#include<iostream>
#include<cstring>
#include<cstdio>
#include<map>
#include<utility>
#include<vector>
#include<unordered_map>
#include<unordered_set>
#include<set>
using namespace std;

char s[10009];
int main()
{int T,t=0 ;
 scanf("%d",&T) ;
while(T--)
{int i,j,k,n,a,b;
 long long int live_the_king ;
 long long int ans=0;
 bool flag=false;
 scanf("%s",&s) ;
 n=strlen(s);
 for(int y=2;y<n;y++)
    i=y ;
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
 for(int x=0;x<n;x++)
 {
  if(s[x]=='-')
        {flag=true;
        break;
        }
 }

 if(flag)
    printf("Case #%d: IMPOSSIBLE\n",++t) ;
 else
    printf("Case #%d: %lld\n",++t,ans) ;
}
  return 0;
}
