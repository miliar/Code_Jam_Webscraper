#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>


using namespace std;

void flip(string &p,int i,int K);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    int T,K,count=0;
    string p;
    cin >> T;
    int j=0,i;
    char c;
    bool flag;
    for(int tc=1;tc <= T;tc++){
      cin >> p;
      cin >> K;
      cout << "Case #" << tc << ": ";
      int j=0;
      c = p[0];
      count = 0;
      for (i=0; i < p.length()-K+1;i++){
        if (p[i]=='-'){
          flip(p,i,K);
          count++;
        }
      }
      flag = true;
      while (flag && i<p.length()){
        if (p[i] == '-'){
          cout << "IMPOSSIBLE\n";
          flag = false;
        }
        i++;
      }
      if (flag)
        cout << count << '\n';
      count = 0;
    }

    return 0;
}

void flip(string &p,int i,int K){
  for (int j=0;j<K;j++)
    if (p[i+j]=='-')
      p[i+j] = '+';
    else
      p[i+j] = '-';
}
