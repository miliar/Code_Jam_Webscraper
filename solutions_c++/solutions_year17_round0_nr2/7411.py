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
ll t,n;

int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    ifstream fin;fin.open("B-small-attempt0 (2).in");
    ofstream fout;fout.open("out.txt");


    fin>>t;
    rep(tt,1,t){

        fin>>n;
        string s;
        while(n){
            s.pb(n%10 + '0');
            n/=10;
        }
        reverse(s.begin(),s.end());

        string ans;

        if(s.size()==1) ans=s;
        else{
            rep(i,0,s.size()-1){
                if(i==s.size()-1 || s[i]<=s[i+1]){
                    ans.pb(s[i]);
                    continue;
                }
                if(s[i]=='1'){
                    string tem;
                    rep(i,1,s.size()-1) tem.pb('9');
                    ans=tem;
                    break;
                }

                ans.pb(s[i]);
                char cc = s[i];
                ll st=i;
                while(st>=0 && ans[st] == cc){
                    ans[st]--;
                    st--;
                }
                rep(j,i+1,s.size()-1) ans.pb('9');
                break;
            }
        }
        fout<<"Case #"<<tt<<": "<<ans<<'\n';
        cout<<"Casedsd "<<tt<<endl;
    }
}
