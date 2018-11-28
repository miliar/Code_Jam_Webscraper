#include<iostream>
#include<queue>
#include<algorithm>
#include<utility>
#include <cmath>
#include <cstdio>

using namespace std;
    int N,K;

pair<double,double> f( vector<pair<double,double> > v ){
  sort( v.begin(),v.end(),greater<pair<double,double> >() );
  pair<double,double> res;
  for( int i = 0;i<K-1;i++ ){
    res.first+= v[i].first;
    res.second=max(res.second,v[i].second);
  }
  return res;
}


int main(void){
  int T;
  cin>>T;
  for( int c=1;c<=T;c++){

    double r = 0;
    cin>>N>>K;
    vector<pair<double,double> > v;
    for(int i = 0;i<N;i++){
      double tmpr, tmph;
      cin>>tmpr>>tmph;
      v.push_back(make_pair(tmpr*2*M_PI*tmph, tmpr*tmpr*M_PI));
    }
    for( int i = 0;i<N;i++){
      pair<double,double> tmpp=v[i];
      v[i]=make_pair(0,0);
      pair<double,double> res=f(v);
      r= max(r , res.first+tmpp.first+max(res.second,tmpp.second) );
      v[i]=tmpp;
    }



    //    cout<<"Case #"<<c<<": "<<r<<endl;
    printf("Case #%d: %.9f\n", c, r);
  }
  return 0;
}

