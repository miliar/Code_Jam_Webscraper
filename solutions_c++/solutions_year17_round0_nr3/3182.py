#include<iostream>
#include<algorithm>
#include<map>
using namespace std;


int main(){
   int T;
   cin >> T;
   for(int c = 1; c <= T; c++){
      cout << "Case #" << c << ": ";
      long long N,K, cur = 0;
      cin >> N >> K;
      map<long long, long long> M;
      M[N] = 1;
      bool B = true;
      while(B){
	 auto it = M.rbegin();
	 long long I= it->first, C = it->second;
	 //cerr << endl << "I,C " << I << " " << C << endl;
	 M.erase(I);
	 long long LS = (I-1)/2,RS = I - LS - 1;
	 //cerr << "LS, RS " <<  LS << " " << RS << endl;
	 if(C + cur >= K){
	    cout << max(LS,RS) << " " << min(LS,RS) << endl;
	    B = false;
	 }
	 if(B){
	    M[LS] += C;
	    M[RS] += C;
	    cur += C;
	 }
      }
   }
   return 0;
}
