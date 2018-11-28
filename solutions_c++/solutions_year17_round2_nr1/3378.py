#include<bits/stdc++.h>
using namespace std;
#define M 1000000007
#define f first
#define s second
#define pb push_back
#define ll long long
#define mp make_pair
#define r0 return 0
typedef pair<int,int> pii;
typedef pair<ll,ll> lpii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<lpii> vlpii;
int mini(int a,int b){return a<b?a:b;}
ll lmini(ll a,ll b){return a<b?a:b;}
int maxi(int a,int b){return a>b?a:b;}
ll lmaxi(ll a,ll b){return a>b?a:b;}
//double gcd(double a, double b){ if(b==0) return a; return gcd(b,a%b); }
//ll lgcd(ll a, ll b){ if(b==0) return a; return gcd(b,a%b); }
//double lcm(double a, double b) {return a*(b/gcd(a,b));}
//ll llcm(ll a, ll b) {return a*(b/gcd(a,b));}
int t;
int main(){
    fstream file;
    file.open("first.txt",ios::out);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int q;
    cin>>t;
    for(q=1;q<=t;q++){
       // vector<pair<int,int> > v;
        int n,d,d1,s1;
        cin>>d>>n;
        int i;
        double m=-1,x;
        for(i=1;i<=n;i++){
            cin>>d1>>s1;
             x=(double)(d-d1)/(double)s1;
            if(x>m)m=x;
           // v.pb(mp(d1,s1));
        }
        x=(double)d/(double)m;
        file<<fixed;
        file<<setprecision(9);
        file<<"Case #"<<q<<": "<<x<<endl;
    }
    file.close();r0;
}
