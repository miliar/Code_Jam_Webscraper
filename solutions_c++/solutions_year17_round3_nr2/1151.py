#include <bits/stdc++.h>
#define rep(i,n) for(__typeof(n) i=0;i<n;++i)
#define reu(i,s,e) for(__typeof(e) i=s;i<e;++i)
#define each(it,o) for(auto it= (o).begin(); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x7fffffff
#define INFL 0x7fffffffffffffffLL
#define inrep int t;cin>>t; while(t--)
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<string> vs;
typedef map<int,int> mii;
typedef map<ll,ll> mll;

template<typename T> ostream& operator<< (ostream &o,vector<T> v){
    if (v.size()>0)	o<<v[0];
    for (unsigned i=1;i<v.size();i++)	o<<" "<<v[i];
    return o<<endl;
}
template<typename U,typename V> ostream& operator<< (ostream &o,pair<U,V> p){
    return o<<"("<<p.first<<", "<<p.second<<") ";
}
template<typename T> istream& operator>> (istream &in,vector<T> &v){
    for (unsigned i=0;i<v.size();i++)	in>>v[i];
    return in;
}

int t;
int c,d,ac,aj;
int main(){
      freopen("B-small-attempt1.in","r",stdin);
      freopen("B-small.out","w",stdout);
      // freopen("B-large.in","r",stdin);
      // freopen("B-large.out","w",stdout);
      cin>>t;
      rep(testcase,t){
        cout<<"Case #"<<testcase+1<<": ";
        cin>>ac>>aj;
        if(ac==1 || aj==1){
          rep(i,ac+aj) cin>>c>>d;
          cout<<"2";
        }
        if(ac==2 || aj==2){
            int a[2],b[2];
            cin>>a[0]>>b[0];
            cin>>a[1]>>b[1];
            sort(a,a+2);
            sort(b,b+2);
            if(b[1]-a[0]<=720) cout<<"2";
            else if(1440+b[0]-a[1]<=720) cout<<"2";
            else cout<<"4";
        }
        cout<<"\n";
      }
      return 0;
}
