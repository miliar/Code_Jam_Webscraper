/* Brian's GCJ entries */
#include <vector>
#include <iterator>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <set>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <chrono>
using namespace std;
typedef long long ll;
int bitct(long r) {int c=0; for(; r; r&=r-1) c++; return c;}
long gcd(long x, long y) {return x ? gcd(y%x,x) : y;}
long choose(long n, long q) { if(n==0 || q==0) return 1;
  if (q==1) return n; else return ( choose(n, q-1) * (n-q+1 ) /q); }
template<typename T> ostream& operator << (ostream &o,vector<T> v) {o<<"[";
	int i=0,s=v.size();for(;i+1<s;i++)o<<v[i]<<", ";if(s)o<<v[i];o<<"]";return o;}
template<typename K, typename V> ostream& operator << (ostream &o,
  unordered_map<K, V> m) {o<<"h{";for(auto i:m)o<<i.first<<" -> "<< i.second <<
  ", "; o<<"}";return o;}
template<typename K, typename V> ostream& operator << (ostream &o, map<K, V> m)
  {o<<"{";for(auto i:m)o<<i.first<<" -> "<< i.second << ", "; o<<"}";return o;}
template<typename K> ostream& operator << (ostream &o, set<K> m) 
  {o<<"#{";for(auto i:m)o<<i<< ", "; o<<"}";return o; }
template<typename K> ostream& operator << (ostream &o, unordered_set<K> m) 
  {o<<"#h{";for(auto i:m)o<<i<< ", "; o<<"}";return o;}
template<typename T> ostream& printv(vector<T> v) {int i=0,s=v.size();
  for(;i+1<s;i++)cout<<v[i]<<" ";if(s)cout<<v[i];return cout;}
//int dx[8] = {0,  1,  1,  1,  0, -1, -1, -1}
//int dy[8] = {1,  1,  0, -1, -1, -1,  0,  1}
int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};

void calc(ifstream &, ofstream &);
int main() { stringstream filename, fnamein, fnameout;
  typedef std::chrono::duration<int,std::milli> ms;
	string file("A");
	filename << file << "-small.";
	fnamein << filename.str() << "in"; fnameout << filename.str() << "out";
	ifstream fin(fnamein.str().c_str()); ofstream fout(fnameout.str().c_str());
	int count;
	fin >> count;
	for(int i=0;i<count;i++) {
		fout << "Case #" << (i+1) << ": ";
    chrono::steady_clock::time_point t0 = chrono::steady_clock::now();
		calc(fin, fout);
    chrono::steady_clock::time_point t1 = chrono::steady_clock::now();
    cerr << "CASE" << (i+1) << " " << 
      (chrono::duration_cast<ms>(t1-t0)).count() << endl;
		fout.flush(); }
	fin.close(); fout.close(); }

ll mkst(vector<ll> &l) {
  ll out=0, tot=0;
  int i=0, base=1;
  while(i<l.size()) {
    out+=l[i]*base;
    base*=101;
    tot+=l[i];
    i++;
  }
  out+=tot*base;
  return out;
}

vector<ll> gst(ll in, ll P) {
  vector<ll> out(P,0);
  for(int i=0;i<P;i++) {
    out[i]=in%101;
    in=in/101;
  }
  return out;
}

void calc(ifstream &fin, ofstream &fout) {
  ll N, P;
  fin >> N >> P;
  vector<ll> mods(P, 0);
  for(int i=0;i<N;i++) {
    ll x;
    fin >> x;
    mods[x%P]++;
  }

  ll tott = 0;
  for(int i=1;i<P;i++)
    tott+=mods[i]*i;
  if(tott==0) {
    fout << mods[0] << endl;
    return;
  }


  /* cerr << mods << mkst(mods) << '\n' << gst(mkst(mods), P) << endl; */

  map<ll, ll> state;
  ll freewins=mods[0];
  mods[0]=0;
  ll st0 = mkst(mods);
  state[st0]=1+freewins;
  while(state.size() > 1 || state.begin()->first != 0) {
    auto mep = (--state.end());
    vector<ll> me = gst(mep->first, P);
    ll value=mep->second;
    ll totme=tott;
    for(int i=1;i<P;i++)
      totme-=me[i]*i;

    /* if(totme%P==0) */
    /*   value++; */
    for(int i=1;i<P;i++) {
      if(me[i]==0) continue;
      me[i]--;
      ll newst=mkst(me);
      ll myvalue = value + ((newst!=0 && (0==(totme+i)%P))?1:0);
      //cerr << myvalue << " " << totme+i << " " << me << " " << newst << endl;
      if(state[newst] < myvalue)
        state[newst]=myvalue;
      me[i]++;
    }
    state.erase(mep);

  }

  fout << state.begin()->second << endl;
}
