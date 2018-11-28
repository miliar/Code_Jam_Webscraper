#include<iostream>

using namespace std;

int main(){
   int T;
   cin >> T;
   for(int c = 1; c <= T; c++){
      cout << "Case #" << c << ": ";
      string S;
      cin >> S;
      int i,j;
      for(i = 0; i+1 < (int)S.size(); i++){
	 if(S[i+1] < S[i]){
	    break;
	 }
      }
      if(i == S.size()-1){
	 cout << S << endl;
	 continue;
      }
      for(j = i; j >= 0; j--){
	 if(S[j+1] < S[j])
	    S[j]--;
	 else
	    break;
      }
      for(int k = j+2; k < S.size(); k++){
	 S[k] = '9';
      }

      for(int k = 0; k < S.size(); k++){
	 if( k == 0 and S[k] == '0') continue;
	 cout << S[k];
      }
      cout << endl;
   }
   return 0;
}
