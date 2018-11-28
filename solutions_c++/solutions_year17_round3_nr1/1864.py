#include<iostream>
#include<iomanip>
#include<vector>
#include<utility>
#include<algorithm>
#include<math.h> // PI is M_PI

using namespace std;

long double solve(vector<pair<long long,long long>> pc, int K){
  sort(pc.begin(),pc.end());
  reverse(pc.begin(),pc.end());
  long long bestCand = 0;
  long long sum = 0;
  long long maxArea = 0;
  int bestInd = 0;
  for(int i = 0; i < K; i++){
    sum += pc[i].first;
    if(pc[i].second > maxArea){ 
      maxArea = pc[i].second;
      bestInd = i;
    }
  }
  long long tmpMax = sum + maxArea;
  for(int i = K; i < pc.size(); i++){
    if(sum-pc[K-1].first+pc[i].first+pc[i].second > tmpMax){
      tmpMax = sum-pc[K-1].first+pc[i].first+pc[i].second;
    }
  }
  return M_PI*(long double)(tmpMax);
}

int main(){
  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    int N,K;
    cin >> N >> K;
    vector<pair<long long,long long>> pc(N);
    for(int j = 0; j < N; j++){
      long long R,H;
      cin >> R >> H;
      long long sideArea = 2*(long long)(R)*(long long)(H);
      long long area = (long long)(R)*(long long)(R);
      pc[j].first = sideArea;
      pc[j].second = area;
    }
    long double res = solve(pc,K);
    cout << fixed;
    cout << setprecision(9);
    cout << "Case #" << i+1 << ": " << res << endl;
  }
  return 0;
}
