#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pb push_back
#define vll vector<long long>
#define cd complex<double>
#define pll pair<long long, long long>
using namespace std;
int main(){
    freopen("3.in","r",stdin);
    freopen("3.out","w",stdout);
    int t,cases;
    ll n,k,aux,l;
    cin>>t;
    cases=1;
    while(t--){
        cin>>n>>k;
        map<ll, ll> m;
        priority_queue<ll> q;
        m[n]=1;
        q.push(n);
        while(k>0){
            n = q.top();
            q.pop();
            aux = m[n];
            if(aux>=k)break;
            k-=aux;
            l = n/2ll;
            if(n%2==1){
                if(m.count(l)==0){
                    q.push(l);
                }
                m[l] += 2*aux;
            }
            else{
                if(m.count(l)==0){
                    q.push(l);
                }
                m[l] += aux;
                if(m.count(l-1)==0){
                    q.push(l-1);
                }
                m[l-1] += aux;
            }
        }
        cout<<"Case #"<<cases<<": ";
        l=n/2ll;
        if(n%2==1){
            cout<<l<<" "<<l<<"\n";
        }
        else{
            cout<<l<<" "<<(l-1ll)<<"\n";
        }
        cases++;
    }
}
