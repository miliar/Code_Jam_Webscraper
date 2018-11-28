typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <utility>
#define pb push_back
#define mp make_pair
#define pll pair<ll,ll> 
#define plll pair<ll,pair<ll,ll> >

using namespace std;
char s[1007];
int main()
{
    ll t,w=1,i,j,k,flag,c;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%s %lld",s,&k);
        i=0;
        flag=c=0;
        while(i<strlen(s))
        {
            if(s[i]=='-')
            {
                if(i+k-1>=strlen(s))
                {
                    flag=1;
                    break;
                }
                c++;
                for(j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                    s[j]='-';
                    else
                    s[j]='+';
                }
            }
            i++;
        }
        if(flag)
        printf("Case #%lld: IMPOSSIBLE\n",w++);
        else
        printf("Case #%lld: %lld\n",w++,c);
    }
	return 0;
}