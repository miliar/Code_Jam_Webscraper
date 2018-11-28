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

//#define DEBUG

int checkTidy(string & N)
{
    int L = N.length();
    if(L <=1) return 1;
    char prev = N[0];
    for(int i = 1;i < L ; i++){
        char curr = N[i];
        if(prev>curr) return 0;
        prev = curr;
    }
    return 1;
}
void createMinTidy(string &N, string &ans)
{
    // check last ascending position
    int lastpos = 0;
    char prev = N[0];
    for(int i = 1 ; i < N.length() ; i++){
        char curr = N[i];
        if(prev < curr) lastpos = i;
        else if(prev > curr) break;
        prev = curr;
    }
    int index = 0;
    for(index = 0 ; index < lastpos ; index++){
        ans += N[index];
    }
    char ci = N[index];
    if(!(index == 0 && N[index]=='1')){
        ans += N[index] - 1;
    }
    index++;
    for( ; index < N.length() ; index++){
        ans += "9";
    }
}

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    string N;
    string ans;
    cin>>N;
    int f;
    ans = "";
    f = checkTidy(N);
    if(f == 0){
        createMinTidy(N,ans);
    } else{
        ans = N;
    }
    cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}

