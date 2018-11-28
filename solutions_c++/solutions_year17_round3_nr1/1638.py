#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>
#include <set>

using namespace std;

string inpFileName="A-large.in";
string outFileName="A-large.out";
const double PI  =3.141592653589793238463;

double cake_area(int R, int H){
  return PI*R*R + 2*PI*R*H;
}

double circle_area(int R){
  return PI*R*R;
}


int main(int argc, char **argv){

  if (argc > 1){
    inpFileName = std::string(argv[1]);    outFileName = std::string(argv[2]);
  }
  cerr <<"In:  "<< inpFileName << "\t Out : " << outFileName << "\n";
  
  int T;
  freopen(inpFileName.c_str(), "r", stdin);
  freopen(outFileName.c_str(), "w", stdout);
  
  scanf("%d", &T);
  for (int iT=1; iT<=T; iT++){

    int K, N;    
    vector<double> time;
    cin >> N >> K;
    vector<int> R, H;
    for (int i=0; i<N; i++){
      int ri, hi;
      cin >> ri >> hi;
      R.push_back(ri); H.push_back(hi);
    }

    //sort
    for (int i=0; i<N-1; i++){
      for (int j=i+1; j<N; j++){
	if (R[i]<R[j]){
	  int t = R[i]; R[i] = R[j]; R[j] = t;
	  t = H[i]; H[i] = H[j]; H[j] = t;
	}	
      }
    }

    //Dynamic programming
    double best[K][N];
    for (int i=0; i<N; i++)
      best[0][i] = cake_area(R[i], H[i]);
    

    for (int i=1; i<K; i++){
      //Init to 0;
      for (int j=0; j<N; j++){
	best[i][j]=0;	
      }

      //Start searching
      for (int j=i; j<N; j++){	
	for (int k=j-1; k>=0; k--){
	  double a = best[i-1][k] + cake_area(R[j], H[j]) - circle_area(R[j]);
	  if ( a > best[i][j]){
	    best[i][j] = a;
	  }	  
	}	  
      }            
    }

    double rst = best[K-1][0];
    for (int i=1;i<N; i++){
      if (best[K-1][i]>rst){
	rst = best[K-1][i];
      }
    }
          
    printf("Case #%d: %.6f\n", iT, rst);
    
  }
  
  
  return 0;
}
