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
  int N;
  int K;
  iFile >> N >> K;


  vector<int> b;
  b.push_back(N);

  for(size_t i = 0; i < K - 1; ++i){
    int l = b.back();
    b.pop_back();
    if( l /2 !=0 ) b.push_back (l / 2);
    if( l - 1 - l/2 != 0)  b.push_back (l - 1 - l/2);
    sort(b.begin(), b.end());
  }

  int k = b.back();

  cout <<"Case #" << n <<": " <<k/2 << " " << k - 1 - k/2 << endl;
}



