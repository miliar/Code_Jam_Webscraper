#include <bits/stdc++.h>

using namespace std;

#define siz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define foreach(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define rep(i,a,b) for (int i=(a),_ed=(b);i<_ed;i++)
#define per(i,a,b) for (int i=(b)-1,_ed=(a);i>=_ed;i--)

typedef long long ll;
typedef unsigned long long ull;

int T,N,K;
priority_queue<int, vector<int>, less<int> > q;

int main()
{
#ifndef ONLINE_JUDGE
//  freopen("C-small-1-attempt0.in","r",stdin);
//  freopen("C.out","w",stdout);
#endif
  cin >> T;
  rep(cas, 1, T+1) {
    cout << "Case #" << cas << ": ";
    cin >> N >> K;
    while(!q.empty()) q.pop();
    q.push(N);
    rep(test, 1, K) {
      int tt = q.top(); q.pop();
      if(tt&1) {
        q.push(tt/2);
        q.push(tt/2);
      } else {
        q.push(tt/2);
        q.push(tt/2 - 1);
      }
    }
    int ans = q.top();
    int y,z;
    if(ans&1) {
      y = z = ans/2;
    } else {
      y = ans/2;
      z = y-1;
    }
    cout << y << ' ' << z << endl;
  }

//  cout<<"time: "<<(ll)clock()*1000/CLOCKS_PER_SEC<<" ms"<<endl;

  return 0;
}

