// by realflash
#include<bits/stdc++.h>
using namespace std;

#include<limits>
#define ll long long

typedef pair<int, int > pii;
#define pb push_back
#define mk make_pair
#define MEM(a,b) memset(a,(b),sizeof(a))
#define rep(p,q,r) for(int p=q;p<r;p++)
#define TEST int test; cin >> test;while(test--)
#define si(x) scanf("%d",&x)
#define author real_flash
#define si2(x,y) scanf("%d %d",&x,&y)
#define sl(x) scanf("%lld",&x)
#define prl(x) printf("%lld\n",x)
#define ff first
#define ss second
#define BE(a) a.begin(), a.end()
#define bitcnt(x) __builtin_popcountll(x)
#define INF 111111111111111LL
#define mo 1000000007
//std::cout << std::setprecision(3) << std::fixed;
int MAX=numeric_limits<int>::max();
const int N=1e6+5;
//ios_base::sync_with_stdio(0);cin.tie(0);

ll len(int n)
{
    ll ret=0;
    while(n--)
    {
        ret=(ret*10+9);
    }
    return ret;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
  ll po[20];
  po[0]=1;
  rep(i,1,19)
  po[i]=po[i-1]*10;
    int hh=1;
    TEST
    {
        ll x;
        cin>>x;
        ll y=x;
        ll ans=0;
        int i=0;
        ll rem=0;
        ll last=10;
        while(y>0)
        {
            ll p=y%10;
            y/=10;
            if(last>=p)
            {
                ans=p*po[i]+ans;
                last=p;
            }
            else
            {
                p--;
                ans=p*po[i]+len(i);
                last=p;
            }
            i++;
            //cout<<ans<<"\n";
        }
        cout<<"Case #"<<hh<<": "<<ans<<"\n";
        hh++;
    }

}
