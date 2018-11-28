#include <iostream>
#include <string>

using namespace std;

const int IMPOSSIBLE=-1;

int solve(const string& s,int k);

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    string s;
    int k;
    cin>>s>>k;
    int ret=solve(s,k);
    if(ret==IMPOSSIBLE)
      cout<<"Case #"<<i+1<<": IMPOSSIBLE\n";
    else
      cout<<"Case #"<<i+1<<": "<<ret<<'\n';
  }
}

void flip(char& c){
  if(c=='+')
    c='-';
  else
    c='+';
}

int solve(const string& s,int k){
  string board=s;
  int ret=0;
  for(int i=0;i+k<=board.size();i++)
    if(board[i]!='+'){
      ret++;
      for(int j=0;j<k;j++)
        flip(board[i+j]);
    }
  for(int i=0;i<board.size();i++)
    if(board[i]!='+')
      return IMPOSSIBLE;
  return ret;
}
