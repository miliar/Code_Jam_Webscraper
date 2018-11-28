#include <bits/stdc++.h>
using namespace std;
int t,Total;
long long n,y,last;
char s[100];
bool b1;
vector<char> v;
int main()
{
    freopen("inputA.in","r",stdin);
    //ifstream cin("input.in");
    freopen("output.in","w+",stdout);
    scanf("%d",&t);
    Total=t;
    while(t--)
    {

        scanf("%lld",&n);
        last=0;
        for(long long i=n; i>=1; i--)
        {

            if(i<10)
            {
                last=i;
            }
            else
            {
                sprintf(s,"%lld",i);
                b1=true;
                for(int j=1; j<strlen(s); j++)
                {
                    if(s[j]=='0')
                    {
                        b1=false;
                    }
                }
                if(b1)
                {
                    b1=true;
                    for(int j=0; j<strlen(s)-1; j++)
                    {
                        if(s[j]>s[j+1])
                        {
                            b1=false;
                        }
                    }
                    if(b1)
                        last=i;
                }
                s[0]='\0';
            }
            if(last!=0)
                break;
        }
        printf("Case #%d: %lld\n",Total-t,last);
    }
}
