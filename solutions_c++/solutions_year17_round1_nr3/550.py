#include <iostream>
#include <fstream>
#include <set>
#include <queue>

using namespace std;

int B,D,HD;

class state {
public:
  int hd,ad,hk,ak;
  int d;
  state(int a,int b,int c,int d,int depth) {
    hd = a; ad=b; hk=c; ak=d;
    this->d = depth;
  }
  bool isGoal() {
    if (hk <= 0) return true;
    else return false;
  }
  bool isDead() {
    if (hd <= 0) return true;
    else return false;
  }
  string encode() {
    return to_string(hd)+"."+to_string(ad)+"."+to_string(hk)+"."+to_string(ak);
  }
};

string encode(int hd,int ad,int hk,int ak) {
  return to_string(hd)+"."+to_string(ad)+"."+to_string(hk)+"."+to_string(ak);
}

bool isDead(int hd,int ad,int hk,int ak) {
  if (hd <= 0) return true;
  else return false;
}

int solve(int Hd,int Ad,int Hk, int Ak, int BB, int DD) {
  state *init = new state(Hd,Ad,Hk,Ak,0);
  HD = Hd;
  B = BB;
  D = DD;
  queue<state*> Q;
  set<string> S;
  S.insert(init->encode());
  Q.push(init);
  state *ns;
  string str;
  int res=-1;
  while (!Q.empty()) {
    state *s = Q.front();
    Q.pop();
    if (s->isGoal()) {
      res = s->d;
      goto exit;
    }
    if (s->isDead()) continue;
    // attack
    if (s->hk - s->ad <= 0) {
      res = s->d + 1;
      goto exit;
    }

    if (s->hd - s->ak > 0) {
      str = encode(s->hd - s->ak, s->ad, s->hk - s->ad, s->ak);
      if (S.find(str) == S.end()) {
        Q.push(new state(s->hd - s->ak, s->ad, s->hk - s->ad, s->ak, s->d + 1));
        S.insert(str);
      }
    }
    // buff
    if (B > 0 && s->hd - s->ak > 0) {
      str = encode(s->hd - s->ak, s->ad+B, s->hk, s->ak);
      if (S.find(str) == S.end()) {
        Q.push(new state(s->hd - s->ak, s->ad+B, s->hk, s->ak, s->d+1));
        S.insert(str);
      }
    }
    // cure
    if (s->ak < HD && HD - s->ak > 0) {
      str = encode(HD - s->ak, s->ad, s->hk, s->ak);
      if (S.find(str) == S.end()) {
        Q.push(new state(HD - s->ak, s->ad, s->hk, s->ak, s->d+1));
        S.insert(str);
      }
    }
    // debuff
    if (s->ak > 0 && D > 0 && s->hd - max(s->ak-D,0) > 0) {
      str = encode(s->hd - (s->ak-D), s->ad, s->hk, max(s->ak-D,0));
      if (S.find(str) == S.end()) {
        Q.push(new state(s->hd - (s->ak-D), s->ad, s->hk, max(s->ak-D,0), s->d+1));
        S.insert(str);
      }
    }
    delete s;
  }
exit:
  while (!Q.empty()) {
    state *s = Q.front();
    Q.pop();
    delete s;
  }
  return  res;
}

int main(){
  int i,t,hd,ad,hk,ak,b1,d1;
  ifstream infile;
  ofstream outfile;
  infile.open("knight.in");
  outfile.open("knight.txt");
  infile >> t;
  for (i=0;i<t;i++){
    infile >> hd >> ad >> hk >> ak >> b1 >> d1;
//cout << hd << " " << ad << " " << hk << " " << ak << " " << b1 << " " << d1 << endl;
    int r=solve(hd,ad,hk,ak,b1,d1);
//cout << r << endl;
    if (r==-1) outfile << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
    else outfile << "Case #" << i+1 << ": " << r << endl; 
  }
  return 0;
}

