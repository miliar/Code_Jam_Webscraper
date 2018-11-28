#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;

int main()
{
    freopen("/Users/qianjay/Documents/cc/in", "r", stdin);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        printf("Case #%d: ",test);
        ll n;
        scanf("%lld",&n);
        vector<int> a;
        while(n>0)
        {
            a.push_back(n%10);
            n/=10;
        }
        int now=(int)a.size();
        for(int i=0;i<a.size();i++)
        {
            if(i<a.size()-1&&a[i]<a[i+1])
            {
                now=i+1;
                if(now==(int)a.size()+1) break;
                while(now<a.size()-1&&a[now]-1<a[now+1])
                    now++;
            }
        }
        if(now<a.size())
        {
            a[now]--;
            for(int i=now-1;i>=0;i--) a[i]=9;
        }
        ll res=0;
        ll base=1;
        for(int i=0;i<a.size();i++)
        {
            res+=a[i]*base;
            base*=10;
        }
        printf("%lld\n",res);
    }
    return 0;
}
