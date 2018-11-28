#include <bits/stdc++.h>

using namespace std;

int anzahl[3];

int main(){
  int T;
  cin >> T;
  int N, r, o, y, g, b, v;
  for(int t=1; t<=T; t++){
    cout << "Case #" << t << ": ";
    cin >> N >> r >> o >> y >> g >> b >> v;
    if(r*2 > N || y*2 > N || b*2 > N){
      cout << "IMPOSSIBLE";
    }
    else{
      int start = 0;
      if(y > r && y > b)
        start = 1;
      if(b > r && b > y)
        start = 2;
      int last = -1;
      int anzahl[3];
      anzahl[0] = r;
      anzahl[1] = y;
      anzahl[2] = b;
      char buchst[3];
      buchst[0] = 'R';
      buchst[1] = 'Y';
      buchst[2] = 'B';
      while(N > 0){
        int max = -1;
        int maxI = -1;
        for(int i=0; i<3; i++){
          if((anzahl[i] > max || (anzahl[i] == max && i == start))&& last != i){
            max = anzahl[i];
            maxI = i;
          }
        }
        cout << buchst[maxI];
        anzahl[maxI]--;
        N--;
        last = maxI;
      }
    }
    cout << endl;
  }

  return 0;
}
