#include<iostream>
#include<queue>
#include<algorithm>
#include<utility>
#include <cmath>
#include <cstdio>

using namespace std;

int N,K;
double f( vector<double> v, double u ){
  v.push_back(1.0);
  for( int i = 0; i< v.size();i++){
    //      printf("v[%d] = %f\n",i,v[i]);
    double d = v[i+1] -v[i];
    if( d*(i+1)>= u ){
      return v[i]+(u/(i+1));
    }
    u-=d*(i+1);
  }
  return 1.0;
}

int main(void){
  int T;
  cin>>T;
  for( int c=1;c<=T;c++){
    cin>>N>>K;
    double u;
    cin>> u;
    vector<double> v;
    for( int i = 0;i<N;i++){
      double d;
      cin>>d;
      v.push_back( d);
    }
    sort(v.begin(),v.end() );
    double e = f( v,  u);

    double res = 1;
    for( int i = 0;i<v.size();i++){
      v[i] = max( v[i], e );
      //      printf("v[%d] = %f\n",i,v[i]);
      res*=v[i];
    }
    printf("Case #%d: %.6f\n",c,res);
    //    cout<<"Case #"<<c<<": "<<res<<endl;
  }
  return 0;
}

