#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define rep(i, from, to) for(int i = from; i < to; i++)

int main(){
  int T, R, O, Y, B, G, V, N; cin >> T;
  rep(t, 1, T+1){
    cout << "Case #" << t << ": ";
    cin >> N >> R >> O >> Y >> G >> B >> V;
    string line;

    if (O > B) { cout << "IMPOSSIBLE" << endl; continue; }
    if (V > Y) { cout << "IMPOSSIBLE" << endl; continue; }
    if (G > R) { cout << "IMPOSSIBLE" << endl; continue; }
    if (O == B && O > 0 && O+B != N) { cout << "IMPOSSIBLE" << endl; continue; }
    if (V == Y && V > 0 && V+Y != N) { cout << "IMPOSSIBLE" << endl; continue; }
    if (G == R && G > 0 && G+R != N) { cout << "IMPOSSIBLE" << endl; continue; }

    if (O == B && O > 0){
      rep(i, 0, O) { line += 'B'; line += 'O'; }
      cout << line << endl;
      continue;
    }
    if (V == Y && V > 0){
      rep(i, 0, V) { line += 'V'; line+= 'Y'; }
      cout << line << endl;
      continue;
    }
    if (G == R && G > 0){
      rep(i, 0, G) { line += 'G'; line += 'R'; }
      cout << line << endl;
      continue;
    }

    B -= O; R -= G; Y -= V;

    if (B > R+Y) { cout << "IMPOSSIBLE" << endl; continue; }
    if (R > B+Y) { cout << "IMPOSSIBLE" << endl; continue; }
    if (Y > B+R) { cout << "IMPOSSIBLE" << endl; continue; }


    if (B != 0 && R != 0 && Y != 0){
      if (Y >= B && Y >= R){
        line += 'R'; R--;
        while (G > 0) { line += 'G'; line += 'R'; G--; }
      }
    }

    int last = 3;
    while (R+B+Y > 0){
      if (R >= B && R >= Y){
        if (last != 0){
          line += 'R';
          while (G > 0) { line += 'G'; line += 'R'; G--; }
          last = 0; R--;
        } else if (B > Y){
          line += 'B';
          while (O > 0) { line += 'O'; line += 'B'; O--; }
          last = 1; B--;
        } else {
          line += 'Y';
          while (V > 0) { line += 'V'; line += 'Y'; V--; }
          last = 2; Y--;
        }
      } else if (B >= Y && B >= R){
        if (last != 1){
          line += 'B';
          while (O > 0) { line += 'O'; line += 'B'; O--; }
          last = 1; B--;
        } else if (Y >= R){
          line += 'Y';
          while (V > 0) { line += 'V'; line += 'Y'; V--; }
          last = 2; Y--;
        } else {
          line += 'R';
          while (G > 0) { line += 'G'; line += 'R'; G--; }
          last = 0; R--;
        }
      } else {
        if (last != 2){
          line += 'Y';
          while (V > 0) { line += 'V'; line += 'Y'; V--; }
          last = 2; Y--;
        } else if (B >= R){
          line += 'B';
          while (O > 0) { line += 'O'; line += 'B'; O--; }
          last = 1; B--;
        } else {
          line += 'R';
          while (G > 0) { line += 'G'; line += 'R'; G--; }
          last = 0; R--;
        }
      }
    }
    cout << line << endl;
  }

}
