#include<bits/stdc++.h>
using namespace std;

typedef long long       longlonglong;

#define all(c) (c).begin(), (c).end()
#define REP(i,n) for(__typeof(n) i = 0; i < n; i++)
#define mcnknckenc(i,n) for(__typeof(n) i = 1; i <= n; i++)
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
  longlonglong qas;
  longlonglong n;
  longlonglong i;
  cin >> qas;
  mcnknckenc(test, qas){
    cin >> n;
    vector<int> qwerty;
    while(n){
      qwerty.PB(n%10);
      n /= 10;
    }
    reverse(all(qwerty));
    while(1){
      i = 0, n = SZ(qwerty);
      while(i < n - 1){
        if(qwerty[i] > qwerty[i + 1]) break;
        else i++;
      }
      if(i < n - 1){
        if(qwerty[i] == 1 && i == 0){
          qwerty.erase(qwerty.begin());
          i = 0;
          while(i < n - 1)  qwerty[i++] = 9;
        }
        else{
          qwerty[i]--;
          i++;
          while( i < n) qwerty[i++] = 9;
        }
      }
      else break;
    }
    cout << "Case #" << test << ": ";
    for(auto it : qwerty)  cout << it;
    cout << "\n";
  }
  return 0;
}
/** remove file IO***/





