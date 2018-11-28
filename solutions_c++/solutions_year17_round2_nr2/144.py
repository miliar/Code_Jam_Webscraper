#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

class Data {
 public:
  char c;
  int num;
  bool operator<(const Data& another) const { return num < another.num; }
};

string get_result(int R, int Y, int B) {
  Data data[3];
  data[0].c = 'R';
  data[0].num = R;
  data[1].c = 'Y';
  data[1].num = Y;
  data[2].c = 'B';
  data[2].num = B;
  sort(data, data + 3);
  int overlap = data[0].num + data[1].num - data[2].num;
  if (overlap < 0) return "IMPOSSIBLE";
  string res = "";
  for (int i = 0; i < data[2].num; i++) {
    res += data[2].c;
    if (data[0].num) {
      res += data[0].c;
      data[0].num--;
    } else {
      res += data[1].c;
      data[1].num--;
    }
    if (overlap) {
      overlap--;
      res += data[1].c;
      data[1].num--;
    }
  }
  return res;
}

string get_circle(char A, char B, int counts) {
  string res = "";
  for (int i = 0; i < counts; i++) {
    res += A;
    res += B;
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    cout << "Case #" << cas << ": ";
    if (R == G && O == 0 && Y == 0 && B == 0 && V == 0) {
      cout << get_circle('R', 'G', R) << endl;
      continue;
    }
    if (B == O && R == 0 && Y == 0 && G == 0 && V == 0) {
      cout << get_circle('B', 'O', B) << endl;
      continue;
    }
    if (Y == V && O == 0 && R == 0 && B == 0 && G == 0) {
      cout << get_circle('Y', 'V', Y) << endl;
      continue;
    }
    if ((G && R < G + 1) || (O && B < O + 1) || (V && Y < V + 1)) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    string tmp = get_result(R - G, Y - V, B - O);
    if (tmp == "IMPOSSIBLE") {
      cout << tmp << endl;
      continue;
    }
    string res = "";
    bool r = true, y = true, b = true;
    for (auto c : tmp) {
      res += c;
      switch (c) {
        case 'R':
          if (r) {
            res += get_circle('G', 'R', G);
            r = false;
          }
          break;
        case 'Y':
          if (y) {
            res += get_circle('V', 'Y', V);
            y = false;
          }
          break;
        case 'B':
          if (b) {
            res += get_circle('O', 'B', O);
            b = false;
          }
          break;
      }
    }
    cout << res << endl;
  }
}
