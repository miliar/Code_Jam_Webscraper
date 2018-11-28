#include<iostream>
#include<cstring>
#include<string>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<unordered_map>
#include<list>
#include<utility>
#include<algorithm>

#define NN 1000

using LL = long long int;
using namespace std;

int cas, ca;

struct comp {
  bool operator()(LL a, LL b) {
    return a>b;
  }
};

LL n, k, a,b,x,ct;
set<LL, comp> s;
unordered_map<LL, LL> ctn;

void main2() {
  s.clear();
  ctn.clear();
  cin >> n >> k;
  LL cur = 0;
  s.insert(n);
  ctn[n] = 1;
  while (!s.empty()) {
    auto it = s.begin();
    x = *it;
    ct = ctn[x];
//    cout <<x <<" "<<ct<<endl;
    cur += ct;
    s.erase(it);
    a = x/2;
    b = (x-1)/2;
    s.insert(a);
    s.insert(b);
    ctn[a] += ct;
    ctn[b] += ct;

    if ( cur >= k) {
      cout<<a<<" "<<b<<endl;
      return;
    }
  }
  throw ca;
}

int main(int argc, char *argv[]) {
	cin>>cas;
  bool showtime = argc > 1;
  time_t starttime = 0;
  if (showtime) {
    time(&starttime);
  }
	for(ca = 1; ca<=cas; ++ca) {
    if (showtime) {
      cerr<<ca<<"/"<<cas<<" "<<time(NULL) - starttime<<endl;
    }
		cout<<"Case #"<<ca<<": ";
    main2();
	}
}
