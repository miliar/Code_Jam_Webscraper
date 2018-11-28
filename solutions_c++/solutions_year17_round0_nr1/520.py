#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair

int check_all_flipped(string &S)
{
    for(int i = 0 ; i < S.length() ; i++){
        if( S[i] == '-') return 0;
    }
    return 1;
}

void flipp(string &S, int index, int K)
{
    for(int i = index ; i < index + K ; i++){
        if(S[i] == '-') S[i] = '+';
        else S[i] = '-';
    }
}

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    string S;
    int K;
    cin>>S>>K;
    int count = 0;
    int index = 0;
    int check = 0;
    while(index <= S.length() - K){
        if((check = check_all_flipped(S))!=0) break;
        count++;
        while(S[index] == '+')index++;
        flipp(S, index, K);
    }
    if(check){
      cout<<"Case #"<<t<<": "<<count<<endl;
    }else{
      cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
    }
  }
  return 0;
}

