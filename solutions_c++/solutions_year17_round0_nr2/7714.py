#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("init.in","r",stdin);
freopen("output.out","w",stdout);
    int n,cases=1;
    scanf("%d",&n);

    while(n--)
    {
        char ch[10005];
        scanf("%s",&ch);

        int len = strlen(ch);
        int nn=18;
        while(nn--){
        for(int i=0;i<len-1;i++)
        {
           if(ch[i]>ch[i+1])
           {
               ch[i]=ch[i]-1;
              for(int j=i+1;j<len;j++)
              {
                  ch[j]='9';
              }
           }

        }
        }

        printf("Case #%d: ",cases++);
        int i;
        if(ch[0]=='0') i=1;
        else i=0;
        for(i;i<len;i++)
        {
            printf("%c",ch[i]);
        }
        printf("\n");


    }
    return 0;
}

