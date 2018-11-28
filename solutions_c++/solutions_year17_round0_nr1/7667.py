#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define fore(i,a,b) for(ll i=a;i<b;i++)
#define fores(i,a,b) for(ll i=a;i<=b;i++)
typedef vector<ll> vi;
typedef pair<ll,ll> pii;

int main() {
	// your code goes here
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	ll t;
    cin>>t;
    fores(j,1,t){
        string s;
        ll k,cnt=0;
        cin>>s>>k;
        ll l=0,r=s.size()-1,n=s.size();
        while(l<r){
            if(s[l]=='-'){
                fore(i,l,min(l+k,n))
                    (s[i]=='+')?(s[i]='-'):(s[i]='+');
                cnt++;
                //cout<<"L"<<" "<<l<<"\n";
            }
            if(s[r]=='-'){
                for(ll i=r;i>=max((r-k+1),0ll);i--)
                    (s[i]=='+')?(s[i]='-'):(s[i]='+');
                //cout<<"R"<<" "<<r<<"\n";
            cnt++;
            }
            l++;
            r--;
        }
        bool flag=false;
        fore(i,0,n)
        if(s[i]=='-')
        {
            flag=true;
            break;
        }
        //cout<<s<<"\n";
        if(flag)
            cout<<"Case "<<"#"<<j<<": IMPOSSIBLE\n";
        else
            cout<<"Case "<<"#"<<j<<": "<<cnt<<"\n";
    }
	return 0;
}

