#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n,m;
int p[21];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.ou","w",stdout);
    int t,idx;
    cin>>t;
    for(int tt=0;tt<t;++tt){
        cin>>n;
        m=n;
        for(idx=0;m;m/=10)
            p[idx++]=m%10;
        for(;;){
            bool flag=true;
            for(int j=idx-1;j>=0;--j){
                if(p[j]>p[j-1]){
                    --p[j];
                    while(j>=0) p[--j]=9;
                    flag=false;
                    break;
                }
            }
            while(p[idx-1]==0) --idx;
            if(flag) break;
        }
        m=0;
        for(int j=idx-1;j>=0;--j) m=m*10+p[j];
        printf("Case #%d: %lld\n",tt+1,m);
    }
    return 0;
}
//99999999999999999
//9999999999999999
