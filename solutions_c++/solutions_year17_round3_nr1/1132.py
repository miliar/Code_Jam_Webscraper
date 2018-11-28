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
#include <iomanip>

using namespace std;

#define PI 3.14159265358979

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

pair<int, int> validRange(int p, int b)
{
  pair<int, int> t(-1,-1);

  double tmp = p /0.9/b;
  if((int)tmp * b * 1.1 >= p) t.second = (int)tmp;
  tmp = p / 1.1 / b;
  if(((int)tmp + 1) * b * 0.9 <= p) t.first = (int)tmp + 1;
  if(t.first == -1 && t.second != -1) t.first = t.second;
  else if(t.second == -1 && t.first != -1) t.second = t.first;
  return t;
}

void sort(vector<pair<int, int> >& row)
{
  for(int i = 0; i < row.size(); ++i){
    for(int j = i + 1; j < row.size(); ++j){
      if( row[j].first < row[i].first){
        pair<int,int> t = row[i];
        row[i] = row[j];
        row[j]= t;
      }
      else if(row[j].first == row[i].first && row[j].second < row[i].second){
        pair<int,int> t = row[i];
        row[i] = row[j];
        row[j]= t;
      }
    }
  }
}

bool inRange(int a, pair<int,int> b)
{
  if(a >= b.first && a <= b.second) return true;
  return false;
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
  int K;
  int N;
  iFile >> N >> K;

  vector<double> rad(N);
  vector<double> high(N);
  for(int r = 0 ; r < N; ++r){
    iFile >> rad[r] >> high[r];
  }
  int count = 0;
  double total = 0.0;
  double max_r = 0;
  while(count < K -1)
  {
    double max = 0;
    int index = 0;
    //find next biggest outsider
    for(int m = 0; m < N; ++m){
      double out = high[m] * rad[m] * 2 * PI;
      if(out > max ){
        max  = out;
        index = m;
      }
    }
    //update bottom one
    if( rad[index] > max_r) max_r = rad[index];
    //reset this item to 0
    rad[index] = 0;
    high[index]= 0;
    total += max;
    ++count;
  };
  total += PI * max_r * max_r;
  double max = 0;
  int index = 0;
  //Find the bottom one
  for(int m = 0; m < N; ++m){
    double out = 2.0 * high[m] * rad[m] * PI;
    if(rad[m] > max_r){
     out += PI * ( rad[m] * rad[m] - max_r * max_r);
    }
    if(out > max){
       max = out;
    }
  }
  total += max;
  cout <<"Case #" << n <<": " << setiosflags(ios::fixed) << std::setprecision(9) << total << endl;
  //cout <<"Case #" << n <<":" << endl;
}



