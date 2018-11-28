#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>
#include <limits>
using namespace std;

const string inpFileName="B-small-attempt0.in";
const string outFileName="B-small.out";


bool isTidy(std::vector<int> num){
  int i=0;
  while (num[i]==0 && i<num.size())
    i++;
  
  while (i<num.size()-1){
    if (num[i]<=num[i+1])
      i++;
    else
      return false;
  }
  return true;
}

string tidy(string sNum){

  string tidyNum = "";
  int N = sNum.length();
  std::vector<int> num;

  int j=0;
  while (sNum[j]=='0') j++;
  
  for (int i=j; i<N; i++){
    int n = sNum.at(i) - '0';
    num.push_back(n);
  }

  N = num.size();
  
  if (!isTidy(num)){
    int i=0;
    while (num[i]<num[i+1])
      i++;
    for (int j=i+1; j<N; j++)
      num[j] = 9;
    num[i] = num[i]-1; 
  }

  int i=0;
  while (num[i]==0) i++;
  for (int j=i; j<num.size(); j++){
    tidyNum = tidyNum + std::to_string(num[j]);
  }
  
  return tidyNum;

  
}

int main(int argc, char **argv){

  int nTests;
  FILE *finp = fopen(inpFileName.c_str(),"r");
  FILE *fout = fopen(outFileName.c_str(), "w");
  fscanf(finp, "%d", &nTests);
  for (int iTest=1; iTest<=nTests; iTest++){

    char sNum[50]; 
    fscanf(finp, "%s", sNum);

    string result = tidy(std::string(sNum));
    
    fprintf(fout, "Case #%d: %s\n", iTest, result.c_str());
  }
  

  fclose(finp);
  fclose(fout);
  
  return 0;
}
