#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>


using namespace std;

void fill_R(char G[25][25],int R,int C);
void fill_L(char G[25][25],int R,int C);
void fill_D(char G[25][25],int R,int C);
void fill_U(char G[25][25],int R,int C);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    int T,R,C;
    cin >> T;
    for(int tc=1;tc <= T;tc++){
      cout << "Case #" << tc << ": " << endl;
    char G[25][25];
      cin >>R; cin >> C;
      for (int i=0;i<R;i++)
        for(int j=0;j<C;j++)
          cin >> G[i][j];
      fill_R(G,R,C);
      fill_L(G,R,C);
      fill_D(G,R,C);
      fill_U(G,R,C);
      for (int i=0;i<R;i++){
        for(int j=0;j<C;j++)
          cout << G[i][j];
        cout <<endl;
      }
    }

    return 0;
}
void fill_R(char G[25][25],int R,int C){
  for (int i=0;i<R;i++)
    for (int j=0;j<C-1;j++){
      if (G[i][j]!='?' && G[i][j+1]=='?'){
        G[i][j+1] = G[i][j];
      }
    }
}
void fill_L(char G[25][25],int R,int C){
  for (int i=0;i<R;i++)
    for (int j=C-1;j>0;j--){
      if (G[i][j]!='?' && G[i][j-1]=='?'){
        G[i][j-1] = G[i][j];
      }
    }
}
void fill_D(char G[25][25],int R,int C){
  for (int j=0;j<C;j++)
    for (int i=0;i<R-1;i++){
      if (G[i][j]!='?' && G[i+1][j]=='?'){
        G[i+1][j] = G[i][j];
      }
    }
}
void fill_U(char G[25][25],int R,int C){
  for (int j=0;j<C;j++)
    for (int i=R-1;i>0;i--){
      if (G[i][j]!='?' && G[i-1][j]=='?'){
        G[i-1][j] = G[i][j];
      }
    }
}



