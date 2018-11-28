#include<iostream>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int C = 1; C <= T; C++){
    long long int N, K;
    cin >> N >> K;

    /*if(K > (N / 2)){
      cout << "Case #" << C << ": 0 0" << endl;
      continue;
      }*/
    
    while(K != 1){
      if(K % 2 == 0){
	N /= 2;
	K /= 2;
      }
      else{
	N = N / 2 - ((N % 2) == 0 ? 1 : 0);
	K /= 2;
      }
    }

    cout << "Case #" << C << ": " << N/2 << " " << N - N/2 - 1 << endl;
  }

  return 0;
}
	
