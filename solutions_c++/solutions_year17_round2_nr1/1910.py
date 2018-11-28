#include <bits/stdc++.h>

using namespace std;

#define _FILES
#define PB push_back
#define MP make_pair

typedef long long ll;
typedef pair<int,int> pii;
const int MAXN = 1005;
ll k[MAXN],s[MAXN];

double solve()
{
    ll d,n;
    long double lg,rg,mid,t1,t2;
    bool flag;
    cin>>d>>n;
    for (int i=0;i<n;i++) cin>>k[i]>>s[i];
    lg = 1.0;
    rg = 100000000000000.0;
    for (int it=0;it<500;it++)
    {
        mid = (lg+rg)/2.0;
        flag = true;
        for (int i=0;i<n;i++)
        {
            t1 = d/mid;
            t2 = 1.0*(d-k[i])/s[i];
            if (t1<t2)
            {
                flag = false;
                break;
            }
        }
        if (flag) lg = mid; else rg = mid;
    }
    return lg;
}
int main()
{
    ios_base::sync_with_stdio(false);

    #ifdef _FILES
        freopen("A-large.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif // _FILES
    int T;
    cin>>T;
    for (int test=1;test<=T;test++)
    {
        cout<<setprecision(8)<<fixed<<"Case #"<<test<<": "<<solve()<<endl;
    }
    return 0;
}
