#include <bits/stdc++.h>
#define ll long long int
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define itr vector <int> :: iterator
#define vi vector <int> 
#define lb lower_bound
#define fast ios::sync_with_stdio(0);cin.tie(0);
#define tt int t; cin>>t; while(t--)
#define ff first
#define ss second
#define fora(i,a,b) for(i=a;i<b;i++)
#define reva(i,a,b) for(i=a;i>=b;i--)
using namespace std;
bool prime[100010];

void SieveOfEratosthenes(int n){
    memset(prime, true, sizeof(prime));
 
    for (int p=2; p*p<=n; p++)
    {
        if (prime[p] == true)
        {
            for (int i=p*2; i<=n; i += p)
                prime[i] = false;
        }
    }
}

ll power(ll x, ll y, ll p)
{
    int res = 1;      
    x = x % p;  
    while (y > 0)
    {
        if (y & 1)
            res = (res*x) % p;
 
        y = y>>1; // y = y/2
        x = (x*x) % p;  
    }
    return res;
}

void F(){
    ll n,k;
    int i;
    cin>>n>>k;
    k--;
    ll va=1,co=2;
    set<ll> s;
    map<ll,ll> m1;
    m1[n]++;
    s.insert(n);
    while(va<=k){
        set<ll> a;
        map<ll,ll> m2;
        for(auto it=s.begin();it!=s.end();it++){
            ll z=*it;
            if(z%2==0){
                a.insert((z/2)-1);
                a.insert(z/2);
                m2[z/2]+=m1[z];
                m2[(z/2)-1]+=m1[z];
            }
            else{
                a.insert(z/2);
                a.insert(z/2);
                m2[z/2]+=2*m1[z];
            }
        }
        s=a;
        m1=m2;
        va+=co;
        co*=2;
    }    
    k=k-(va-1-co/2);
    vector<ll> vv;
    for(auto it=s.begin();it!=s.end();it++){
        vv.pb(*it);
    }
    for(i=vv.size()-1;i>=0;i--){
        if(m1[vv[i]]>=k){
            if(vv[i]%2==0){
                cout<<vv[i]/2<<" "<<vv[i]/2-1<<endl;
            }
            else
                cout<<vv[i]/2<<" "<<vv[i]/2<<endl;
            return ;
        }
        else{
            k-=m1[vv[i]];
        }
    }
}

int main(){
    fast
    int x=1;
    tt{
        cout<<"Case #"<<x<<": "; 
        F();
        x++;
    }

}