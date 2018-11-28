#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <fstream>
#include <string>
#include <vector>
#include <limits>
#include <set>

using namespace std;

string inpFileName="A-small.in";
string outFileName="A-small.out";


char G[50][50];
char F[50][50];

int solve(int R, int C){
  cerr << "\n\n\n";
  for (int i=0; i<R; i++){
    for (int j=0; j<C; j++){
      F[i][j] = G[i][j];
      //cerr << F[i][j];
    }
    //    cerr << "\n";
  }

  
  for (int i=0; i<R; i++){
    for (int j=0; j<C; j++){
      if (G[i][j]!='?'){
	F[i][j] = G[i][j];
	int k=j-1;
	while (G[i][k]=='?' && k>=0){
	  F[i][k] = F[i][j]; k--;
	}
	k = j+1;
	while (G[i][k]=='?' && k<C){
	  F[i][k] = F[i][j]; k++;
	}	  
      }
    }
  }


  for (int i=0; i<R; i++){
    for (int j=0; j<C; j++){
      if (F[i][j]=='?'){
	if ((j>0 && F[i][j-1]=='?') || (j==0 && F[i][j+1] == '?') || (C==1)){
	  int t=0;
	  if (i==0) for (t=i+1; t<R; t++) if (F[t][j]!='?') break;
	  if (i>0) t=i-1;
	  
	  for (int k=0; k<C; k++)
	    //if (i==0) F[i][k]=F[i+1][k]; else F[i][k] = F[i-1][k];
	    F[i][k]=F[t][k];
	}
      }	
    }
  }
    
  
  return 0;
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

    int R, C;
    scanf("%d %d", &R, &C);
    for (int i=0; i<R; i++){
      char sc[50];
      scanf("%s", sc);
      for (int j=0; j<C; j++){
	G[i][j] = sc[j];
	cerr << G[i][j];
      }
      cerr << "\n";
    }
    
    int rst = solve(R, C);
    

    printf("Case #%d:\n", iT);
    for (int i=0; i<R; i++){
      for (int j=0; j<C; j++){
	cout << F[i][j];
      }
      cout <<"\n";
    }
  }
  
  
  return 0;
}
