#include<bits/stdc++.h>
//shreyx#1
#define vi vector<int>
#define sd(x) scanf("%d",&x)
#define sst(x) scanf("%s",x);

#define unsigned long long ull
#define long long ll
// Problem A: Oversized Pancake Flipper
using namespace std;
void flipper(int,int);
char pc[1001];
int main()
{
    int t,ca=1;
    int k,flips,i,n,occ;
    sd(t);
    while(ca<=t)
    {
        flips=0;
        scanf("%s%d",pc,&k);
        n=strlen(pc);
        for(i=0;i<n-k;i++)
        {
            if(pc[i]=='-')
            {
                flipper(i,k);
                ++flips;
            }
        }
        occ=count(pc,pc+n,'-');
        if(occ==0)
            printf("Case #%d: %d\n",ca,flips);
        else if(occ==k)
            printf("Case #%d: %d\n",ca,flips+1);
        else
            printf("Case #%d: IMPOSSIBLE\n",ca);

        ca++;
    }
    return 0;
}

void flipper(int pos,int k)
{
    int i;
    for(i=pos;i<pos+k;i++)
    {
        if(pc[i]=='-')
            pc[i]='+';
        else
            pc[i]='-';
    }
}
