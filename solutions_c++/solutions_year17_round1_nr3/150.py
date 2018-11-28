#include <iostream>
#include <queue>
using namespace std;

int64_t Hd, Ad, Hk, Ak, B, D;
int64_t gHd;
int map[101][101][101][101];
struct State{
  int64_t Hd, Ad, Hk, Ak;
  State attack() {
    State ret = (State) {Hd,Ad,Hk,Ak};
    ret.Hk -= ret.Ad;
    if(ret.Hk <= 0) {
      ret.Hk = 0;
    } else {
      ret.Hd -= ret.Ak;
      if(ret.Hd <= 0) ret.Hd = 0;
    }
    return ret;
  }
  State buff() {
    State ret = (State) {Hd,Ad,Hk,Ak};
    ret.Ad += B;
    if(ret.Ad >= ret.Hk) ret.Ad = ret.Hk; // 相手のHPを越える必要はない
    ret.Hd -= ret.Ak;
    if(ret.Hd <= 0) ret.Hd = 0;
    return ret;
  }

  State Cure() {
    State ret = (State) {Hd,Ad,Hk,Ak};
    ret.Hd = gHd;
    ret.Hd -= ret.Ak;
    if(ret.Hd <= 0) ret.Hd = 0;
    return ret;
  }

  State Debuff() {
    State ret = (State) {Hd,Ad,Hk,Ak};
    ret.Ak -= D;
    if(ret.Ak <= 0) ret.Ak = 0;
    ret.Hd -= ret.Ak;
    if(ret.Hd <= 0) ret.Hd = 0;
    return ret;
  }
  
};
int solve() {
  for(int i = 0; i <= Hd; i++) {
    for(int j = 0; j <= Hk; j++) {
      for(int k = 0; k <= Hk; k++) {
        for(int l = 0; l <= Ak; l++) {
          map[i][j][k][l] = 0;
        }
      }
    }
  }
  State state = (State){Hd,min(Hk, Ad),Hk,Ak};
  map[state.Hd][state.Ad][state.Hk][state.Ak] = 1;
  queue<State> que;
  que.push(state);
  while(!que.empty()) {
    State cs = que.front();que.pop();
    //cout << cs.Hd << "," << cs.Ad << "," << cs.Hk << "," << cs.Ak << endl;
    int turn = map[cs.Hd][cs.Ad][cs.Hk][cs.Ak];
    state = cs.attack();
    if(state.Hk == 0) {
      return turn;
    }
    
    if(state.Hd > 0 && !map[state.Hd][state.Ad][state.Hk][state.Ak]) {
      map[state.Hd][state.Ad][state.Hk][state.Ak] = turn + 1;
      que.push(state);
    }
    state = cs.buff();
    if(state.Hd > 0 && !map[state.Hd][state.Ad][state.Hk][state.Ak]) {
      map[state.Hd][state.Ad][state.Hk][state.Ak] = turn + 1;
      que.push(state);
    }
    state = cs.Cure();
    if(state.Hd > 0 && !map[state.Hd][state.Ad][state.Hk][state.Ak]) {
      map[state.Hd][state.Ad][state.Hk][state.Ak] = turn + 1;
      que.push(state);
    }
    state = cs.Debuff();
    if(state.Hd > 0 && !map[state.Hd][state.Ad][state.Hk][state.Ak]) {
      map[state.Hd][state.Ad][state.Hk][state.Ak] = turn + 1;
      que.push(state);
    }
  }
  return -1;
}
int main() {
  int T;
  cin >> T;
  for(int tz = 1; tz <= T; tz++) {
    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
    gHd = Hd;
    cout << "Case #" << tz << ": ";
    int ret = solve();
    if(ret == -1) {
      cout << "IMPOSSIBLE" << endl;
    }else{
      cout << ret << endl;
    }
  }
}