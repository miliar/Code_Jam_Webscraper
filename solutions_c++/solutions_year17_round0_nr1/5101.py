# include <cstdlib>
# include <cstdio>
# include <iostream>
# include <cmath>
# include <vector>
# include <map>
# include <set>
# include <sstream>
# include <queue>
#define __ ios_base::sync_with_stdio(0); cin.tie(0);

using namespace std;



template <class T> int toInt(const T &x){
  stringstream s; s << x; int r; s >> r; return r;
}

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }


int main(){
  int T; cin >> T;
  for(int t = 1; t <= T; ++t){
    string pancakes; cin >> pancakes;
    int k; cin >> k;
    int contplus = 0;
    for(int i = 0; i < pancakes.size(); ++i)
      contplus += (pancakes[i] == '+');

    //string tmp = pancakes;
    int moves1 = 0;
    for(int i = 0; i <= pancakes.size() - k; ++i){
      if(pancakes[i] == '-'){
        moves1++;
        for(int j = i; j <= i + k - 1; ++j){
          if(pancakes[j] == '-'){
            pancakes[j] = '+';
            contplus++;
          }
          else{
            pancakes[j] = '-';
            contplus--;
          }
        }
      }
    }
    if(contplus == pancakes.size())
      cout << "Case #" << t << ": " << moves1 << endl;
    else
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;

  }
  return 0;
}
