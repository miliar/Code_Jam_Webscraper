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
ll a[1007],b[1007];
int main()
{   
    ll t,x,y,temp,i,w=1;
    scanf("%lld",&t);
    while(t--)
    {   
        scanf("%lld %lld",&x,&y);
        for(i=0;i<x;i++)
        scanf("%lld %lld",&a[i],&b[i]);
        for(i=0;i<y;i++)
        scanf("%lld %lld",&a[i+x],&b[i+x]);
        if(a[1]<a[0])
        {   
            temp=a[1];
            a[1]=a[0];
            a[0]=temp;
            temp=b[1];
            b[1]=b[0];
            b[0]=temp;
        }
        if(x==2 || y==2)
        { 
            if(b[1]-a[0]<=720 || a[1]-b[0]>=720)
            printf("Case #%lld: 2\n",w++);
            else
            printf("Case #%lld: 4\n",w++);
        }
        else
        printf("Case #%lld: 2\n",w++);
    }
    return 0;
}