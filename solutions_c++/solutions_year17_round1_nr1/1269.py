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
typedef vector<string>	VS;

//#define DEBUG

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int R,C;
    cin>>R>>C;
    VS vs;
    vs.clear();
    for(int r = 0 ; r < R ; r++){
        string tmp;
        cin>>tmp;
        vs.push_back(tmp);
    }
#ifdef DEBUG
        cout<<"t="<<t<<endl;
#endif
#ifdef DEBUG
    for(int r = 0 ; r < R ; r++){
        cout<<vs[r]<<endl;
    }
#endif
    int prevline = -1;
    for(int r = 0 ; r < R ; r++){
        // count ?
        int countq = 0;
        for ( int c = 0 ; c < C ; c++){
            if(vs[r][c] == '?') countq++;
        }
#ifdef DEBUG
    cout<<"countq="<<countq<<endl;
#endif

        if(countq == C){
            if(prevline != -1){
                for ( int c = 0 ; c < C ; c++){
                    vs[r][c] = vs[prevline][c];
                }
                prevline = r;
            }
        } else {
            int prevcol = -1;
            for ( int c = 0 ; c < C ; c++){
                if(vs[r][c] == '?'){
                    if(prevcol != -1){
                        vs[r][c] = vs[r][prevcol];
                    }
                }else{
                    if(prevcol==-1){
                        for(int cc = 0; cc < c; cc++){
                            vs[r][cc] = vs[r][c];
                        }
                    }
                    prevcol = c;
                }
            }
            if(prevline == -1){
                for(int rr = 0 ; rr < r ; rr++){
                    for ( int c = 0 ; c < C ; c++){
                        vs[rr][c] = vs[r][c];
                    }
                }
            }
            prevline = r;
        }
#ifdef DEBUG
        cout<<vs[r]<<endl;
#endif
    }
    cout<<"Case #"<<t<<": "<<endl;
    for(int r = 0 ; r < R ; r++){
        cout<<vs[r]<<endl;
    }
#ifdef DEBUG
        cout<<"t="<<t<<endl;
#endif
  }
  return 0;
}

