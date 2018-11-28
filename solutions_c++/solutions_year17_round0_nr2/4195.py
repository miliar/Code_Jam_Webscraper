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
string s,tmp;
int main(){
      ios_base::sync_with_stdio ( false );
      freopen("B-large.in","r",stdin);
      freopen("B-large.out","w",stdout);
      cin>>t;
      rep(testcase,t){
        cin>>s;
        int len=s.size();
        if(len==1){
          cout<<"Case #"<<testcase+1<<": "<<s<<"\n";
          continue;
        }
        tmp.assign(s);
        rep(i,len){
          int tmp1=tmp[i];
          bool check1=false,check2=false;
          reu(j,i+1,len){
            if(tmp[j]>tmp1){
              check1=true;
              break;
            }
            if(tmp[j]<tmp1){
              check2=true;
              tmp[i]=tmp[i]-1;
              reu(k,i+1,len) tmp[k]='9';
              break;
            }
          }
          if(check1) continue;
          if(check2) break;
        }
        cout<<"Case #"<<testcase+1<<": ";
        bool check=false;
        rep(i,len){
          if(tmp[i]!='0') check=true;
          if(check) cout<<tmp[i];
        }
        cout<<"\n";
      }
      return 0;
}
