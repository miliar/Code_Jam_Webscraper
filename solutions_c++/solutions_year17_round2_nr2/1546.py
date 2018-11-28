#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    int N;
    vector<int> cols(6);
    vector<char> letters = {'R','O','Y','G','B','V'};
    cin >> N;
    int maxCol = 0;
    int maxVal = 0;
    for(int j = 0; j < 6; j++){
      cin >> cols[j];
      if(cols[j] > cols[maxCol]){
        maxCol = j;
        maxVal = cols[j];
      }
    }
    int startCol = maxCol;
    string sol = "";
    for(int j = 0; j < N; j++){
      if((cols[0]>cols[2]+cols[4] | cols[2]>cols[0]+cols[4] | cols[4]>cols[2]+cols[0]) & j == 0){
        sol = "IMPOSSIBLE";
        break;
      }
      sol += letters[maxCol];
      cols[maxCol]--;
      int tmpCol = maxCol;
      maxVal = 0;
      for(int k = 0; k < 6; k++){
        if(k == tmpCol) continue;
        if(cols[k] > maxVal){
          maxCol = k;
          maxVal = cols[k];
        }
      }
      if(startCol != tmpCol){
        if(cols[startCol] == cols[maxCol]) maxCol = startCol;
      }
    }
    cout << "Case #" << i+1 << ":" << " " << sol << endl;
  }
  return 0;
}
