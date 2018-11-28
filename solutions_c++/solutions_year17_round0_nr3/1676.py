#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(int)a;i<=(int)b;i++)
#define rip(i,a,b) for(int i=(int)a;i>=(int)b;i--)
#define ll long long
#define MOD 1000000007
#define N 200005
#define f first
#define s second
#define pb push_back
#define pii pair<int,int>
#define matrix vector<vector<ll>>
#define PI acos(-1)
#define INF 10000000
#define LSOne(S) (S & (-S))
int main() {
   freopen("/home/vikhyat/Desktop/in.txt","r",stdin);
   freopen("/home/vikhyat/Desktop/out.txt","w",stdout);
    // ios_base::sync_with_stdio(false);
    //	cin.tie(0);
	//cout.tie(0);
    int t;
    cin>>t;
    rep(_,1,t)
    {
        cout<<"Case #"<<_<<": ";
        ll k,n,ans1,ans2;
        cin>>n>>k;
        set<ll> s;
        map<ll,ll> mp;
        mp[n]=1;
        ll j=0;
        s.insert(n);
        while(!s.empty()&&j<k)
        {
            auto it=(s.end());
            it--;
            auto p=*it;
            auto cnt=mp[p];
            //cout<<p<<endl;
            if(p==0)
            {
                ans1=0,ans2=0;
                break;
            }
           // cout<<p<<endl;
            s.erase(p);
            j+=cnt;
            if(p%2)
            {
            ans1=p/2,ans2=p/2;
                s.insert(ans1);
                mp[p/2]+=2*cnt;
            }
            else
            {
            ans1=p/2,ans2=p/2-1;
                s.insert(p/2);
                s.insert(p/2-1);
                mp[p/2]+=cnt;
                mp[p/2-1]+=cnt;
            }
        }
        cout<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}
