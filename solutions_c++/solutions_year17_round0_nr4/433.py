#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 3030;
const ll  MODD = 1000000007;

char A[MAX_N][MAX_N];

void do_case(){
  int n,m; cin >> n >> m;
  for(int i=0;i<=n;i++)
    for(int j=0;j<=n;j++)
      A[i][j] = '.';

  set<pair<int,int> > S;
  int found_o = -1;
  for(int i=0;i<m;i++){
    int I,J; char c;
    cin >> c >> I >> J;
    A[I][J] = c;
    if(c != '+'){
      found_o = J;
      if(c == 'x')
        S.emplace(I,J);
      A[I][J] = 'o';
    }
  }

  if(found_o == -1) { A[1][1] = 'o'; S.emplace(1,1); found_o = 1; }

  if(n > 1){
    for(int j=1;j<=n;j++)
      if(A[1][j] == '.'){
        A[1][j] = '+';
        S.emplace(1,j);
      }


    int col = (found_o != 1 ? 1 : n);
    A[n][col] = 'x';
    S.emplace(n,col);

    for(int j=2,off=-1;j<n;j++){
      for(int cc=0;cc<3;cc++){
        if(j+off == found_o) off++;
        if(j+off == col) off++;
      }
      A[j][j+off] = 'x';
      S.emplace(j,j+off);
    }
    for(int j=2;j<n;j++){
      A[n][j] = '+';
      S.emplace(n,j);
    }
  }
  cout << (n == 1 ? 2 : 3*n-2) << " " << S.size() << endl;
  for(auto x : S)
    cout << A[x.first][x.second] << " " << x.first << " " << x.second << endl;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(9);
  
  int T,C=1; cin >> T;
  
  while(T--) {
    cout << "Case #" << C++ << ": ";
    //cout << do_case() << endl;
    do_case();
  }
  
  return 0;
}
