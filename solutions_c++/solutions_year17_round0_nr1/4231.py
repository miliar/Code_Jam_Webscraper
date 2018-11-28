#pragma GCC optimize("O3")
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
int main(){
      ios_base::sync_with_stdio ( false );
      freopen("A-large.in","r",stdin);
      freopen("A-large.out","w",stdout);
      cin>>t;
      rep(testcase,t){
        string s;
        int k,flips=0;
        cin>>s>>k;
        for(int i=s.size()-1;i>=k-1;i--){
          if(s[i]=='-'){
            flips++;
            for(int j=i;j>=i-k+1;j--){
              if(s[j]=='-') s[j]='+';
              else s[j]='-';
            }
          }
        }
        int tmp=s[0];
        bool check=true;
        reu(i,1,k){
          if(s[i]!=tmp){
            cout<<"Case #"<<testcase+1<<": "<<"IMPOSSIBLE\n";
            check=false;
            break;
          }
        }
        if(check) cout<<"Case #"<<testcase+1<<": "<<flips<<"\n";
      }
      return 0;
}
