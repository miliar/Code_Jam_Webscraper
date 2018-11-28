#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
FILE *out;
int main()
{
    out=fopen("output.txt","w");
    int i,t;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        long long space;
        long long h=1; // to now.
        long long n,k;
        long long p=1;
        long long en,on;
        long long e,o;
        cin >> n;
        cin >> k;
        while(2*h<=k)
        {
            h*=2;
        }
        h--;
        //printf("h : %lld\n",h);
        if(n%2==0)
        {
            e=1;
            o=0;
            en=n;
            on=0;
        }
        else
        {
            o=1;
            e=0;
            on=n;
            en=0;
        }
        while(2*p<=k)
        {
            long long temp1,temp2;
            long long t1,t2;

            if(on!=0&&en!=0)
            {
                temp1=e;
                temp2=o;
                e=temp1;
                o=temp1;
                if(((on-1)/2)%2==0)
                {
                    e+=2*temp2;
                }
                else
                {
                    o+=2*temp2;
                }
                if(en<on)
                {
                    t1=en/2;
                    t2=on-t1-2;
                    if(t1%2==0)
                    {
                        en=t1;
                        on=t2;
                    }
                    else
                    {
                        en=t2;
                        on=t1;
                    }
                }
                else
                {
                    t1=en/2;
                    t2=en/2-1;
                    if(t1%2==0)
                    {
                        en=t1;
                        on=t2;
                    }
                    else
                    {
                        on=t1;
                        en=t2;
                    }
                }
            }
            else if(o!=0)
            {
                if(on%4==3)
                {
                    on/=2;
                    o*=2;
                }
                else if(on%4==1)
                {
                    en=(on-1)/2;
                    on=0;
                    e=2*o;
                    o=0;
                }
            }
            else if(e!=0)
            {
                t1=en/2;
                o+=e;
                if(t1%2==0)
                {
                    en=t1;
                    on=t1-1;
                }
                else
                {
                    on=t1;
                    en=t1-1;
                }
            }
            p*=2;
        //printf("on : %lld, en : %lld\n",on,en);
        //printf("o : %lld, e :%lld\n",o,e);
        }
        //printf("o : %lld, e :%lld\n",o,e);
        //printf("on : %lld, en : %lld\n",on,en);
        if(en > on)
        {
            if(h+e>=k)
            {
                space=en;
            }
            else
            {
                space=on;
            }
        }
        else
        {
            if(h+o>=k)
            {
                space=on;
            }
            else
            {
                space=en;
            }
        }
        //printf("%lld\n",space);
        printf("Case #%d: ",i+1);
        fprintf(out,"Case #%d: ",i+1);
        if(space%2==0)
        {
            if(space==0)
            {
                printf("0 0\n");
                fprintf(out,"0 0\n");
            }
            else
            {
                printf("%lld %lld\n",space/2,space/2-1);
                fprintf(out,"%lld %lld\n",space/2,space/2-1);
            }
        }
        else
        {
            if(space==1)
            {
                printf("0 0\n");
                fprintf(out,"0 0\n");
            }
            else
            {
                printf("%lld %lld\n",space/2,space/2);
                fprintf(out,"%lld %lld\n",space/2,space/2);
            }
        }

    }
}
