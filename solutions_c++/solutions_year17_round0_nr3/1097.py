#include <bits/stdc++.h>
using namespace std;
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define forex(i,j) for(int i=0;i<(j);i++) // 0 .. N-1
#define forin(i,j) for(int i=0;i<=(j);i++) // 0 .. N
#define printv(v) {for(int i=0;i<v.size();i++) cout<<v[i]<<" ";cout<<"\n";}
#define printa(a,len) {for(int i=0;i<len;i++) cout<<a[i]<<" ";cout << "\n";}

typedef long long ll;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef vector<pii> vpii;

#define mp make_pair
#define pb push_back
#define uset unordered_set
#define umap unordered_map
#define mset multiset
#define mmap multimap
#define umset unordered_multiset
#define ummap unordered_multimap
#define all(v) (v).begin(),(v).end()

//int xx[]={0,1,0,-1,-1,-1,1,1,-1};int yy[]={1,0,-1,0,1,1,-1,-1}; //E S W N NE SE SW NW
int main() {
_
int T;cin>>T;

for(int XX=1;XX<=T;XX++){
    ll n,k;
    cin>>n>>k;
    vll v;
    ll temp=n;
    while(temp!=1){
        v.pb(temp);
        temp/=(ll)2;
    }
    v.pb(1);
    ll lev=0;
    ll sz=v.size();
    vector<vector<ll>> dp(sz,vector<ll>(2,0));
    dp[0][0]=1LL;dp[0][1]=0LL;
    for(ll i=1;i<sz;i++){
        if(v[i-1]%2==0){
            dp[i][0]=dp[i-1][0];
            dp[i][1]=dp[i-1][1]*(ll)2+ dp[i-1][0];
        }
        else{
            dp[i][0]=dp[i-1][0]*(ll)2+dp[i-1][1];
            dp[i][1]=dp[i-1][1];
        }
    }
    ll ans=0;
    ll rank=k;
    if(k==1)ans=n;
    else{
        while(k!=1){
            lev++;
            k/=(ll)2;
        }
    //lev--;
    ll pw=1;
    for(int i=0;i<lev;i++)pw=pw*(ll)2;
    pw--;
    rank-=pw;
    if(rank<=dp[lev][0])ans=v[lev];
    else ans=v[lev]-1;
    }
    ans--;
    ll mn=ans/(ll)2;
    ll mx=ans-mn;
    //cout<<"\n";
    //cout<<dp[sz-1][0]<<"\n";
    cout<<"Case #"<<XX<<": "<<mx<<" "<<mn<<"\n";
}
return 0;
}
