#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef long double ld;

#define rep(i,a,b) for(ll i=a;i<=b;++i)
#define rev(i,a,b) for(ll i=a;i>=b;i--)
#define pll pair<ll,ll>
#define vll vector<ll>
#define sll set<ll>
#define vpll vector<pll>
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define ln length()
#define M 1000000007
ll t,k;
string s;
int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    ifstream fin;fin.open("A-large (1).in");
    ofstream fout;fout.open("outfinal.txt");


    fin>>t;
    rep(tt,1,t){
        fin>>s>>k;
        ll n=s.size();
        ll ans=0;
        rep(i,0,n-k){
            if(s[i]=='+') continue;
            rep(j,i,i+k-1){
                if(s[j]=='+') s[j]='-';
                else s[j]='+';
            }
            ans++;
        }
        ll ct=0;
        rep(i,0,n-1) if(s[i]!='+') ct++;
        if(ct) fout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<'\n';
        else fout<<"Case #"<<tt<<": "<<ans<<'\n';
        cout<<"Casedsd "<<tt<<endl;
    }
}
