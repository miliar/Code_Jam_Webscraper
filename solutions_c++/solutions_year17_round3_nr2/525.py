#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
  int T;
  int A0,A1;
  int s[201],e[201],id[201];

  cin >> T;

  for(int tc = 1;tc <= T;++tc){
    cin >> A0 >> A1;

    for(int i = 0;i < A0;++i){
      cin >> s[i] >> e[i];
      id[i] = 0;
    }

    for(int i = 0;i < A1;++i){
      cin >> s[A0 + i] >> e[A0 + i];
      id[A0 + i] = 1;
    }

    int n = A0 + A1;

    for(int i = 0;i < n;++i){
      for(int j = i + 1;j < n;++j){
        if(s[i] > s[j]){
          swap(s[i],s[j]);
          swap(e[i],e[j]);
          swap(id[i],id[j]);
        }
      }
    }

    s[n] = s[0] + 1440;
    e[n] = e[0] + 1440;
    id[n] = id[0];
    ++n;

    int ans = 0;

    for(int i = 0;i + 1 < n;){
      int j = i + 1;

      while(j < n && id[j] == id[i]) ++j;

      if(j < n) ++ans;

      i = j;
    }

    int t[2];
    t[0] = t[1] = 0;

    for(int i = 0;i + 1 < n;++i){
      t[ 1 - id[i] ] += s[i + 1] - s[i];
    }

    //cout << t[0] << " " << t[1] << endl;

    if(t[0] != t[1]){
      int needs,x;
      if(t[0] > t[1]){
        x = 1;
        needs = (t[0] - t[1]) / 2;
      }else{
        x = 0;
        needs = (t[1] - t[0]) / 2;
      }

      //cout << x << " " << needs << endl;


      for(int i = 0;i + 1 < n;++i){
        if(id[i] == x && id[i + 1] == 1 - x)
          needs -= s[i + 1] - e[i];
      }

      if(needs > 0){
        vector<int> aux;

        for(int i = 0;i + 1 < n;++i){
          if(id[i] == x && id[i + 1] == x) aux.push_back(s[i + 1] - e[i]);
        }

        sort(aux.begin(),aux.end());

        while(!aux.empty() && needs > 0){
          int t = aux.back();
          //cout << "t = " << t << endl;
          aux.pop_back();
          needs -= t;
          ans += 2;
        }

        assert(needs <= 0);
      }
    }

    cout << "Case #" << tc << ": " << ans << endl;
  }

  return 0;
}
