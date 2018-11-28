#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
typedef long long int ll;
string imp="IMPOSSIBLE";
string rr(string a, int k){
  string rv;
  REP(i,k) rv+=a;
  return rv;
}
string place_before(string s, char what, string with) {
  REP(i,s.size()) if(s[i]==what) {
    return s.substr(0,i)+with+s.substr(i);
  }
}
string s1(vector<string> V) {

}
string solve() {
  int n,r,o,y,g,b,v;
  cin>>n>>r>>o>>y>>g>>b>>v;
  r-=g;
  b-=o;
  y-=v;
  int sum=r+o+y+g+b+v;
  if(r<0 || b<0 || y<0) return imp;
  if(sum==g && r==0) return rr("RG",g);
  if(sum==o && b==0) return rr("BO",o);
  if(sum==v && y==0) return rr("YV",v);
  if(g && !r) return imp;
  if(v && !y) return imp;
  if(o && !b) return imp;
  
  vector<pair<int, string> >V;
  V.push_back(make_pair(r,"R"));
  V.push_back(make_pair(b,"B"));
  string s;
  V.push_back(make_pair(y,"Y"));
  sort(V.begin(), V.end());
  REP(ooo, r+b+y) {
    if(V[0].first>V[1].first) swap(V[1],V[0]);
    int z=s.size()-1;
    for(int i=2;i>=0;--i) {
      if(V[i].first && s[z]!=V[i].second[0]) {
        s+=V[i].second;
        V[i].first--;
        break;
      }
      if(i==0) return imp;
    }
  }
  if(s[0]==s[s.size()-1]) return imp;

/*
  int d=V[2].first+V[1].first-V[0].first;
  if(d<0 || d%2) return imp;
  int k1=d/2;
  int k0=V[2].first-k1;
  if (k0<0 || k1<0 || k0>V[0].first || k1>V[1].first) return imp;
  REP(i,k0) s+=V[2].second+V[0].second;
  REP(i,k1) s+=V[2].second+V[1].second;
  REP(i,V[1].first-k1) s+=V[0].second+V[1].second;
  */

  if(g) s=place_before(s, 'R',rr("RG",g));
  if(v) s=place_before(s, 'Y',rr("YV",v));
  if(o) s=place_before(s, 'B',rr("BO",o));



  return s; 



}
int main() {
  int t;cin>>t;REP(i,t) {
    cout<<"Case #"<<(i+1)<<": ";
    cout<<solve()<<endl;
  }

}
