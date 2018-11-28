#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <queue>
#include <map>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
  int t;
  long long n, k;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    vector<long long> intVec;
    map<long long, long long> m;
    bool needSort = false;
    long long ls, rs, temp;
    cin >> n >> k;  // read n and then m.
    m[n] = 1;
    while(k > 0) {
      ls = n / 2;
      rs = n - ls;
      if(n % 2 == 0) {
        ls--;
      }
      else {
        rs--;
      }

      map<long long, long long>::iterator it = m.find(ls);
      if(it != m.end())
      {
        temp = it->second;
        temp += m[n];
      }
      else {
        temp = m[n];
        intVec.push_back(ls);
        needSort = true;
      }
      m[ls] = temp;

      if(ls == rs) {
        temp += m[n];
        m[ls] = temp;
      }
      else {
        map<long long, long long>::iterator it = m.find(rs);
        if(it != m.end())
        {
          temp = it->second;
          temp += m[n];
        }
        else {
          temp = m[n];
          intVec.push_back(rs);
          needSort = true;
        }
        m[rs] = temp;
      }
      if(needSort) {
        sort(intVec.begin(), intVec.end());
        needSort = false;
      }
      k -= m[n];
      n = intVec.back();
      intVec.pop_back();
    }
    cout << "Case #" << i << ": " << max(ls,rs) << " " << min(ls,rs) << endl;
  }
  return 0;

}
