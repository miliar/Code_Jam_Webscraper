#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <cassert>
#include <cstring>
#include <cstddef>
#include <climits>
#define _USE_MATH_DEFINES // for C++
#include <cmath>

using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

vector<string> split(const string& s, char c) {
  vector<string> v;
  stringstream ss(s);
  string x;
  while (getline(ss, x, c))
    v.emplace_back(x);
  return move(v);
}

void err(vector<string>::iterator it) {}
template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
  cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
  err(++it, args...);
}

const long long mod = 1000000007;
long long powmod(long long a,long long b) {long long res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}


int main(){
  cout.precision(10);
  cout << fixed;

#ifdef LOCAL_DEFINE
  FILE *fin = freopen("A.in", "r", stdin);
  assert(fin != NULL);
  FILE *fout = freopen("A.ans", "w", stdout);
#endif

  int T;
  cin >> T;

  for(int testcase = 1; testcase <= T; testcase++){
    int r, c;
    cin >> r >> c;

    multimap< char, pair< pair<int, int>, pair<int, int> > > om;
    map< char, pair<int, int> > mm;
    vector< vector<char> > a(r, vector<char>(c));
    for(int i = 0; i < r; i++){
      for(int j = 0; j < c; j++){
        cin >> a[i][j];
        if(a[i][j] != '?'){
          mm[ a[i][j] ] = {i, j};
          if(a[i][j] == 'B'){
            cerr << "b = " << i << " " << j << endl;
          }
        }
      }
    }

    for(auto au : mm){
      char ch = au.first;
      pair<int, int> p = au.second;

      pair<int, int> p1, p2;
      int s = 0;
      for(int i = 0; i < r; i++){
        if(i > p.first){
          break;
        }
        for(int j = 0; j < c; j++){
          if(j > p.second){
            break;
          }
          for(int x = p.first; x < r; x++){
            for(int y = p.second; y < c; y++){
              bool valid = true;
              for(auto ot : mm){
                if(ot.first == ch){
                  continue;
                }

                if(((i <= ot.second.first) && (j <= ot.second.second)
                      && (x >= ot.second.first) && (y >= ot.second.second))){
                  valid = false;
                  break;
                }
              }

              for(auto ot : om){
                if(ot.first == ch){
                  continue;
                }

                for(int a = ot.second.first.first; a <= ot.second.second.first; a++){
                  for(int b= ot.second.first.second; b <= ot.second.second.second; b++){
                    if(((i <= a) && (j <= b)
                          && (x >= a) && (y >= b))){

                      if(ch == 'B'){
                        cerr << "|false " << i << " " << j << " " << x << " " << y << " " << a << " " << b << endl;
                      }
                      valid = false;
                      break;
                    }
                  }
                }
                /* if(ch == 'B'){ */
                /*   cerr << "|check " << i << " " << j << " " << x << " " << y << endl; */
                /*   cerr << "|2 " << ot.first << " " << ot.second.first << " " << ot.second.second << endl; */
                /* } */
              }


              if(valid){
                if(s < (x - i + 1) * (y - j + 1)){
                  p1 = {i, j};
                  p2 = {x, y};
                  s = (x - i + 1) * (y - j + 1);
                  if(ch == 'B')
                    error(p1.first, p1.second, p2.first, p2.second);

                }
              }
            }
          }
        }
      }

      for(int i = p1.first; i <= p2.first; i++){
        for(int j = p1.second; j <= p2.second; j++){
          a[i][j] = ch;
          cerr << "a[" << i << "][" << j << "]=" << a[i][j] << endl;
        }
      }
      cerr << "| " << ch << " " << p1.first << " " << p1.second << endl;
      cerr << "| " << ch << " " << p2.first << " " << p2.second << endl;
      om.insert({ch, {p1, p2}});
    }

    cout << "Case #" << testcase << ":" << endl;
    for(int i = 0; i < r; i++){
      for(int j = 0; j < c; j++){
        cout << a[i][j];
      }
      cout << "\n";
    }
  }


#ifdef LOCAL_DEFINE
  cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
}

