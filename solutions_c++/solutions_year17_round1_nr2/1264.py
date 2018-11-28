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

//#define DEBUG


int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N,P;
    VS vs;
    cin>>N>>P;
    VI Ri;
    for(int n = 0; n < N ; n++){
        int tmp;
        cin>>tmp;
        Ri.push_back(tmp);
    }
    VII Qij;
    for(int n = 0; n < N ; n++){
        VI tmpvi;
        for(int p = 0; p < P ; p++){
            int t;
            cin >> t;
            tmpvi.push_back(t);
        }
        Qij.push_back(tmpvi);
    }
    int ans = 0;
    vector<int> per(P);
    for(int i=0;i<P;i++)per[i] = i;
    do{
#ifdef DEBUG
        for(int p = 0 ; p < P ; p++)cout<<per[p] <<" ";
        cout<<endl;
#endif
        int tmpans = 0;
    for(int pp = 0; pp < P ; pp++){
        int numallbig = 0;
        int numallsmall = 0;
        int addflag = 1;
        for(int n = 0; n < N ; n++){
            int p = pp;
            if(n>=1)p= per[pp];
            int numbig = (int)((double)Qij[n][p] / (Ri[n]*0.90));
            int numsmall = (int)((double)Qij[n][p] / (Ri[n]*1.10));
            if(numbig==numsmall && abs((double)Qij[n][p] /(Ri[n]*1.10)) >numsmall + EPS){
                addflag = 0;
                break;
            }else if(abs((double)Qij[n][p] /(Ri[n]*1.10)) >numsmall + EPS){
                numsmall++;
            }
            if(n==0){
                numallbig = numbig;
                numallsmall = numsmall;
            }
            else{
                if(numbig < numallsmall || numsmall >numallbig ){
                    addflag = 0;
                    break;
                }
                numallbig = min(numallbig, numbig);
                numallsmall = max(numallsmall, numsmall);
            }
#ifdef DEBUG
            cout<<p<<","<<n<<","<<numallbig<<","<<numallsmall<<endl;
//            cout<<p<<","<<n<<","<<numbig<<","<<numsmall<<endl;
//            cout<<p<<","<<n<<endl;
#endif
        }
        tmpans += addflag;
    }
        ans = max(ans,tmpans);
    }while(next_permutation(per.begin(),per.end()));

    cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}

