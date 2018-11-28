#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>
#define MAXX 1100

using namespace std;


string str;
bool happy[MAXX];

int main(){

  freopen("io/gcj17a_big_in.txt", "r", stdin);
  freopen("io/gcj17a_big_out.txt", "w", stdout);

  int kases, i, j, k;
  cin >> kases;

  for(i = 0; i < kases; i++){
    cin >> str >> k;

    int l = str.size();

    for(j = 0; j < l; j++){
      if(str[j] == '+') happy[j] = true;
      else happy[j] = false;
    }

    int ans = 0;

    for(j = 0; j+k-1 < l; j++){
      if(!happy[j]){
        ans++;
        for(int p = j; p <= j+k-1; p++){
          happy[p] = 1-happy[p];
        }
      }
    }
    bool is_h = true;
    for(j = 0; j < l; j++){
      //cout << happy[j] << endl;
      if(!happy[j]){
        is_h = false;
        //cout << ans << endl;
        cout << "Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        break;
      }
    }
    if(is_h){
      cout << "Case #"<<i+1<<": "<<ans<<endl;
    }
  }

  return 0;
}
