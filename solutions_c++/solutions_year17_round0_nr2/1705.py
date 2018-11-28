#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <string>
#include <unordered_map>
#include <utility>
#include <algorithm>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
using namespace std;

typedef pair<int, int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef long long ll;

#define fi first
#define se second
#define pb push_back
#define rep(i, a, b) for(int (i)=(a); (i)<(b); (i)++)

const int INF = 0x3f3f3f3f;


int main(){
  cin.sync_with_stdio(0);
  cin.tie(nullptr);
  
  int n;
  string s;
  cin >> n;
  rep(kase, 1, n+1){
    cin >> s;
    for (;;){
      int found = false;
      rep (i, 0, s.length()-1){
        if (s[i] > s[i+1]){
          s[i]--;
          rep (j, i+1, s.length())
            s[j] = '9';
          found = true;
          break;
        }
      }
      if (!found)
        break;
    }
    int start = 0;
    while (s[start] == '0')
      start++; 
    cout << "Case #" << kase << ": " << s.substr(start) << endl;
  }
  return 0;
  
}  
