#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int solve(int dragon_health,int dragon_attack,int knight_health,int knight_attack,int dragon_buff,int knight_debuff);
const int IMPOSSIBLE=999999999;

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    int dragon_health,dragon_attack,knight_health,knight_attack,dragon_buff,knight_debuff;
    cin>>dragon_health>>dragon_attack>>knight_health>>knight_attack>>dragon_buff>>knight_debuff;
    int ret=solve(dragon_health,dragon_attack,knight_health,knight_attack,dragon_buff,knight_debuff);
    if(ret==IMPOSSIBLE)
      cout<<"Case #"<<i+1<<": IMPOSSIBLE\n";
    else
      cout<<"Case #"<<i+1<<": "<<ret<<'\n';
  }
}

int simulate(int dragon_health,int dragon_attack,int knight_health,int knight_attack,int dragon_buff,int knight_debuff,int buffs,int debuffs);

int solve(int dragon_health,int dragon_attack,int knight_health,int knight_attack,int dragon_buff,int knight_debuff){
  int best=IMPOSSIBLE;
  for(int b=0;;b++){
    if(b && dragon_buff==0) break;

    for(int d=0;;d++){
      if(d && knight_debuff==0) break;

      int t=simulate(dragon_health,dragon_attack,knight_health,knight_attack,dragon_buff,knight_debuff,b,d);
      //cout<<b<<','<<d<<": "<<t<<'\n';
      best=min(t,best);

      if(d*knight_debuff>=knight_attack) break;
    }

    if(dragon_buff*b+dragon_attack>=knight_health) break;
  }
  return best;
}

int simulate(int dragon_health,int dragon_attack,int knight_health,int knight_attack,int dragon_buff,int knight_debuff,int buffs,int debuffs){
  int dragon=dragon_health;
  int knight=knight_health;
  int cured=0;

  int t=0;

  while(true){
    t++;
    if(dragon_attack>=knight) return t;

    if(knight_attack>=dragon){
      if(cured>200) return IMPOSSIBLE;

      if(debuffs>0){
        int knight_potential_attack=max(knight_attack-knight_debuff,0);
        if(knight_potential_attack<dragon){
          debuffs--;
          knight_attack=max(knight_attack-knight_debuff,0);
          goto knight_turn;
        }
      }

      //cure
      dragon=dragon_health;

      cured++;
      goto knight_turn;
    }
    cured=0;

    if(debuffs>0){
      debuffs--;
      knight_attack=max(knight_attack-knight_debuff,0);
      goto knight_turn;
    }

    if(buffs>0){
      buffs--;
      dragon_attack+=dragon_buff;
      goto knight_turn;
    }

    //attack
    knight-=dragon_attack;

knight_turn:
    dragon-=knight_attack;
    if(dragon<=0) return IMPOSSIBLE;
  }
}
