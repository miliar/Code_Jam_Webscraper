#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pb push_back
#define vll vector<long long>
#define cd complex<double>
#define pll pair<long long, long long>
using namespace std;
int main(){
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int t,cases;
    ll n,l,r,m10,aux;
    bool b;
    cin>>t;
    cases=1;
    while(t--){
        cin>>n;
        b=true;
        while(b){
            l=n;
            aux = l%10ll;
            b=false;
            l/=10ll;
            m10=1ll;
            while(l>0ll){
                m10*=10ll;
                if(aux<l%10ll){
                    b=true;
                    break;
                }
                aux = l%10ll;
                l/=10ll;
            }
            if(b){
                n = (n/m10) * m10;
                n--;
            }
        }
        cout<<"Case #"<<cases<<": "<<n<<"\n";
        cases++;
    }
}
