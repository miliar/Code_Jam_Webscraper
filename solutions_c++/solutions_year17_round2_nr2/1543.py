#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");

#define cin fin
#define cout fout


int t , n , color[6];
string res = "";

bool check(){
  for(int i = 0 ; i < res.size() ; i++){
    int next = (i+1) % res.size();
    if(res[i] == res[next] ||
       (res[i] == 'R' && (res[next] == 'O' || res[next] == 'V')) ||
       (res[i] == 'O' && (res[next] == 'R' || res[next] == 'Y')) ||
       (res[i] == 'Y' && (res[next] == 'O' || res[next] == 'G')) ||
       (res[i] == 'G' && (res[next] == 'Y' || res[next] == 'B')) ||
       (res[i] == 'B' && (res[next] == 'G' || res[next] == 'V')) ||
       (res[i] == 'V' && (res[next] == 'B' || res[next] == 'R')))
      return false;
  }
  return true;
}

void input(int x){
  cin >> n;
  res = "";
  for(int i = 0 ; i < 6 ; i++)
    cin >> color[i];
  if(color[0] > color[2] + color[4] || color[2] > color[0] + color[4]
     || color[4] > color[0] + color[2]){
    cout << "Case #" << x << ": " << "IMPOSSIBLE" << endl;
    return;
  }
  while(color[0] > 0){
    res += "R";
    color[0]--;
  }
  for(int j = 0 ; j < res.size() && color[2] > 0 ; j++){
    int before = (j == 0) ? res.size() - 1 : j-1;
    if(res[before] == res[j]){
      res.insert(j , "Y");
      color[2]--;
    }
  }
  for(int j = 0 ; j < res.size() && color[2] > 0 ; j++){
    int before = (j == 0) ? res.size() - 1 : j-1;
    if(res[before] != 'Y' && res[j] != 'Y'){
      res.insert(j , "Y");
      color[2]--;
    }
  }
  while(color[2] > 0){
    res += "Y";
    color[2]--;
  }
  for(int j = 0 ; j < res.size() && color[4] > 0 ; j++){
    int before = (j == 0) ? res.size() - 1 : j-1;
    if(res[before] == res[j]){
	res.insert(j , "B");
	color[4]--;
    }
  }
  for(int j = 0 ; j < res.size() && color[4] > 0 ; j++){
    int before = (j == 0) ? res.size() - 1 : j-1;
    if(res[before] != 'B' && res[j] != 'B'){
      res.insert(j , "B");
      color[4]--;
    }
  }
  while(color[4] > 0){
    res += "B";
    color[4]--;
  }
  cout << "Case #" << x << ": " << (check() ? res : "IMPOSSIBLE") << endl;
}

int main(){
  cin >> t;
  for(int i = 0 ; i < t ; i++)
    input(i+1);
  return 0;
}
