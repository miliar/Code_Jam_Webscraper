#include<iostream>
#include<vector>
#include <algorithm>
#include <string>
#include <bitset>
using namespace std;

void ocupy(vector<bool> &it, bool print = false){
  int l,r,smax,smin,s,min,max;
  bool flag = true;
  for(int i = 1 ; i < it.size() - 1; i++){
    if(it[i] == true)
      continue;
    for(int j = i; j >= 0; j --){
      if(it[j] == true){
        l = i - j;
        break;
      }
    }
    for(int j = i; j < it.size(); j ++){
      if(it[j] == true){
        r = j - i;
        break;
      }
    }
    // cout << "for "<<i << " l="<<l<<", r="<<r<<endl;
    smax = (l > r) ? l : r;
    smin = (l < r) ? l : r;
    if(flag){
      s = i;
      max = smax;
      min = smin;
      flag = false;
      // cout << "first s="<<s<<" min="<<min<<", max="<<max<<endl;
    }
    if(smin > min){
      s = i;
      min = smin;
      max = smax;
      // cout << "smin > min: s="<<s<<" min="<<min<<", max="<<max<<endl;
    }else if(smin == min && max < smax){

        s = i;
        min = smin;
        max = smax;
        // cout << "smin == min && max < smax: s="<<s<<" min="<<min<<", max="<<max<<endl;
    }
  }
  if(print){
  cout << max-1 << " " << min-1 <<endl;
  }
  // cout << "went in "<<s<<endl;
  it[s] = true;
}
void solve(int N, int K){
  int max = 0, min = 0;
  vector<bool> it(N + 2,false);
  it[0] = true; it[it.size() - 1] = true;

  for(int i = 0; i < K - 1  ; i++){
    // cout << "person " << i << " came in \n";
    ocupy(it);
    // cout << "person "<<i<<endl;
    // for(int k = 0; k < it.size(); k++){
    //   cout << it[k] <<" ";
    // }
    // cout << endl;
  }

  // cout << "last person came in \n";
  ocupy(it,true);
  // for(int k = 0; k < it.size(); k++){
  //   cout << it[k] <<" ";
  // }
  // cout << endl;


}
int main (){
    int T;
    int N,K;
    cin >> T;
    for(int i = 1; i <= T; i++){
      cin >> N;
      cin >> K;
      cout << "Case #"<<i<<": ";
      solve(N, K);
    }
}
