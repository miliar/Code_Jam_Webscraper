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
           
    int D, N;    
    vector<double> time;
    cin >> D >> N;
    for (int i=0; i<N; i++){
      int K, S;
      cin >> K >> S;
      double ti = (D-K)*1.0/S;
      time.push_back(ti);
    }
    std::sort(time.begin(), time.end());

    
    double rst = D/(time[N-1]);   

    //    cerr << "Case " << iT << "   " << time[N-1] <<"\n";
    
    printf("Case #%d: %.6f\n", iT, rst);
    
  }
  
  
  return 0;
}
