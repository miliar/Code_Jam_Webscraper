#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;
FILE *out;
int main()
{
    out=fopen("output.txt","w");
    int get=0;
    int t;
    long long n;
    long long q=1;
    long long ans=0;
    long long v=1;
    int x1=0;
    int x2=0;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        q=1;
        ans=0;
        cin >> n;
        v=n;
        while(n>0&& ans < v)
        {
            if(n<10)
            {
                ans+=n*q;
                n=0;
                x1=0;
                x2=0;
            }
            else
            {
                if(x1==0&&x2==0)
                {
                    x1=(n%100)/10;
                    x2=n%10;
                }
                if(x1 <= x2)
                {
                    ans += q*x2;
                    n/=10;
                    x1=0;
                    x2=0;
                    q*=10;
                }
                else
                {
                    x1--;
                    x2=9;
                    ans = 10*q*1-1;
                    n/=10;
                    x2=0;
                    q*=10;
                    get=1;
                }
                if(x1<0)
                {
                    if(n>=10)
                    {
                        x1=(n%100)/10-1;
                        x2=9;
                    }
                }
                else
                {
                    if(get==1)
                    {
                        n--;
                        get=0;
                    }
                    x1=0;
                    x2=0;
                }
            }
            //printf("%lld\n",ans);
        }
        printf("Case #%d: %lld\n",i+1,ans);
        fprintf(out,"Case #%d: %lld\n",i+1,ans);
    }
}
