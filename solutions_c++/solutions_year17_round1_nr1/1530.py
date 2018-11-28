// codejam.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <bitset>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

#define LOOPI(N) for(int i = 0; i < N; ++i)
#define LOOPJ(N) for(int j = 0; j < N; ++j)

bool inStr(char c, string& str)
{
  int n = str.size();
  for(int i = 0; i < n; ++i){
    if(c == str[i]){
      return true;
    }
  }
  return false;
}

void removeStr(string key, string& str)
{
  int n = key.size();
  int m = str.size();
  for(int i = 0; i < n; ++i){
    for(int j = 0; j < str.size(); ++j){
      if(key[i] == str[j]){
        str.replace(j, 1, 1, ' ');
        break;
      }
  
    }
  }
}

int sum(vector<int> a)
{
  int sum_ = 0;
  LOOPI(a.size()){
    sum_ += a[i];
  }
  return sum_;
}

string DecimalToBinaryString(int a)
{
  string binary = "";
  int mask = 1;
  for(int i = 0; i < 31; i++)
  {
    if((mask&a) >= 1)
      binary = "1"+binary;
    else
      binary = "0"+binary;
    mask<<=1;
  }
  return binary;
}

/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////

void solve(int n, ifstream& iFile);

int main(int argv, char **argc)
{
  if(argv < 2) return 1;
  string s(argc[1]);

  ifstream iFile(argc[1]);
  
  int n = 0;

  if(iFile.good()) {
    iFile >> n;
  }
  else return 1;

  for(int i = 1; i <= n; i++){
    solve(i, iFile);
  }
  return 0;
}

void solve(int n, ifstream& iFile)
{
  int R;
  int C;
  iFile >> R >> C;

  vector<vector<char> > matrix(R);
  for(size_t r = 0; r < R; ++r){
    matrix[r].resize(C);
    for(size_t c = 0; c < C; ++c){
      iFile >> matrix[r][c];
    }
  }
  char curr = '?';
  set<int> emptyrow;
  int nonemptyrow = 0;
  for(size_t r = 0; r < R; ++r){
    size_t c = 0;
    int start = 0;
    for(c = 0; c < C; ++c){//find first non ?
      if(matrix[r][c] != '?' ){
        start = c;
        break;
      }
    }
    if(c == C){//empty row
      emptyrow.insert(r);
      continue;
    }
    else{
      nonemptyrow = r;
      for(; c < C; ++c){
        if(matrix[r][c] == '?') matrix[r][c] = curr;
        else curr = matrix[r][c];
      }
      for(c = 0 ; c < start ; ++c) matrix[r][c] = matrix[r][start];
    }
  }
  int curRow = nonemptyrow;
  for(int r = nonemptyrow; r < R; ++r){
    if(emptyrow.find(r) != emptyrow.end()){
      for(int c = 0; c < C; ++c) matrix[r][c] = matrix[curRow][c];
    }
    else curRow = r;
  }
  curRow = nonemptyrow;
  for(int r = nonemptyrow; r >= 0 ; --r){
    if(emptyrow.find(r) != emptyrow.end()){
      for(int c = 0; c < C; ++c) matrix[r][c] = matrix[curRow][c];
    }
    else curRow = r;
  }
  cout <<"Case #" << n <<":" << endl;

  for(size_t r = 0; r < R; ++r){
    for(size_t c = 0; c < C; ++c){
      cout << matrix[r][c];
    }
    cout << endl;
  }
  //cout <<"Case #" << n <<":" << endl;
}



