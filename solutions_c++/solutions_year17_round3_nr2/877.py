#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(a);i<=(b);i++)
#define ll long long
#define pll pair<ll, ll>
#define pii pair<int,int>
#define pb push_back
#define F first
#define S second
#define mod 1000000007
#define maxn 100005
#define boost ios::sync_with_stdio(false);cin.tie(0)
#define fr freopen("source.txt","r",stdin),freopen("output.txt","w",stdout)
#define SET(a,b) memset(a,b,sizeof(a))

pii a[201];

int main(){
    boost;
    
    int t;
    cin>>t;
    rep(tc,1,t){
        cout<<"Case #"<<tc<<": ";

        int ac,aj,ans;
        cin>>ac>>aj;
        rep(i,1,ac+aj)cin>>a[i].F>>a[i].S;
        if(ac==2||aj==2){
            sort(a+1,a+3);
            if(a[2].S-a[1].F>720)ans=4;
            else ans=2;
        }
        else ans=2;
        cout<<ans<<endl;
        
    }

    return 0;
}