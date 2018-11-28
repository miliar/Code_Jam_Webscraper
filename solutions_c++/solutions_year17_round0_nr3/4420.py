#include<bits/stdc++.h>
using namespace std;

typedef long long       LL;

#define all(c) (c).begin(), (c).end()
#define REP(i,n) for(__typeof(n) i = 0; i < n; i++)
#define asdfg(i,n) for(__typeof(n) i = 1; i <= n; i++)
#define REPn(i,j,n) for(__typeof(n) i = j; i < n; i++)
#define tr(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define SZ(c) (int)(c).size()
#define iOS ios_base::sync_with_stdio(false)
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define MT make_tuple


int main(){
  freopen("input.in", "r", stdin);
  freopen("output.out", "w", stdout);
  int testcasesesese;
  LL qwsa;
  LL k;
  cin >> testcasesesese;
  asdfg(test, testcasesesese){
    cin >> qwsa >> k;
    priority_queue<LL, vector<LL> >mbnvmkd;
    mbnvmkd.push(qwsa);
    cout << "Case #" << test << ": ";
    while(1){
      LL qwerty = mbnvmkd.top();
      if(k == 1){
        qwerty--;
        LL xcv = max(qwerty/2, qwerty - qwerty/2);
        LL mannr = min(qwerty/2, qwerty - qwerty/2);
        cout << xcv << " " << mannr;
        break;
      }
      if(qwerty == 0){
        cout << "0";
        break;
      }
      qwerty--;
      LL temp = qwerty/2;
      mbnvmkd.push(temp);
      mbnvmkd.push(qwerty - temp);
      mbnvmkd.pop();
      k--;
    }
    cout << "\n";
  }
  return 0;
}
/** remove file IO***/





