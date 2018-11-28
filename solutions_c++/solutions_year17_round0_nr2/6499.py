#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<vector>
#include<stack>
#include<string>
using namespace std;
char a[2000];
int main()
{
    freopen("D:B2.in","r",stdin);

    freopen("D:B1.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        printf("Case #%d: ",ca);
       scanf("%s",a);
       int len=strlen(a);
       while(1)
       {

            int pos=-1;
           for(int i=0;i<len-1;i++)
           {
               if(a[i]>a[i+1])
               {
                   pos=i;
                   a[i]--;
               for(int j=i+1;j<len;j++)
               {
                   a[j]='9';
               }
                   break;
               }

           }
           if(pos==-1)
            break;
       }
       int flag=0;
       for(int i=0;i<len;i++)
       {
           if(a[i]=='0'&&flag==0)
            continue;
           if(a[i]!='0')
            flag=1;
           cout<<a[i];
       }
       cout<<endl;
    }
}
