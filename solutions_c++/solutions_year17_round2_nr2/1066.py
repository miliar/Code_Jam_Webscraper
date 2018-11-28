#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct ranky{
  pair<int, char>first;
  pair<int, char>second;
  pair<int, char>third;
  ranky(int r, int y, int b){
    pair<int, char>R1(r, 'R');
    pair<int, char>Y1(y, 'Y');
    pair<int, char>B1(b, 'B');
    vector<pair<int, char> >colours = {R1, Y1, B1};
    sort(colours.begin(), colours.end());
    first = colours[2];
    second = colours[1];
    third = colours[0];
  }
};


int main(){
  ios_base::sync_with_stdio(false);
  int T;
  int n, r, o, y, g, b, v;
  cin >> T;
  for(int ind=0; ind<T; ind++){
    cin >> n >> r >> o >> y >> g >> b >> v;
    ranky Ra(r, y, b);
    string ans(n, ' ');
    cout << "Case #" << (ind+1) << ": ";
    if(Ra.first.first > n/2) cout << "IMPOSSIBLE" << endl;
    else {
      for(int i=0; i<Ra.first.first; i++)
        ans[2*i] = Ra.first.second;
      int j = 2*Ra.first.first-1;
      for(;j<n; j+=2){
        ans[j] = Ra.second.second;
        Ra.second.first--;
      }
      for(j=0; j<Ra.second.first; j++)
        ans[2*j+1] = Ra.second.second;
      int count=0;
      for(j=0; j<n; j++)
        if(ans[j] == ' '){
          count ++;
          ans[j] = Ra.third.second;
        }
      if(count!=Ra.third.first)
        cout << "worng" << endl;
      cout << ans << endl;
    }
  }
    
  return 0;
}