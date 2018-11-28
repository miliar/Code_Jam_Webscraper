#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <cstring>
#include <sstream>
#include <map>
#define pi 2*acos (0.0)
using namespace std;


void change(char s[])
{
        long long l,i,f;
        l=strlen(s);
        f=0;
        for(i=1;i<l;i++)
        {
            if(s[i]>=s[i-1] && f==0)
            {
                continue;
            }
            else if(s[i]<s[i-1] && f==0)
            {

                s[i-1]--;
                s[i]='9';
                f=1;
            }
            else
            {
                s[i]='9';
            }
        }
}


int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    long long t,f,i,l,tc=0;
    char s[20];
    scanf("%lld",&t);
    getchar();
    while(t--)
    {
        strcpy(s,"");
        scanf("%s",&s);
        printf("Case #%lld: ",++tc);
        l=strlen(s);
        for(i=0;i<l;i++)
            change(s);
        for(i=0;i<l;i++)
        {
            if(s[i]=='0') continue;
            else cout<<s[i];
        }
        cout<<endl;
    }
    return 0;
}

