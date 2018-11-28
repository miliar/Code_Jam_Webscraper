#include<iostream>
#include<queue>
#include<algorithm>
#include<utility>
#include <cmath>
#include <cstdio>

using namespace std;
    int N,K;

int sum(const vector<int>& v){
  int sum=0;
  for( int i = 0;i<v.size();i++){
    sum+=v[i];
  }
  return sum;
}
int f( vector<pair<pair<int,int>,bool> > v ){
  vector<int> fr;
  vector<int> frc;
  vector<int> frj;

  int cnt = 0;
  int sc =0; // sum act
  int sj=0; // sum act
  for( int i=0;i<v.size();i++){

    //    cout<<"s = "<< v[i].first.first<<", e = "<<v[i].first.second<<", b = "<<v[i].second<<endl;


    if( v[i].second ){
      sj+=v[i].first.second-v[i].first.first;
    }else{
      sc+=v[i].first.second-v[i].first.first;
    }


    if( v[i].second != v[(i+1)%v.size()].second ){
      cnt++;
      fr.push_back( (v[(i+1)%v.size()].first.first - v[i].first.second + 1440)%1440 );
    }else if( v[i].second == false ){
      frc.push_back( (v[(i+1)%v.size()].first.first - v[i].first.second + 1440)%1440 );
    }else if( v[i].second == true ){
      frj.push_back( (v[(i+1)%v.size()].first.first - v[i].first.second + 1440)%1440 );
    } 


  }

  //  cout<< "sj = " << sj <<endl;
  //  cout<< "sc = " << sc <<endl;
  //  cout<< "sum(fr) = " << sum(fr) <<endl;
  //  cout<< "sum(frc)" << sum(frc)  <<endl;
  //  cout<< "sum(frj)" << sum(frj)  <<endl;



  int tmpl, tmpu;
  tmpl = sc+sum(frc);
  tmpu = sc+sum(frc)+sum(fr);
  if( tmpl <= 720 && 720 <= tmpu )return cnt;



  if( tmpl > 720 ){
    sort( frc.begin(), frc.end(), greater<int>() );
    while(tmpl > 720 ){
      cnt+=2;
      tmpl-=frc[0];
      frc.erase(frc.begin());
    }
  }else if( tmpu < 720 ){
    sort( frj.begin(),frj.end(), greater<int>() );
    while( tmpu < 720 ){
      cnt+=2;
      tmpu+=frj[0];
      frj.erase(frj.begin());
    }
  }
  return cnt;
}



int main(void){
  int T;
  cin>>T;
  for( int c=1;c<=T;c++){
    int Ac,Aj;
    cin>>Ac>>Aj;
    vector<pair<pair<int,int>,bool> > v;
    for( int i = 0;i<Ac+Aj;i++){
      pair<pair<int,int>,bool> p;
      cin>>p.first.first>>p.first.second;
      p.second= (i>=Ac);
      v.push_back(p);
    }
    sort(v.begin(),v.end());

    int cnt = f(v);






    cout<<"Case #"<<c<<": "<<cnt<<endl;
  }
  return 0;
}

