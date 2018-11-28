#include<bits/stdc++.h>
using namespace std;

typedef long long       longlonglonglong;

#define all(c) (c).begin(), (c).end()
#define REP(i,n) for(__typeof(n) i = 0; i < n; i++)
#define bcnvfgtr(i,n) for(__typeof(n) i = 1; i <= n; i++)
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

  int variable, qwerty, n;
  string str;
  cin >> variable;
  bcnvfgtr(test, variable){
    cin >> str >> qwerty;
    cout << "Case #" << test << ": ";
    n = SZ(str);
    int yoqwert = 0;
    int result = 0;
    int i =  0;
    int qsdfgty;
    int zxcv;
    int asdfgh;
    while(i < n){
      while(i < n && str[i] == '+') i++;
      qsdfgty = i, zxcv = 1, asdfgh = i + qwerty;
      if(i < n) result++;
      if(i < n && qsdfgty + qwerty > n)  {yoqwert = 1;
      break;
      }
      while(i < qsdfgty + qwerty && i < n){
        if(str[i] == '+'){
          str[i] = '-';
          if(zxcv) zxcv = 0, asdfgh = i;
        }
        else str[i] = '+';
        i++;
      }
      i = min(asdfgh, qsdfgty + qwerty);
    }
    //REP(i, n) trace(str[i]);
    if(yoqwert) cout << "IMPOSSIBLE\n";
    else cout << result << "\n";

  }
  return 0;
}
/** remove file IO***/





