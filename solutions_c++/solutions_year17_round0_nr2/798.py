#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>


using namespace std;

int countDig(unsigned long int N,vector<int> &digs);
unsigned long int ipow(int a,int b){
  unsigned long int res=1;
  for (int i=1;i<=b;i++)
    res*=a;
  return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    int T,d;
    unsigned long int N;
    vector<int> digs(19,0);
    cin >> T;
    for(int tc=1;tc <= T;tc++){
      cin >> N;
      d = countDig(N,digs);
      cout << "Case #" << tc << ": ";
      for (int ii=1;ii<=d;ii++){
      for (int i=1;i<=d-1;i++){
        if (digs[d-i] > digs[d-i-1] && d!=1 ){
          N =N - N % ipow(10,d-i);
          N=N-1;
          d=countDig(N,digs);
        }
      }
      }
      cout << N <<'\n';
    }
    return 0;
}

int countDig(unsigned long int N,vector<int>& digs)
{
  int d=0;
  while (N!=0){
    digs[d] = N % 10;
    N = N / 10;
    d++;
  }

  return d;
}
