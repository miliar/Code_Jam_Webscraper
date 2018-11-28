#include<iostream>
#include<algorithm>

using namespace std;

char str[108][108];
int r, c;
int t;

void solve(){
  cin >> r >> c;

  for(int i = 0;i < r;i++){
    for(int j = 0;j < c;j++){
      cin >> str[i][j];
    }
  }
  for(int i = 0;i < r;i++){
    for(int j = 0;j < c;j++){
      if(str[i][j] == '?')continue;
      for(int k = 1;k < c;k++){
	if(j+k<c && str[i][j+k] == '?')str[i][j+k] = str[i][j];
	else break;
      }
      for(int k = 1;k < c;k++){
	if(j-k>=0 && str[i][j-k] == '?')str[i][j-k] = str[i][j];
	else break;
      }
    }
  }

  for(int i = 0;i < r;i++){
    for(int j = 0;j < c;j++){
      if(str[i][j] == '?')continue;
      for(int k = 1;k < r;k++){
	if(i + k < r && str[i+k][j] == '?')str[i+k][j] = str[i][j];
	else break;
      }
      for(int k = 1;k < r;k++){
	if(i - k >= 0 && str[i-k][j] == '?')str[i-k][j] = str[i][j];
      }
    }
  }
  for(int i = 0;i < r;i++){
    for(int j= 0;j < c;j++){
      cout << str[i][j];
    }cout << endl;
  }
}

int main(){
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ":" << endl;
    solve();
  }
  return 0;
}
