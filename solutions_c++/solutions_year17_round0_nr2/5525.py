#include <bits/stdc++.h>
using namespace std;
bool dp[20][10][2];
int num[20];
int ans[20];
int calc(int idx,int lst,bool is)
{
    if (idx==20)
        return true;
    if (dp[idx][lst][is])
        return false;
    dp[idx][lst][is]=true;
    for (int i=is?9:num[idx]; i>=lst; --i)
        if (calc(idx+1,i,is|(i!=num[idx])))
        {
            ans[idx]=i;
            return true;
        }
    return false;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    long long n;
    for (int test=1;test<=t;++test)
    {
        cin>>n;
        for (int i=19; i>=0; --i,n/=10)
            num[i]=n%10;
        memset(dp,0,sizeof(dp));
        calc(0,0,0);
        long long s=0;
        for (int i=0; i<20; ++i)
        {
            s*=10;
            s+=ans[i];
        }
        cout<<"Case #"<<test<<": "<<s<<endl;
    }

}
