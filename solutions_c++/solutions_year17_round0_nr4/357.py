#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

typedef set<int> si;
typedef vector<pair<int, int> > vpii;
typedef set<pair<int, int> > spii;
typedef map<int, map<int, char> > mimic;

long N;

si Bas, Bbs;
mimic board;
int score;

int getThreatCount(int a, int b) {
  int vCount = 0;
  for (auto v : Bbs) {
    if ((a + v) % 2) continue;
    int i = (a + v) / 2;
    int j = (v - a) / 2;
    if (i < 0 || j < 0 || i >= N || j >= N) continue;
    vCount += 1;
  }
  int uCount = 0;
  for (auto u : Bas) {
    if ((u + b) % 2) continue;
    int i = (u + b) / 2;
    int j = (b - u) / 2;
    if (i < 0 || j < 0 || i >= N || j >= N) continue;
    uCount += 1;
  }
  // lonely
  if (uCount == 1 || vCount == 1) return -1000;
  return uCount + vCount;
}

void addBishop(int i, int j) {
  int a = i - j;
  int b = i + j;
  Bas.erase(i - j);
  Bbs.erase(i + j);
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {

    long M;
    cin >> N >> M;

    si Ris, Rjs;
    for (int i = 0; i < N; i++) {
      Ris.insert(i);
    }
    for (int j = 0; j < N; j++) {
      Rjs.insert(j);
    }

    score = 0;
    Bas.clear();
    Bbs.clear();
    for (int i = -N + 1; i < N; i++) {
      Bas.insert(i);
    }
    for (int j = 0; j < 2 * N - 1; j++) {
      Bbs.insert(j);
    }

    board.clear();
    for (int m = 0; m < M; m++) {
      string c;
      int i, j;
      cin >> c >> i >> j;
      i -= 1;
      j -= 1;

      if (c == "x" || c == "o") {
        Ris.erase(i);
        Rjs.erase(j);
        board[i][j] = c == "o" ? 'q' : 'r';
        score += 1;
      }
      if (c == "+" || c == "o") {
        addBishop(i, j);
        board[i][j] = c == "o" ? 'q' : 'b';
        score += 1;
      }
    }

    spii Rlog;
    vpii Qlog;
    while (Ris.size()) {
      int i = *Ris.begin();
      int j = *Rjs.begin();
      Ris.erase(i);
      Rjs.erase(j);
      auto p = make_pair(i, j);
      score += 1;
      if (board[i][j] == 'b') {
        Qlog.push_back(p);
        board[i][j] = 'q';
      } else {
        Rlog.insert(p);
        board[i][j] = 'r';
      }
    }

    vpii Blog;
    while (Bas.size()) {
      pair<int, int> minP;
      int minThreat = 0x7fffffff;
      for (auto a : Bas) {
        for (auto b : Bbs) {
          if ((a + b) % 2) continue;
          int i = (a + b) / 2;
          int j = (b - a) / 2;
          if (i < 0 || j < 0 || i >= N || j >= N) continue;
          int threat = getThreatCount(a, b);
          if (threat < minThreat) {
            minThreat = threat;
            minP = make_pair(a, b);
          }
        }
      }
      if (minThreat == 0x7fffffff) break;

      {
        int a = minP.first;
        int b = minP.second;
        int i = (a + b) / 2;
        int j = (b - a) / 2;
        Bas.erase(a);
        Bbs.erase(b);
        //cout << "attempt to insert bishop " << i << " " << j <<  " " << a << " " << b << endl;
        auto p = make_pair(i, j);
        if (board[i][j] == 'r') {
          Qlog.push_back(p);
          Rlog.erase(p);
          board[i][j] = 'q';
        } else {
          Blog.push_back(p);
          board[i][j] = 'b';
        }
        score += 1;
      }
    }

    int z = Rlog.size() + Qlog.size() + Blog.size();
    cout << "Case #" << (t + 1) << ": " << score << " " << z << endl;
    for (auto it = Rlog.begin(); it != Rlog.end(); it++) {
      cout << "x " << (it->first + 1) << " " << (it->second + 1) << endl;
    }
    for (auto it = Qlog.begin(); it != Qlog.end(); it++) {
      cout << "o " << (it->first + 1) << " " << (it->second + 1) << endl;
    }
    for (auto it = Blog.begin(); it != Blog.end(); it++) {
      cout << "+ " << (it->first + 1) << " " << (it->second + 1) << endl;
    }
  }

  return 0;
}
