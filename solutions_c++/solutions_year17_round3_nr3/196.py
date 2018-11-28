#include <bits/stdc++.h>

using namespace std;

#define _FILES
#define PB push_back
#define MP make_pair

typedef long long ll;
typedef pair<int,int> pii;
const int MAXN = 55;
double p[MAXN];

double solve()
{
    int n,k,cnt;
    double U,ans;
    cin>>n>>k;
    cin>>U;
    cnt = (int)(U*10000+1e-5);
    for (int i=0;i<n;i++)
    {
        cin>>p[i];
    }

    for (int i=0;i<cnt;i++)
    {
        sort(p,p+n);
        p[0] += 0.0001;
    }

    ans = 1.0;
    for (int i=0;i<n;i++) ans *= p[i];
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);

    #ifdef _FILES
        freopen("C-small-1-attempt0.in","r",stdin);
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
