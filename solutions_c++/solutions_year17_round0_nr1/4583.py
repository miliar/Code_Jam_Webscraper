#include<iostream>
#include<queue>
using namespace std;

#define sz(X) (int)X.size()

int main() {
  int t, k;
  cin >> t;
  for(int c=1;c<=t;++c) {
    string s;
    cin >> s >> k;
    char cur = '+', other = '-';
    queue<int> q;
    int ret = 0;
    for(int i=0;i<sz(s);++i) {
      if(!q.empty() && i == q.front()) {
        swap(cur, other);
        q.pop();
      }
      if(i<=sz(s)-k) {
        if(s[i]!= cur) {
          ret++;
          swap(cur, other);
          q.push(i+k);
        }
      } else if(s[i]!=cur) {
        ret = -1;
      }
    }
    cout << "Case #" << c << ": " <<
      (ret==-1?"IMPOSSIBLE":to_string(ret)) << endl;
  }
  return 0;
}
