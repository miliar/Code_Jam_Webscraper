#include<iostream>
#include<stdio.h>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;
int D;
int N;
int main(void){
  int T;
  cin>>T;
  for( int c=1;c<=T;c++){
    cin>>D>>N;
    double time = 0;
    for( int i=0;i<N;i++){
      int k,s;
      cin>>k>>s;
      time = max(time, (double)(D-k)/(double)s );
    }
    //    cout<<"Case #"<<c<<": "<< setprecision(5) <<(double)D/time<<endl;
    printf("Case #%d: %f\n", c, (double)D/time);


  }
  return 0;
}
