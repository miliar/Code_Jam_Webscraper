#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(), (x).end()

string solve_small(int R, int O, int Y, int G, int B, int V) {
  if(O || G || V) return "IMPOSSIBLE";
  if(R + Y < B || Y + B < R || B + R < Y) return "IMPOSSIBLE";

  vector<pair<int,string>> tmp(3);
  tmp[0] = make_pair(R, "R");
  tmp[1] = make_pair(Y, "Y");
  tmp[2] = make_pair(B, "B");
  sort(ALL(tmp));

  string s1;
  REP(i,tmp[1].first - tmp[0].first) s1 += tmp[1].second;
  REP(i,tmp[0].first) {
    s1 += tmp[0].second;
    s1 += tmp[1].second;
  }

  string res;
  REP(i,tmp[2].first) {
    res += tmp[2].second;
    res += s1[i];
  }
  res += s1.substr(tmp[2].first);

  return res;
}

string solve_large(int R, int O, int Y, int G, int B, int V) {
  int N = R + O + Y + G + B + V;

  string res;
  if(N == B + O) {
    if(B == O) {
      REP(i,B) {
        res += "B";
        res += "O";
      }
    }else{
      res = "IMPOSSIBLE";
    }
  }
  if(N == R + G) {
    if(R == G) {
      REP(i,R) {
        res += "R";
        res += "G";
      }
    }else{
      res = "IMPOSSIBLE";
    }
  }
  if(N == Y + V) {
    if(Y == V) {
      REP(i,Y) {
        res += "Y";
        res += "V";
      }
    }else{
      res = "IMPOSSIBLE";
    }
  }
  if(!res.empty()) return res;

  if(O && B <= O) return "IMPOSSIBLE";
  if(G && R <= G) return "IMPOSSIBLE";
  if(V && Y <= V) return "IMPOSSIBLE";

  string BB = "B", RR = "R", YY = "Y";
  REP(i,O) {
    BB += "O";
    BB += "B";
  }
  REP(i,G) {
    RR += "G";
    RR += "R";
  }
  REP(i,V) {
    YY += "V";
    YY += "Y";
  }
  B -= O;
  R -= G;
  Y -= V;

  if(R + Y < B || Y + B < R || B + R < Y) return "IMPOSSIBLE";

  vector<pair<int,string>> tmp(3);
  tmp[0] = make_pair(R, "R");
  tmp[1] = make_pair(Y, "Y");
  tmp[2] = make_pair(B, "B");
  sort(ALL(tmp));

  string s1;
  REP(i,tmp[1].first - tmp[0].first) s1 += tmp[1].second;
  REP(i,tmp[0].first) {
    s1 += tmp[0].second;
    s1 += tmp[1].second;
  }

  REP(i,tmp[2].first) {
    res += tmp[2].second;
    res += s1[i];
  }
  res += s1.substr(tmp[2].first);

  REP(i,res.length()) {
    if(res[i] == 'B') {
      res = res.substr(0, i) + BB + res.substr(i + 1);
      break;
    }
  }
  REP(i,res.length()) {
    if(res[i] == 'R') {
      res = res.substr(0, i) + RR + res.substr(i + 1);
      break;
    }
  }
  REP(i,res.length()) {
    if(res[i] == 'Y') {
      res = res.substr(0, i) + YY + res.substr(i + 1);
      break;
    }
  }

  return res;
}

int main(){
  int T;
  cin >> T;
  REP(t,T) {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    string res = solve_large(R, O, Y, G, B, V);
    cout << "Case #" << t + 1 << ": " << res << endl;
  }
  return 0;
}

