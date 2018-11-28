#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
  int numCases;
  cin >> numCases;
  for (int testCase=1; testCase<=numCases; ++testCase) {
    cout << "Case #" << testCase << ":" << endl;
    int r,c;
    cin >> r >> c;
    vector<string> input(r), ret;
    for(int i=0;i<r;++i)
      cin >> input[i];
    ret = input;
    for(int i=0;i<c;++i)
      for(int j=1;j<r;++j)
        if (ret[j][i] == '?')
          ret[j][i] = ret[j-1][i];
    for(int i=0;i<c;++i)
      for(int j=r-2;j>=0;--j)
        if (ret[j][i] == '?')
          ret[j][i] = ret[j+1][i];
    for(int i=1;i<c;++i)
      for(int j=0;j<r;++j)
        if (ret[j][i] == '?')
          ret[j][i] = ret[j][i-1];
    for(int i=c-2;i>=0;--i)
      for(int j=0;j<r;++j)
        if (ret[j][i] == '?')
          ret[j][i] = ret[j][i+1];
    for(int i=0;i<r;++i)
      cout << ret[i] << endl;
  }
}