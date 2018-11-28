# include <cstdlib>
# include <cstdio>
# include <iostream>
# include <cmath>
# include <vector>
# include <map>
# include <set>
# include <sstream>
# include <queue>

using namespace std;

#define __ ios_base::sync_with_stdio(0); cin.tie(0);

template <class T> int toInt(const T &x){
  stringstream s; s << x; int r; s >> r; return r;
}

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }

int main(){
  int T; cin >> T;
  for(int t = 1; t <= T; ++t){
    int n,k;
    cin >> n >> k;
    priority_queue<int> Q;
    Q.push(n);
    int a = 0, b = 0;
    for(int i = 0; i < k; ++i){
      int interval = Q.top();
      Q.pop();
      //cout << interval << endl;
      if(interval % 2 == 0){
        int mleft = (interval / 2) - 1;
        int mright = interval / 2;
        Q.push(mleft); Q.push(mright);
        a = max(mleft, mright);
        b = min(mleft, mright);
      }
      else{
        int mleft = (interval / 2);
        int mright = interval / 2;
        Q.push(mleft); Q.push(mright);
        a = max(mleft, mright);
        b = min(mleft, mright);
      }
    }
    cout << "Case #" << t << ": " << a << " " << b << endl;
  }
  return 0;
}
