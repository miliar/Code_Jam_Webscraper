#include<string>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<vector>
#include<unordered_map>
#include<string.h>
#include<queue>
#include<map>
using namespace std;
#define N 400005
#define INF 1100000000
map<int,int> mp;
map<int,int> ::iterator it;
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    int ca=0;
    scanf("%d",&t);
    while(t--)
    {
        mp.clear();
        int n,k;
        scanf("%d%d",&n,&k);
        mp[n]=1;
        int ans1,ans2;
        while(k--)
        {
            it=mp.end();
            it--;
            int q=it->first;
         //   cout<<q<<endl;
            if(--mp[q]==0)mp.erase(it);
            int z=q/2;
            mp[z]++,mp[max(z-(q&1?0:1),0)]++;
            ans1=z,ans2=max(z-(q&1?0:1),0);
        }
        printf("Case #%d: ",++ca);
        cout<<ans1<<' '<<ans2<<endl;
    }

    return 0;
}


