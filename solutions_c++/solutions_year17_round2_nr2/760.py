#include <bits/stdc++.h>

using namespace std;

void solve()
{
  int N, R, O, Y, G, B, V;
  cin >> N;
  cin >> R >> O >> Y >> G >> B >> V;

  if (R+Y+G+V == 0) {
    // just O and B
    if (O == B) {
      for (int i = 0; i < O; i++) {
	cout << "OB";
      }
    } else {
      cout << "IMPOSSIBLE";
    }
    return;
  }

  if (O+Y+B+V == 0) {
    // just R and G
    if (R == G) {
      for (int i = 0; i < R; i++) {
	cout << "RG";
      }
    } else {
      cout << "IMPOSSIBLE";
    }
    return;
  }
  
  if (R+O+G+B == 0) {
    // just Y and V
    if (Y == V) {
      for (int i = 0; i < Y; i++) {
	cout << "YV";
      }
    } else {
      cout << "IMPOSSIBLE";
    }
    return;
  }

  string Bsub, Rsub, Ysub;
  
  if (O > 0) {
    if (O+1 > B) {
      cout << "IMPOSSIBLE";
      return;
    }
    B -= O;
    Bsub = "B";
    for (int i = 0; i < O; i++) {
      Bsub += "OB";
    }
  }
  if (G > 0) {
    if (G+1 > R) {
      cout << "IMPOSSIBLE";
      return;
    }
    R -= G;
    Rsub = "R";
    for (int i = 0; i < G; i++) {
      Rsub += "GR";
    }
  }
  if (V > 0) {
    if (V+1 > Y) {
      cout << "IMPOSSIBLE";
      return;
    }
    Y -= V;
    Ysub = "Y";
    for (int i = 0; i < V; i++) {
      Ysub += "VY";
    }
  }

  pair<int, char> A[3];
  A[0] = make_pair(R, 'R');
  A[1] = make_pair(Y, 'Y');
  A[2] = make_pair(B, 'B');
  sort(A, A+3);

  if (A[2].first > A[0].first + A[1].first) {
    cout << "IMPOSSIBLE";
    return;
  }
  
  string s;
  while (A[2].first < A[0].first + A[1].first) {
    for (int i = 2; i >= 0; i--) {
      s += A[i].second;
      A[i].first--;
    }
  }
  while (A[2].first > 0) {
    s += A[2].second;
    A[2].first--;

    if (A[0].first > 0) {
      s += A[0].second;
      A[0].first--;
    } else {
      s += A[1].second;
      A[1].first--;
    }
  }

  if (Bsub != "") {
    auto index = s.find('B');
    s.replace(index, 1, Bsub);
  }
  if (Rsub != "") {
    auto index = s.find('R');
    s.replace(index, 1, Rsub);
  }
  if (Ysub != "") {
    auto index = s.find('Y');
    s.replace(index, 1, Ysub);
  }
  
  cout << s;
    

}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }    
  return 0;
}
