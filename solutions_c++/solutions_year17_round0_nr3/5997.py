/*Coded by::
    **Avinash Tiwary**
    **BE/10298/2015**
    **Production Engineer**
    **Producing <code>**
*/
#include<bits/stdc++.h>
#define bf ios_base::sync_with_stdio (0), cin.tie (0)
typedef long long ll;
typedef double d;
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
ll ar[MAX],not_prime[MAX]; 
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
    ll x=1,n,t,i=1,j,m,p,c,flag,t1,ta1,ta2,t2,ans=0,k; string s;
    cin>>t;
    while(x<=t){
        cin>>n>>k;
        priority_queue<ll> v;
        v.push(n);
        for(i=1;i<k;i++){
            j=v.top();
            v.pop();
            if(j%2==1){
                v.push((j-1)/2); v.push((j-1)/2); //cout<<j<<":: ";
            }
            else{
                v.push(j/2); v.push(j/2-1); //cout<<j<<";; ";
            }
        }
        t1=-1,t2=-1,ta1=-1,ta2=-1;
        for(i=0;i<v.size();i++){
            j=v.top(); v.pop();
            if(j%2){
                t1=(j-1)/2; t2=(j-1)/2;
            }
            else{
                t1=j/2; t2=j/2-1;
            }
            if(min(t1,t2)>min(ta1,ta2)){
                ta1=t1; ta2=t2;
            }
            else if(min(t1,t2)==min(ta1,ta2)){
                if(max(t1,t2)>max(ta1,ta2)){
                    ta1=t1; ta2=t2;
                }
            }
        }
        cout<<"Case #"<<x<<": "<<max(ta1,ta2)<<" "<<min(ta1,ta2)<< endl;
        x++;
    }
    return 0;
} 