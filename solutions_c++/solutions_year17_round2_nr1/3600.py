/*Coded by::
    **Avinash Tiwary**
    **BE/10298/2015**
    **Production Engineer**
    **Producing <code>**
*/
#include<bits/stdc++.h>
#define bf ios_base::sync_with_stdio (0), cin.tie (0)
typedef long long ll;
typedef double dob;
#define MAX 1000009
#define MIN -1
#define M 1000000007
#define INF 5e17
using namespace std;
typedef vector<ll> Vector;
typedef queue<ll > Queue;
typedef stack<ll> Stack;
typedef pair<ll,ll> Pair;
#define mp make_pair
#define pb push_back
bool desc(ll i, ll j) { return i > j; }
ll gcd(ll a, ll b)
{   if (a == 0) return b;
    return gcd(b%a, a);
}
ll power(ll x,ll n)
{   if(n==0) return 1;
    else if(n%2 == 0) return power((x*x)%M,n/2);
    else return (x*power((x*x)%M,(n-1)/2))%M;
}
ll ar[MAX],not_prime[MAX],ms[MAX],st[MAX];
string s2d[MAX];
void sieve(){
    not_prime[1]=1; not_prime[0]=1;
    for(ll p=2;p*p<=MAX;p++){
        if(!not_prime[p]){
            for(ll i=p*2;i<=MAX;i+=p) not_prime[i]=1;
        }
    }
}
int main(){
    bf; 
    //sieve();
    ll i,j,tc=1,k,n; dob d,t,ans=0,tim=0,mans=0,flag=1,l; string sar[101],s; char c;
    cin>>t;
    cout<<fixed<<setprecision(6);
    while(tc<=t){
        cin>>d>>n;
        vector<pair<ll,ll> > v;
        l=d;
        for(i=1;i<=n;i++) {
            cin>>j>>k;
            if(i>1){
                if((d-j)/k>=tim) tim=(d-j)/k;
            }
            else{
                tim=(d-(dob)j)/(dob)k; l=j;
            }
        }
        cout<<"Case #"<<(ll)tc<<": "<<d/tim<<endl;
        tc++;
    }
    return 0;
} 