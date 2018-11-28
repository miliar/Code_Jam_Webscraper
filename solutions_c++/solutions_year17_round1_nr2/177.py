#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
typedef pair<int, int> P;
#define INF (1<<28)
int cntu[108][108];
int cntd[108][108];
int need[108];
int n, p, x;
int t;



int solve(){
  cin >> n >> p;  
  for(int i = 0;i < n;i++){
    cin >> need[i];
  }
  for(int i = 0;i < n;i++){
    for(int j = 0;j < p;j++){
      cin >> x;
      int hoge = x /(1.1*need[i]);
      for(int k = max(1, hoge - 2);k <= hoge + 2;k++){
	double p = x * 1.0 / (k * need[i]);
	if(0.9 <= p && p <= 1.1){
	  cntd[i][j] = k;
	  break;
	}
	cntd[i][j] = 0;
      }
      
      hoge = x /(0.9*need[i]);
      for(int k = hoge + 2;k >= max( hoge - 2, 1);k--){
	double p = x * 1.0 / (k * need[i]);
	if(0.9 <= p && p <= 1.1){
	  cntu[i][j] = k;
	  break;
	}
	cntu[i][j] = 0;
      }
    }
  }

  int res = 0;
  vector<P> nums[108];
  vector<int> val;
  for(int i = 0;i < n;i++){
    for(int j = 0;j < p;j++){
      if(cntd[i][j] == 0)continue;
      nums[i].push_back(P(cntd[i][j], cntu[i][j]));
      val.push_back(cntd[i][j]);
    }
    sort(nums[i].begin(), nums[i].end());
  }
  sort(val.begin(), val.end());
  for(int k = 0;k < val.size();k++){
    int cntok = 0;
    int v = val[k];
    for(int i = 0;i < n;i++){
      for(int j = 0;j < nums[i].size();j++){
	if(nums[i][j].first <= v && v <= nums[i][j].second){
	  cntok++;
	  break;
	}
      }
    }
    if(cntok != n)continue;
    for(int i = 0;i < n;i++){
      for(int j = 0;j < nums[i].size();j++){
	if(nums[i][j].first <= v && v <= nums[i][j].second){
	  nums[i][j] = P(INF,INF);
	  break;
	}
      }
    }
    res++;
  }

  return res;
}

int main(){
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}
