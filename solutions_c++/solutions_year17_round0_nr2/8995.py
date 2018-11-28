#include<bits/stdc++.h>
using namespace std ;

int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
int t;scanf("%d",&t);int j=1;
while(t--)
    {int done=0;
    char st[200];int n=0;
    scanf("%s",st);int ct=0;int trig=0;
    for(int i=0;i<=strlen(st)-1;i++){if(st[i]=='0'){trig=1;}if(trig==1){st[i]='0';}}
    trig=0;
    //for(int i=strlen(st)-1;i>0;i--){if(st[i]<st[i-1]){}}
  //  printf("[%s]",st);
    for(int i=strlen(st)-1;i>=0;i--){if(st[i]!='0'){break;}++ct;}
//printf("{%d}",ct);
    for(int i=strlen(st)-1;i>0;i--)
        {
         if(ct>0){--ct;st[i]='9';if(st[i-1]!=0){st[i-1]=st[i-1]-1;}else{st[i-1]='9';}}
         if(st[i-1]>st[i])
            {st[i]='9';if(st[i-1]!=0){st[i-1]=st[i-1]-1;}else{st[i-1]='9';}

                for(int j=i+1;j<strlen(st);j++){st[j]='9';}

         }
        }
      long long sum=0;
      for(int i=0;i<strlen(st);i++){sum=sum*10+(long long)(st[i]-48);}
      printf("Case #%d: %lld",j,sum);j++;if(j!=t){puts("");}
    }
return 0;
}
