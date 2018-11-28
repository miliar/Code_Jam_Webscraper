#include<iostream>
#include<iomanip>
#include<algorithm>
using namespace std;

const int MAX = 105;

void solve(){
   int N, Q;
   cin >> N >> Q;
   long long E[MAX], S[MAX], D[MAX][MAX];
   for(int i = 0; i < N; i++){
      cin >> E[i] >> S[i];
   }
   for(int i = 0; i < N; i++){
      for(int j = 0; j < N; j++){
	 cin >> D[i][j];
      }
   }
   for(int k = 0; k < N; k++){
      for(int i = 0; i < N; i++){
	 for(int j = 0; j < N; j++){
	    if(D[i][k] >= 0 and D[k][j] >= 0){
	       if(D[i][j] < 0)
		  D[i][j] = D[i][k] + D[k][j];
	       else
		  D[i][j] = min(D[i][k] + D[k][j], D[i][j]);
	    }
	 }
      }
   }
   long double D2[MAX][MAX];
   for(int i = 0; i < N; i++){
      for(int j = 0; j < N; j++){
	 if(D[i][j] > E[i]){
	    D2[i][j] = -1;
	 }
	 else{
	    D2[i][j] = (long double)D[i][j] / (long double)S[i];
	 }
      }
   }

   for(int k = 0; k < N; k++){
      for(int i = 0; i < N; i++){
	 for(int j = 0; j < N; j++){
	    if(D2[i][k] >= 0 and D2[k][j] >= 0){
	       if(D2[i][j] < 0)
		  D2[i][j] = D2[i][k] + D2[k][j];
	       else
		  D2[i][j] = min(D2[i][k] + D2[k][j], D2[i][j]);
	    }
	 }
      }
   }

   for(int i = 0; i < Q; i++){
      int U,V; cin >> U >> V;
      U--; V--;
      if(i)
	 cout << " ";
      cout << fixed << setprecision(9) << D2[U][V];
   }
}

int main(){
   int T;
   cin >> T;
   for(int c = 1; c <= T; c++){
      cout << "Case #" << c << ": ";
      solve();
      cout << endl;
   }
   return 0;
}
