#include<iostream>
#include<string>
using namespace std;

bool change[1001];

int main(){
  int T;
  cin >> T;
  for(int C = 1; C <= T; C++) {
    string S;
    int K;
    cin >> S >> K;

    int ans = 0, len = S.length();
    bool valid = true;
    for(int i = 0; i <= len; i++)
      change[i] = false;
    for(int i = 0; i < len - K + 1; i++){
      if(change[i] == false){
	if(S[i] == '+')
	  continue;
	else{
	  ans++;
	  for(int j = 0; j < K; j++)
	    change[j + i] = !(change[j + i]);
	}
      }
      else{
	if(S[i] == '+'){
	  ans++;
	  for(int j = 0; j < K; j++)
	    change[j + i] = !(change[j + i]);
	}
	else
	  continue;
      }
    }

    for(int i = len - K + 1; i < len; i++)
      if(change[i] == true){
	if(S[i] == '-')
	  continue;
	else{
	  valid = false;
	  break;
	}
      }
      else{
	if(S[i] == '+')
	  continue;
	else{
	  valid = false;
	  break;
	}
      }
    if(valid == true)
      cout << "Case #" << C << ": " << ans << endl;
    else
      cout << "Case #" << C << ": IMPOSSIBLE" << endl;
  }
  return 0;
}
