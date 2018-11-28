#include <bits/stdc++.h>
using namespace std;
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define forex(i,j) for(int i=0;i<(j);i++) // 0 .. N-1
#define forin(i,j) for(int i=0;i<=(j);i++) // 0 .. N
#define printv(v) {for(int i=0;i<v.size();i++) cout<<v[i]<<" ";cout<<"\n";}
#define printa(a,len) {for(int i=0;i<len;i++) cout<<a[i]<<" ";cout << "\n";}

typedef long long ll;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef vector<pii> vpii;

#define mp make_pair
#define pb push_back
#define uset unordered_set
#define umap unordered_map
#define mset multiset
#define mmap multimap
#define umset unordered_multiset
#define ummap unordered_multimap
#define all(v) (v).begin(),(v).end()

//int xx[]={0,1,0,-1,-1,-1,1,1,-1};int yy[]={1,0,-1,0,1,1,-1,-1}; //E S W N NE SE SW NW
int main() {
_
int T;cin>>T;

for(int XX=1;XX<=T;XX++){
    int d,n;
    cin>>d>>n;
    vector<pair<double,double>> v;
    int tem=n;
    double a,b;
    //v.pb({0.0,})
    while(tem--){
        cin>>a>>b;
        v.pb({a,b});
    }
    vector<double> tim(n);
    sort(all(v));
    tim[n-1]=(double(d)-v[n-1].first)/v[n-1].second;
    for(int i=n-2;i>=0;i--){
        double tt=(double(d)-v[i].first)/v[i].second;
        tim[i]=max(tt,tim[i+1]);
    }
    double ans=(double)d/tim[0];
    cout<<"Case #"<<XX<<": "<<fixed<<setprecision(6)<<ans<<"\n";
}
return 0;
}
