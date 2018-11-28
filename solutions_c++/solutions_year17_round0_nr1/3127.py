#include<iostream>

using namespace std;

int main(){
   int T;
   cin >> T;
   for(int c = 1; c <= T; c++){
      cout << "Case #" << c << ": ";
      string S;
      cin >> S;
      int k;
      cin >> k;
      int count = 0;
      for(int i = 0; i+k <= (int)S.size(); i++){
	 if(S[i] == '+') continue;
	 count++;
	 for(int j = i; j < i+k; j++){
	    S[j] = (S[j] == '-' ? '+' : '-');
	 }
	 //cout << endl << S << endl;
      }
      bool B = true;
      for(int i = 0; i < S.size(); i++){
	 if(S[i] == '-'){
	    B = false;
	    cout << "IMPOSSIBLE";
	    break;
	 }
      }
      if(B)
	 cout << count;
      cout << endl;
   }
   return 0;
}
