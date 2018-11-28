#include <bits/stdc++.h>
#include <iostream>

using namespace std;


string solveRYB(int r, int y, int b) {
  //cout << "solve " << r << y << b;
  vector<pair<int, char>> things {{r, 'R'}, {y, 'Y'}, {b, 'B'}};
  for(int i = 0; i < 3; i++) {
    bool good = true;
    int sum = 0;
    int x = -1, y = -1;
    for(int j = 0; j < 3; j++) {
      if(j == i)
        continue;
      if(x == -1) {
        x = j;
      }
      else {
        y = j;
      }

      sum += things[j].first;
      if(things[j].first > things[i].first)
        good = false;
    }
    if(sum < things[i].first)
      good = false;

    if(good) {
      stringstream ans;
      for(int a = 0; a < things[i].first; a++) {
        ans << things[i].second;
        if(a < things[x].first) {
          ans << things[x].second;
        }
        if(a >= things[i].first - things[y].first) {
          ans << things[y].second;
        }
      }
      //cout << ans.str();
      return ans.str();
    }
  }
  return "";
}

int main() {
  int loops;
  cin >> loops;
  for(int loop = 1; loop <= loops; loop++) {
    int n;
    int r, o, y, g, b, v;
    cout << "Case #" << loop << ": ";
    cin >> n >> r >> o >> y >> g >> b >> v; 
    if(r + g + v + y == 0 && b == o) {
      for(int i = 0; i < b; i++) {
        cout << "BO" ;
      }
      cout<< endl;
    }
    else if(r + g + b + o == 0 && v == y) {
      for(int i = 0; i < y; i++) {
        cout << "VY" ;
      }
      cout << endl;
    }
    else if(o + b + v + y == 0 && g == r) {
      for(int i = 0; i < r; i++) {
        cout << "RG";
      }
      cout << endl;
    }

    else if((r <= g && r > 0) || (y <= v && y > 0) || (b <= o && b > 0)) {
      cout << "IMPOSSIBLE" << endl;
    }
    else {
      string ans = solveRYB(r - g, y - v, b - o);
      if(ans.length() == 0) {
      cout << "IMPOSSIBLE" << endl;
      }
      else {
        map<char, pair<int, char>> dump;
        dump['R'] = {g, 'G'};
        dump['Y'] = {v, 'V'};
        dump['B'] = {o, 'O'};       
        for(u_int i = 0; i < ans.length(); i++) {
          while(dump[ans[i]].first > 0) {
            cout << ans[i] << dump[ans[i]].second;
            dump[ans[i]].first--;
          }
          cout << ans[i];
        }
        cout << endl;
      }
    }
  }
}
