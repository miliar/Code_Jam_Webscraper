#include <bits/stdc++.h>
using namespace std;
int t,dig,ban=-1;
char str[100];
long long n;
int main()
{freopen("input.IN","r",stdin);
freopen("outxyz.txt","w",stdout);
    scanf("%d",&t);
getchar();
int ind=0;
while(t--)
   {gets(str);
   ban=-1;
   ind++;
   int len=strlen(str);
   if(len==1)
   {printf("Case #%d: ",ind);
       puts(str);
       continue;
   }
   for(int i=len-1;i>=1;i--)
   {if(str[i]>=str[i-1])
   continue;
   else
    {str[i]='9';
    ban=i;
    if(str[i-1]=='0')
        {str[i-1]='9';
        ban=i;}
    else str[i-1]-=1;
   }
   }int i=0;
   while(str[i]=='0')
    i++;
printf("Case #%d: ",ind);
for(i;i<len;i++)
{if(i!=ban)
printf("%c",str[i]);
else{
    while(i<len)
    {printf("9");i++;}
}

}
printf("\n");}
return 0;}

