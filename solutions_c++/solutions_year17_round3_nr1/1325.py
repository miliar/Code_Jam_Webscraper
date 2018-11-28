#include <bits/stdc++.h>
#define double long double
#define PI M_PI
#define N 1010
using namespace std;
typedef pair<double,double> P;
vector<P>A;

double dp[N][N];

double Max(double &a,double b){return a=max(a,b);}

int main(){
  int q,cnt=0;
  cin>>q;
  while(q--){
    int n,K;
    cin>>n>>K;    


    A.resize(n);
    for(int i=0;i<n;i++){
      double r,h;
      cin>>r>>h;
      A[i] = P(r,h);
    }    
    sort(A.begin(),A.end(),greater<P>());
    for(int i=0;i<N;i++)
      for(int j=0;j<N;j++)dp[i][j] = 0;
    
    for(int i=0;i<n;i++){
      double r = A[i].first;
      double  h =A[i].second;
      for(int j=0;j<=K;j++){
	if(j==0) Max(dp[i+1][j+1], (PI*r*r)+((r+r)*PI*h));
	Max(dp[i+1][j],dp[i][j]);
	Max(dp[i+1][j+1],dp[i][j]+(r+r)*PI*h);
      }
    }
    
    cout<<"Case #"<<++cnt<<": ";
    printf("%.9Lf\n",dp[n][K]);
    
  }
  return 0;
}
