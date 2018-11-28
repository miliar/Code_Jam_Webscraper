#include <bits/stdc++.h>
using namespace std;


int main() {
  int T;
  cin >> T;
  for(int cs=1;cs<=T;cs++) {
    cout << "Case #" << cs  << ": ";
    long long n, k, mx, mn, c1=1,c2=0;
    cin >> n >> k;
    mx = n;
    mn = -1;
    long long t = 1;
    while(k>t) {
      k -= t;
      t *= 2;
      mx--;
      mn--;
      long long y = mx/2;
      long long x = mx - y;
      long long Y = mn/2;
      long long X = mn-Y;
      long long c=c1, d=c2;
      map<long long, long long > m;
      map<long long, long long > :: iterator it;
      m[y]+=c1;
      m[x]+=c1;
      if(mn>0) 
	m[X]+=c2, m[Y]+=c2;
      it = m.begin();
      mx = (*it).first;
      c1 = (*it).second;
      if(m.size()>1) {
	it++;
	mn = (*it).first;
	c2 = (*it).second;
	swap(mx, mn);
	swap(c1,c2);
      }
      else mn = -1, c2=0;
    }
    if(k>c1) n = mn;
    else n = mx;
    n--;
    mn = n/2;mx = n-mn;
    cout << mx << " " << mn << endl;
  }
}
