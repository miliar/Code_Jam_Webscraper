#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N=1e6+5;

unordered_map<LL, LL> mp;
LL num[N];
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        printf("Case #%d: ", ca++);
        LL n, k;
        cin>>n>>k;
        mp.clear();
        int d=0;
        num[d++]=n;
        mp[n]=1;
        LL l, r;
        for(int i=0;k>0;i++)
        {
            k-=mp[num[i]];
            LL m=num[i];
            if(m&1)
                l=r=m/2;
            else l=m/2-1, r=m/2;
            if(!mp[r]) num[d++]=r;
            mp[r]+=mp[m];
            if(!mp[l]) num[d++]=l;
            mp[l]+=mp[m];
        }
        cout<<r<<" "<<l<<endl;
    }
    return 0;
}
