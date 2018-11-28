#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <unordered_map>
#include <unordered_set>
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define fillv(v,a) fill(v.begin(),v.end(),a)
#define EPS 1e-9
typedef long long ll;
typedef std::pair<int,int>pii;
typedef std::vector<int> vi;

using namespace std;

int N,K;
double U;
double prob[50];
class Solution{
public:
  void solve(int t){
    double gap=0;
    forn(i,N)gap+=1-prob[i];
    if(equal(gap,U)){printf("Case #%d: 1.000000\n",t);return;}
    if(equal(gap,N)){
      double a=U/N,p=pow(a,N);
      printf("Case #%d: %.6f\n",t,p);
      return;
    }
    while(U>EPS){
      sort(prob,prob+N);
      int i;
      for(i=0;i<N-1;i++)if(prob[i]<prob[i+1]-EPS)break;
//      printf("i %d\n",i);
      if(i==N-1){
        double a=U/N+EPS;
        forn(i,N)prob[i]+=a;
        break;
      }
      else{
        if((prob[i+1]-prob[i])*(i+1)<U+EPS){
          double a=(prob[i+1]-prob[i]);
          for(int j=0;j<i+1;j++)prob[j]+=a,U-=a;
        }
        else{
          double a=U/(i+1);
//          printf("add %lf\n",a);
//          forn(k,N)printf(" %lf",prob[k]);
          for(int j=0;j<i+1;j++)prob[j]+=a;
          U=0;
          break;
        }
      }
    }
    double p=1;
    forn(i,N)p*=prob[i];
//    printf("U %lf\n",U);
    printf("Case #%d: %.6f\n",t,p);
  }
  bool equal(double a,double b){return fabs(a-b)<EPS;}
};

int main(int argc, const char * argv[]) {
  int t;
  cin>>t;
  Solution sol;
  forn(i,t){
    cin>>N>>K>>U;
    forn(i,N)cin>>prob[i];
    sol.solve(i+1);
    // fprintf(stderr, "Case #%d:\n", t + 1);
  }
}

