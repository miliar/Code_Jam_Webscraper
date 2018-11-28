#include <stdio.h>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <stack>
using namespace std;
map<string,bool> dict;
stack<string> x;
int ans,k;

string flipCake(string state,int i,int k){
  int end = i+k;
  if(end > state.size())
    return state;
    
  for(;i<end;i++){
    if(state[i]=='+')
      state[i]='-';
    else
      state[i]='+';
  }
  return state;
}
bool isFinalState(string state){
  size_t found = state.find('-');
  if(found==string::npos)
    return true;
  return false;
}

int solve(string state){
  string newState;
  int cnt = 0;
  for(int i=0;i<state.size();i++){
    if(state[i]=='-'){
      cnt++;
      newState  = flipCake(state,i,k);
      if(state.compare(newState)==0){
        break;
      }
      else{
        state = newState;
      }
    }
  }
  if(isFinalState(state))
    return cnt;
  else
    return 1e9;
  
}

void myProgram(){
  int TC;
  cin >> TC;
  for(int cs=1;cs<=TC;cs++){
    ans=1e9;
    string state;
    
    cin >> state >> k ;
    
    ans =  solve(state);
    if(ans!=1e9)
      printf("Case #%d: %d\n",cs,ans);
    else
      printf("Case #%d: IMPOSSIBLE\n",cs);
  
  }
}
void test(){
  string state;
  int k;
  int TC;
  cin >> TC;
  for(int i=0;i<TC;i++){
    cin >> state >> k;
    cout << state << " " << k << endl;
  }
}
int main(){
  myProgram();
  //test();
  return 0;
}
