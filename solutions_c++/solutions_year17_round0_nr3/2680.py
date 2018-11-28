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

map<ll,ll>mp;
priority_queue<ll>q;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int hh=1;
    TEST
    {
        mp.clear();
        while(!q.empty())
            q.pop();
        ll n,k;
        sl(n);
        sl(k);
        k--;
        q.push(n);
        mp[n]=1;
        while(k>0)
        {
            ll x=q.top();
            q.pop();
            ll xc=mp[x];
            ll cnt=min(k,xc);
            if(x%2==0)
            {
                ll left=(x/2)-1;
                ll right=(x/2);
                if(mp[left]==0)
                {
                    q.push(left);
                    mp[left]=cnt;
                }
                else
                {
                    mp[left]+=cnt;
                }
                if(mp[right]==0)
                {
                    q.push(right);
                    mp[right]=cnt;
                }
                else
                {
                    mp[right]+=cnt;
                }
            }
            else
            {
                ll y=x/2;
                if(mp[y]==0)
                {
                    q.push(y);
                    mp[y]=2*cnt;
                }
                else
                {
                    mp[y]+=(2*cnt);
                }
            }
            if(xc>k)
            {
                mp[x]-=(k);
                q.push(x);
                k=0;
            }
            else
            {
                k-=xc;
            }
        }
        ll x=q.top();
        ll lf,rt;
        if(x%2==0)
        {
            lf=(x/2)-1;
            rt=(x/2);
        }
        else
        {
            lf=rt=(x/2);
        }
        printf("Case #%d: %lld %lld\n",hh,max(lf,rt),min(lf,rt));
        hh++;


    }
}
