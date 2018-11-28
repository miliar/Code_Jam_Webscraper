#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>

// #include <gmpxx.h>
//g++ mycxxprog.cc -lgmpxx -lgmp

using namespace std;




int main(){
	int nb;
	cin >>nb;
	for(int cases=0; cases<nb; cases++){
    cout << "Case #"<<cases+1<<": ";
    long long N, Q;
    cin >>N>>Q;
    vector<pair<double, double> >h(N);
    for(int i=0;i<N;i++) cin >>h[i].first >> h[i].second;
    vector<vector<double> > G(N, vector<double>(N,0));
    double big = 100000000;
    big = big*big;big = big*big;
    for(int i=0;i<N;i++)
      for(int j=0;j<N;j++){
        cin >> G[i][j];
        if(G[i][j]==-1) G[i][j]= big;
      }
    for(int tt =0; tt<N; tt++)
      for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
          for(int k=0;k<N;k++){
            double temp = G[i][j]+G[j][k];
            if( temp<G[i][k]) G[i][k]=temp;       
          }
    for(int i=0;i<N;i++)
      for(int j=0;j<N;j++){
        if(G[i][j]>h[i].first)G[i][j]= big;
        else G[i][j]= G[i][j]/h[i].second;
      }
    for(int tt =0; tt<N; tt++)
      for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
          for(int k=0;k<N;k++){
            double temp = G[i][j]+G[j][k];
            if(temp<G[i][k]) G[i][k]=temp;       
          }
    for(int i=0;i<Q;i++){
      int a,b;
      cin>> a>>b;
      cout<<fixed<<setprecision(6)<<G[a-1][b-1];
      if( i<Q-1)cout<<" ";
    }
    cout<<endl;
    
  }
	return 0;
}
