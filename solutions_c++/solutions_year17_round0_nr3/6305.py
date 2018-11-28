//
//  3.cpp
//  Hello World
//
//  Created by Sri Krishna Vijayapuri on 4/8/17.
//  Copyright © 2017 test. All rights reserved.
//

#include <iostream>
#include <queue>
#include <cmath>
using namespace std;
typedef long long ll;

int main(){
  ll t,n,k,low=0,high=0,val;
  cin>>t;
  for(ll i=1;i<=t;i++){
    priority_queue<ll> myQ;
    cin>>n>>k;
    myQ.push(n);
    while(k--){
      val=myQ.top();
      myQ.pop();
      val--;
      high=ceil(val/2.0);
      low=val-high;
      if(high) myQ.push(high);
      if(low) myQ.push(low);
    }
    cout<<"Case #"<<i<<": "<<high<<" "<<low<<endl;
  }
  return 0;
}
