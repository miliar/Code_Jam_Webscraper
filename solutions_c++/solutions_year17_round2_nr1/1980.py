#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<utility>
#include<set>
#include<queue>
#include<list>
#include<stack>
#include<iomanip>

using namespace std;


void getAns(double d,int n, vector<pair<double,double>> horses){
  double maxTime=(d-horses[0].first)/horses[0].second;
  for(int i=1;i<n; i++){
    maxTime=max(maxTime,(d-horses[i].first)/horses[i].second);
  }
  cout<<setprecision(12)<< d/maxTime<<endl;

}


int main(){

  int T;
  cin>>T;  

  for(int i=1; i<=T; i++){
    double d;
    cin>>d;
    int n;
    cin>>n;
    vector<pair<double,double>> horses;
    for(int i=0; i<n; i++){
      double d1,d2;
      cin>>d1>>d2;
      horses.push_back(make_pair(d1,d2));
    }
        
    
    cout<<"Case #"<<i<<": ";
    getAns(d,n,horses);
    
    
  }

  
  

  return 0;

}
    
