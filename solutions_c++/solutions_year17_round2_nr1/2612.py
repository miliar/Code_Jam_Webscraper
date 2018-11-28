#include<iostream>
#include<math.h>
#include<cmath>
#include<stdio.h>
using namespace std;
int main(){
  long int t,n;
  double total_dist,speed,inital_pos,max_time;
  cin>>t;
  int iteration=1;
  while(iteration<=t){
    cin>>total_dist;
    cin>>n;
    max_time=0;
    while(n--){
      cin>>inital_pos>>speed;
      if(max_time<(total_dist-inital_pos)/speed)
        max_time=(total_dist-inital_pos)/speed;
    }
    printf("case #%d: %.6f\n",iteration++, total_dist/max_time);
    // cout<<"case #"<<iteration++<<": "<<total_dist/max_time<<endl;
  }
  return 0;
}
