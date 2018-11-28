
#include <iostream>
#include <iomanip>

#define INF -1000000000

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;

  for(int c = 1; c <= t; c++){
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    // n, r, y, b
    string ans = "";
    while(r--)
      ans += "R";
    while(y--)
      ans += "Y";
    while(b--)
      ans += "B";

    bool impo = false;
    int count = 0;
    for(int i = 0; i < ans.length(); i++){
      // cout << i << " " << ans << endl;
      if(ans[(i - 1 + ans.length()) % ans.length()] == ans[i]
        || ans[(i + 1) % ans.length()] == ans[i]){

        bool ok = false;
        for(int j = 0; j < ans.length(); j++){
          if(ans[j] != ans[i] && ans[(j + 1) % ans.length()] != ans[i]){
            // cout << i << " " << j << endl;
            // cout << ans << endl;
            ans.insert(ans.begin() + j + 1, ans[i]);
            // cout << ans << endl;

            if(i > j)
              i++;

            ans.erase(ans.begin() + i);
            // cout << ans << endl;

            if(i > j)
              i--;

            ok = true;

            break;
          }
        }
        if(!ok){
          impo = true;
          break;
        }
        i--;
        count++;
        if(count >= ans.length()){
          impo = true;
          break;
        }
      }
    }
    if(impo && ans.length() > 1)
      cout << "Case #" << c << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << c << ": " << ans << endl;

  }



  return 0;
}
