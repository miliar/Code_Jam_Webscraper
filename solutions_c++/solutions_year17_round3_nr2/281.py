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
#include <numeric>
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
	string file("B");
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
  long C, J;
  fin >> C >> J;
  long totc=0, totj=0, flex=0, swp=0;
  vector<long> start, end;
  vector<char> whose;
  vector<long> ctimes, jtimes;
  vector<pair<long, long> > order;
  for(int i=0;i<C+J;i++) {
    long a, b;
    fin >> a >>b;
    start.push_back(a);
    end.push_back(b);
    whose.push_back((i<C)?'c':'j');
    order.push_back(make_pair(a, i));
  }
  sort(order.begin(), order.end());

  long lasttime=end[order[order.size()-1].second]-1440;
  char lastparent=whose[order[order.size()-1].second];
  for(int i=0;i<C+J;i++) {
    long me=order[i].second;
    long pre = start[me]-lasttime;
    if(lastparent != whose[me]) {
      flex+=pre;
      swp++;
    } else {
      if(whose[me]=='c')
        ctimes.push_back(pre);
      else
        jtimes.push_back(pre);
    }
    long mytime=end[me]-start[me];
    if(whose[me]=='c')
      totc+=mytime;
    else
      totj+=mytime;
    lasttime=end[me];
    lastparent=whose[me];
  }
  long ctimetot = accumulate(ctimes.begin(), ctimes.end(), 0);
  long jtimetot = accumulate(jtimes.begin(), jtimes.end(), 0);
  sort(ctimes.begin(), ctimes.end());
  sort(jtimes.begin(), jtimes.end());
  cerr << ctimetot + jtimetot + totc+ totj+flex << endl;

  long error=0;
  vector<long> errors;
  if(totj+jtimetot > 720) {
    error = totj+jtimetot - 720;
    errors=jtimes;
  } else if (totc + ctimetot > 720) {
    error = totc+ctimetot - 720;
    errors=ctimes;
  }
  if (error)
    for(int i=errors.size()-1;error>0;i--) {
      error-=errors[i];
      swp+=2;
    }

  fout << swp << endl;

}
