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
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair
typedef vector<string>	VS;

//#define DEBUG

static const double PI_VALUE = 3.14159265359;

int main(void)
{
  int T,t;
  int ret;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N,K;
    cin>>N>>K;
    vector<pair<pair<double,double>,int> > vd;
    for(int n=0;n<N;n++){
        int R,H;
        cin>>R>>H;
        double surfice_h = 2*PI_VALUE*R*H;
        double surfice_r = PI_VALUE*R*R;
#ifdef DEBUG
cout<< surfice_h<<","<<surfice_r<<endl;
#endif
        vd.push_back(make_pair(make_pair(surfice_h, -surfice_r), n));
    }
    sort (vd.begin(), vd.end());
    double ans = 0;
    vector<int>usedv;
    double maxr = 0;
    for(int k = 0 ; k < K-1 ; k++){
        int index = N-1-k;
        double surfice_h = vd[index].first.first;
        double surfice_r = - vd[index].first.second;
        int n = vd[index].second;
        ans += surfice_h;
        usedv.push_back(n);
        if(surfice_r > maxr)maxr = surfice_r;
#ifdef DEBUG
cout<<"stage1:"<< n<<","<<ans<<endl;
#endif
    }
    double maxhr = 0;
    for(int n = 0 ; n < N ; n++){
        int flag = 1;
        for(int i = 0 ; i < usedv.size();i++){
            if(usedv[i] == vd[n].second){
                flag = 0 ;
                break;
            }
        }
        if(flag){
            double surfice_h = vd[n].first.first;
            double surfice_r = - vd[n].first.second;
            double hr = surfice_h + max(surfice_r - maxr, 0.0);
            if(hr > maxhr){
                maxhr = hr;
#ifdef DEBUG
cout<< n<<","<<maxhr<<endl;
#endif
            }
        }
    }
    ans += maxhr+maxr;
    cout<<"Case #"<<t<<": "<<std::setprecision(20)<<ans<<endl;
  }
  return 0;
}

