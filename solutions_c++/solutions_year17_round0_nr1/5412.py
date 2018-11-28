#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

struct state{
  
};

const string inpFileName="A-small-attempt1.in";
const string outFileName="small.out";

bool exists(std::string &state, std::vector<string>&stateArr){  
  for (int i=stateArr.size()-1; i>=0; i--){
    if (state.compare(stateArr[i])==0)
      return true;
  }
  return false;
}

bool happy(string S){
  for (int i=0; i<S.length(); i++)
    if (S[i]=='-')
      return false;
  return true;
}

bool shouldFlip(string S, int startPos, int K){
  if (startPos+K>S.length())
    return false;

  for (int i=startPos; i<startPos+K; i++){
    if (S[i]=='-')
      return true;
  }

  return false;
}

string flipString(string S, int startPos,  int K){
  string fS = S;
  for (int i=startPos; i<startPos+K; i++)
    if (fS[i]=='+') fS[i]='-';
    else fS[i]='+';

  return fS;
}

int search(string S, int K){

  if (happy(S))
    return 0;
  
  std::vector<string> states;
  std::vector<int> flips;
  
  int N = S.length();
  states.push_back(S);
  flips.push_back(0);
  int idx = 0;

  while (idx<states.size()){
    string cS = states[idx];
    int nFlips = flips[idx];
    for (int i=0; i<=cS.length()-K; i++){
      //if (!shouldFlip(S, i, K))
      //	continue;
      
      string nS = flipString(cS, i, K);
      if (!exists(nS,states)){
	if (happy(nS))
	  return nFlips+1;
	states.push_back(nS);
	flips.push_back(nFlips+1);	       	  
      }
    }
    idx++;    
  }
  return -1;
  
}

int main(int argc, char **argv){

  int nTests;
  FILE *finp = fopen(inpFileName.c_str(),"r");
  FILE *fout = fopen(outFileName.c_str(), "w");
  fscanf(finp, "%d", &nTests);
  for (int iTest=1; iTest<=nTests; iTest++){
    char S[1000];
    int K;
    fscanf(finp, "%s", S);
    fscanf(finp, "%d", &K);
    cout << std::string(S) << "\t" << K <<"\n";
    int nFlips = search(std::string(S), K);
    cout << nFlips << "\n";

    fprintf(fout, "Case #%d: ", iTest);
    if (nFlips<0)
      fprintf(fout, "IMPOSSIBLE\n");
    else
      fprintf(fout, "%d\n", nFlips);
  }
  

  fclose(finp);
  fclose(fout);
  
  return 0;
}
