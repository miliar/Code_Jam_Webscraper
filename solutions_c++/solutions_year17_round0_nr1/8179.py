#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <climits>
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define READ(x) std::cin >> (x);
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define min(a,b) (((a) < (b)) ? (a) : (b))
using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int main(){
  int t,c=1;
  std::cin >> t;
  while(t--){


    string s;
    int k,r=0;
    std::cin >> s;
    std::cin >> k;
    for(int i = 0; i<s.length()-k+1; i++){
      if(s[i]=='-'){
        for(int j = 0; j<k; j++)
          s[i+j] = (s[i+j]=='-')?'+':'-';
        r++;
      }
    }
    bool b = false;
    for(int i = 0; i<s.length(); i++){
      if(s[i]=='-') {
        b=true;
        break;
      }
    }

    if(!b)printf("Case #%d: %d\n", c++,r);
    else printf("Case #%d: IMPOSSIBLE\n", c++);

  }
}
