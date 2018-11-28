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
typedef vector<string>	VS;
typedef vector<VS>	VSS;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair
typedef vector<PI>	VPI;

#define BMAX 50

int calc21(vector<PI> & vA)
{
    int int1 = vA[0].first - 0;
    int int2 = vA[1].first - vA[0].second;
    int1 += 1440 - vA[1].second;
    if(max(int1,int2)>=720) return 2;
    return 4;
}

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int Ac,Aj;
    cin>>Ac>>Aj;
    vector<PI> vAc;
    vector<PI> vAj;
    for(int i = 0 ; i < Ac ; i++){
        int t1,t2;
        cin>>t1>>t2;
        vAc.push_back(make_pair(t1,t2));
    }
    sort(vAc.begin(),vAc.end());
    for(int i = 0 ; i < Aj ; i++){
        int t1,t2;
        cin>>t1>>t2;
        vAj.push_back(make_pair(t1,t2));
    }
    sort(vAj.begin(),vAj.end());
    int ans = 0;
    if(Ac+Aj == 1){
        ans = 2;
    }
    else if(Ac == 1 && Aj == 1){
        ans = 2;
    }
    else if(Ac == 2 && Aj < 2){
        ans = calc21(vAc);
    }
    else if(Ac < 2 && Aj == 2){
        ans = calc21(vAj);
    }
    else if(Ac == 2 && Aj == 2){
        ans = 4;
    }
    cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}

