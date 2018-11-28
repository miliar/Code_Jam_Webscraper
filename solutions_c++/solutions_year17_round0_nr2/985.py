#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cstring>
using namespace std;
char n[20];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T, cas=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%s",n);
        int len = strlen(n);
        long long ans = 0;
        int pos=-1;
        for(int i=1;i<len;i++)
        {
            if(n[i]<n[i-1])
            {
                pos=i;
                break;
            }
        }
        if(pos!=-1)
        {
            for(int i=pos;i<len;i++) n[i]='9';
            for(int i=pos-1;i>=0;i--)
            {
                if(i==0)
                {
                    n[i]--;
                    break;
                }
                if(n[i]==n[i-1])
                {
                    n[i]='9';
                }
                else
                {
                    n[i]--;
                    break;
                }
            }
        }
        for(int i=0;i<len;i++)
        {
            ans = 10LL * ans + n[i] - '0';
        }
        printf("Case #%d: %lld\n", ++cas, ans);


    }
}
