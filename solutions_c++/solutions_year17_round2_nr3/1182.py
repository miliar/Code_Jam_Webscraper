#include <bits/stdc++.h>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=1; t<=T; t++){
    cout << "Case #" << t << ": ";

    int N, Q;
    cin >> N >> Q;
    vector<double> E(N);
    vector<double> S(N);
    vector<vector<double>> D(N);
    for(int i=0; i<N; i++){
      cin >> E[i] >> S[i];
      //cout << E[i] << " " << S[i] << endl;
    }
    for(int i=0; i<N; i++){
      for(int j=0; j<N; j++){
        int x;
        cin >> x;
        D[i].push_back(x);
      }
    }
    int von, nach;
    cin >> von >> nach;
    vector<double> zeit(N);
    for(int i=1; i<N; i++){
      zeit[i] = numeric_limits<double>::max();
    }
    for(int i=0; i<N-1; i++){
      int cur = i+1;
      double d = D[i][i+1];
      while(E[i] >= d && cur < N){
        zeit[cur] = min(zeit[cur], zeit[i] + d/S[i]);
        //cout << zeit[cur] << "->" << d << " " << S[i] << endl;
        if(cur < N-1)
          d += D[cur][cur+1];
        cur++;
      }
    }
    
    cout << fixed << setprecision(7) << zeit[N-1] << endl;
  }

  return 0;
}
