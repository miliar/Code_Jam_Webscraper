#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>
#include <limits>
using namespace std;

const string inpFileName="C-large.in";
const string outFileName="C-large.out";

bool isEven(long long N){
  return (N % 2 == 0);
}

void solve(long long N, long long K, long long &rMax, long long &rMin){

  int x=0;
  long long twoPx = 1;
  long long sum = 1;
  while (sum < K){
    x++;
    twoPx = twoPx*2;
    sum += twoPx;
  }

  if (twoPx - 1 > K)
    twoPx = twoPx/2;

  long long oddN, evenN;
  long long nOdd, nEven;

  if (isEven(N)){
    evenN = N;    nEven = 1; nOdd = 0; oddN = 0;
  } else {
    oddN = N; nOdd = 1; nEven = 0; evenN = 0;
  }
    
  for (int i=0; i<x; i++){
    long long evenD;
    long long oddD;
    long long nEvenD = 0;
    long long nOddD = 0;

    long long eD1 = evenN/2 - 1; long long eD2 = evenN/2;
    long long oD1 = (oddN - 1)/2; long long oD2 = oD1;

    if (isEven(eD1) && eD1>=0){
      evenD = eD1; nEvenD += nEven;
    } else {
      oddD = eD1; nOddD += nEven;
    }

    if (isEven(eD2) && eD2 >=0){
      evenD = eD2; nEvenD += nEven;   
    } else {
      oddD  = eD2; nOddD += nEven;
    }

    if (isEven(oD1)){
      if (nOdd>0) evenD = oD1;
      nEvenD += 2*nOdd;
    } else {
      if (nOdd>0) oddD = oD1;
      nOddD += 2*nOdd;
    }

    evenN = evenD;
    oddN = oddD;
    nEven = nEvenD;
    nOdd = nOddD;        
  }
  long long leftOver = K - (twoPx - 1);
  long long maxN;
  long long cellSize;
  if (evenN > oddN){
    cellSize = evenN;
    if (leftOver > nEven)
      cellSize = oddN;
  }else{
    cellSize = oddN;
    if (leftOver > nOdd)
      cellSize = evenN;
  }

  if (isEven(cellSize)){
    rMax = cellSize/2;
    rMin = rMax - 1;
  } else {
    rMax = (cellSize-1)/2;
    rMin = rMax;
  }

  return;
  
}




int main(int argc, char **argv){

  int nTests;
  FILE *finp = fopen(inpFileName.c_str(),"r");
  FILE *fout = fopen(outFileName.c_str(), "w");
  fscanf(finp, "%d", &nTests);
  for (int iTest=1; iTest<=nTests; iTest++){

    long long N, K;
    fscanf(finp, "%lld %lld", &N, &K);

    long long rMax, rMin;
    solve(N, K, rMax, rMin);
    
    fprintf(fout, "Case #%d: %lld %lld\n", iTest, rMax, rMin );
  }
  

  fclose(finp);
  fclose(fout);
  
  return 0;
}
