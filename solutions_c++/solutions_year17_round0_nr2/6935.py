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
char a[107];
int main()
{
    ll t,i,j,flag,w=1,temp;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%s",a);
        flag=0;
        for(i=0;i<strlen(a)-1;i++)
        {
            if(a[i]>a[i+1])
            {
                if(a[i]=='1')
                {
                    flag=1;
                }
                else
                {
                    j=i;
                    while(j>=0)
                    {
                        if(a[j]!=a[i])
                        break;
                        j--;
                    }
                    a[j+1]--;
                    temp=j+2;
                    for(j=temp;j<strlen(a);j++)
                    a[j]='9';
                }
                break;
            }
        }
        printf("Case #%lld: ",w++);
        if(flag)
        {
            for(i=0;i<strlen(a)-1;i++)
            printf("9");
            printf("\n");
        }
        else
        {
            printf("%s\n",a);
        }
    }
	return 0;
}