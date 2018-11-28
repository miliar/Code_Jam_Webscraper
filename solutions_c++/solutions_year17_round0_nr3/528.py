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
typedef vector<LL>	VLL;
typedef set<int>	SI;
typedef set<LL>	SLL;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair

//#define DEBUG


int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    LL N,K;
    cin>>N>>K;
    LL ans = N;
    if(K>1){
        ll n = 1;
        // (K - 1) >= 2^k - 1 ‚ð–ž‚½‚·Å‘å‚Ìk‚ð‹‚ßAn = 2^k - 1‚Æ‚·‚é
        while ((K - 1) >= (2*n - 1)){
            n = 2*n;
        }
        n--;
        LL Ndiv = (N-n) / (n+1);
        LL Nmod = (N-n) % (n+1);
        LL rest = K - n;
        ans = Ndiv;
        if(rest<= Nmod)ans++;
    }
    LL first = ans;
    first--;
    LL first2 = first / 2;
    cout<<"Case #"<<t<<": "<<(first&1)+first2<<" "<<first2<<endl;
  }
  return 0;
}

