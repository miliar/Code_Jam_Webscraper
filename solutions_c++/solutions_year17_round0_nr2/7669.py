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
        string s,s1="";
        cin>>s;
        ll n=s.size(),i,temp=s.size()-1;
        while(true){
            bool flag=false;
            for(i=0;i<temp;i++){
                if(s[i]<=s[i+1])
                    continue;
                else{
                    flag=true;
                    break;
                }
            }
            if(flag){
                s[i]=s[i]-1;
                temp=i;
                continue;
            }
            else
                break;
        }
        cout<<"Case #"<<j<<": ";
        if(s[0]=='0'){
            fore(i,0,n-1)
            cout<<9;
            cout<<"\n";
        }
        else{
            fores(k,0,temp)
            cout<<s[k];
            fore(k,temp+1,n)
            cout<<9;
            cout<<"\n";
        }
    }
	return 0;
}

