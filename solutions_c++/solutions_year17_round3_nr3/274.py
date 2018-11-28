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
	string file("C");
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

void calc(ifstream &fin, ofstream &fout) {
  long K;
  fin >> K >> K;
  vector<long> P;
  double a;
  fin >> a;
  long U = (long)(a*10000+0.0001);
  for(int i=0;i<K;i++) {
    double a;
    fin >> a;
    long b = (long)(a*10000+0.0001);
    P.push_back(b);
  }
  sort(P.begin(), P.end());
  long uleft=U, pt=0, i=0;
  for(int j=0;j<K;j++) {
    if((P[j]-pt)*j <= uleft) {
      uleft-=(P[j]-pt)*j;
      pt=P[j];
      i=j;
    } else 
      break;
  }

  double prob=1.0;
  for(int j=0;j<K;j++) {
    double mult;
    if(j<=i)
      mult =(1.0/10000.0)*(pt+(0.0+ uleft*1.0)/(i+1.0));
    else
      mult =(1.0/10000.0)*P[j];
    if(mult>1.0) {
      cerr << mult << endl;
      mult=1.0;
    }
    prob*=mult;
  }
  fout << fixed << prob << endl;
}

