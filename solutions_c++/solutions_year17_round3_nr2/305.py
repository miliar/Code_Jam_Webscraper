#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
  int T;
  cin >> T;

  for(int t = 0; t < T; t++) {

    int Ac, Aj;
    cin >> Ac >> Aj;

    vector< pair< pair<int, int>, char> > v;
    int current_c, current_j;

    current_c = current_j = 0;
    for(int i = 0; i < Ac; i++) {
      pair< pair<int, int>, char> p;
      cin >> p.first.first >> p.first.second;
      p.second = 'c';
      v.push_back(p);
      current_c += p.first.second - p.first.first;
    }

    for(int i = 0; i < Aj; i++) {
      pair< pair<int, int>, char> p;
      cin >> p.first.first >> p.first.second;
      p.second = 'j';
      v.push_back(p);
      current_j += p.first.second - p.first.first;
    }

    sort(v.begin(), v.end());

    vector<int> cc, cj, jj;
    for(int i = 0; i < v.size() - 1; i++) {
      if(v[i].second == 'c' && v[i+1].second == 'c') {
        cc.push_back(v[i+1].first.first - v[i].first.second);
      }else if(v[i].second == 'j' && v[i + 1].second == 'j') {
        jj.push_back(v[i+1].first.first - v[i].first.second);
      }else {
        cj.push_back(v[i+1].first.first - v[i].first.second);
      }
    }

    if(v.back().second == 'c' && v.front().second == 'c'){
      cc.push_back(v.front().first.first + 1440 - v.back().first.second);
    }else if(v.back().second == 'j' && v.front().second == 'j') {
      jj.push_back(v.front().first.first + 1440 - v.back().first.second);
    }else {
      cj.push_back(v.front().first.first + 1440 - v.back().first.second);
    }



    sort(cc.begin(), cc.end());
    sort(jj.begin(), jj.end());
    sort(cj.begin(), cj.end());


    int possible_c_fill = 0;
    for(int i = 0; i < cc.size(); i++) {
      current_c += cc[i];
      if(current_c <= 720) {
        possible_c_fill = i + 1;
      }else {
        break;
      }
    }


    int possible_j_fill = 0;
    for(int i = 0; i < jj.size(); i++) {
      current_j += jj[i];
      if(current_j <= 720) {
        possible_j_fill = i + 1;
      }else {
        break;
      }
    }

    cout << "Case #" << t + 1 << ": ";
    cout << (cc.size() - possible_c_fill) * 2 + (jj.size() - possible_j_fill) * 2 + cj.size() << endl;

  }

}
