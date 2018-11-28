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
#include <iomanip>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef map<string, int> MSI;
typedef vector<int>	VI;
typedef vector<string>	VS;
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

#define MULVAL 1000000

//#define DEBUG

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N,K;
    cin>>N>>K;
    double Ud;
    cin>>Ud;
    int U = (Ud+EPS)*MULVAL;
#ifdef DEBUG
cout<< Ud<<","<<U<<endl;
#endif
    priority_queue<LL, vector<LL>, greater<LL> > pll ;
    for(int n = 0 ; n < N ; n++){
        double Pi;
        cin>>Pi;
        ll p = (Pi+EPS)*MULVAL;
#ifdef DEBUG
cout<< Pi<<","<<p<<endl;
#endif
        pll.push(p);
    }
    for(int u = 0 ; u < U ; u++){
        ll v = pll.top();
        pll.pop();
        if(v<MULVAL)v++;
        pll.push(v);
#ifdef DEBUG
cout<< v<<",";
#endif
    }
#ifdef DEBUG
cout<<endl;
#endif
    double ans = 1.0;
    for(int n = 0 ; n < N;n++){
        double p = pll.top();
        pll.pop();
        ans *= p/MULVAL;
#ifdef DEBUG
cout<< p<<",";
#endif
    }
#ifdef DEBUG
cout<<endl;
#endif
    cout<<"Case #"<<t<<": "<<std::setprecision(20)<<ans<<endl;
  }
  return 0;
}

