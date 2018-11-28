#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define XX 200
int Hd, Ad, Hk, Ak, B, D;
int current_Hd, current_Ad, current_Hk, current_Ak;
void init() {
    current_Hd = Hd;
    current_Ad = Ad;
    current_Hk = Hk;
    current_Ak = Ak;
}

void buff() {
  current_Ad += B;
}

void cure() {
  current_Hd = Hd;
}

void debuff() {
  current_Ak -= D;
  current_Ak = max(0, current_Ak);
}

void attack() {
  current_Hk -= current_Ad;
  current_Hk = max(0, current_Hk);
}

void enemy_attack() {
  current_Hd -= current_Ak;
  current_Hd = max(0, current_Hd);
}

bool meDead() {
  if(current_Hd <= 0) {
    return true;
  }
  return false;
}

bool enemyDead() {
  if(current_Hk <= 0) {
    return true;
  }
  return false;
}

bool need_cure() {
  if(current_Hd - current_Ak <= 0) {
    return true;
  }
  return false;
}

bool need_cure_after_debuff() {
  if(current_Hd - (current_Ak - D) <= 0)
    return true;
  return false;
}

int f(int debuff_times, int buff_times) {
  init();

  int turn_cnt = 0;
  int cure_times = 0;

  for(int i = 0; i < debuff_times; i++) {
    turn_cnt++;
    if(need_cure_after_debuff()) {
      cure_times++;
      if(cure_times > XX) {
        return -1;
      }
      cure();
      i--;
    }else{
      debuff();
    }
    enemy_attack();
    if(meDead()) {
      return -1;
    }
  }


  cure_times = 0;
  for(int i = 0; i < buff_times; i++) {
    turn_cnt++;



    if(need_cure()) {
      cure_times++;
      if(cure_times > XX) {
        return -1;
      }
      cure();
      i--;
    }else {
      buff();
    }
    enemy_attack();
    if(meDead()) {
      return -1;
    }
  }

  for(int i = 0; i < XX * 2; i++) {
    turn_cnt++;

    if(current_Hk <= current_Ad) {
      return turn_cnt;
    }

    if(need_cure()) {
      cure();
    }else{
      attack();
      if(enemyDead()) {
        return turn_cnt;
      }
    }
    enemy_attack();

    if(meDead()) {
      return -1;
    }

  }
  return -1;
}

int main() {
  int T;
  cin >> T;

  for(int t = 0; t < T; t++) {

    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

    int ans =1000000;
    for(int debuff_times = 0; debuff_times < XX; debuff_times++) {
      for(int buff_times = 0; buff_times < XX; buff_times++) {
        // cout << debuff_times << ' ' << buff_times << endl;
        // cout << f(debuff_times, buff_times) << endl;
        int result = f(debuff_times, buff_times);
        if(result > 0) {
          ans = min(ans, f(debuff_times, buff_times));
        }

      }
    }


    cout << "Case #" << t + 1 << ": ";
    if(ans == 1000000) {
      cout << "IMPOSSIBLE" << endl;
    }else
    cout << ans << endl;
  }

}
