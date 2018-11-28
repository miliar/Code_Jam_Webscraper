#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <queue>
using namespace std;

#define INF 1000000000
#define REP(i,a,b) for(int i = int(a); i<=int(b);i++)


int main() {
  int TC;
  scanf("%d",&TC);
  REP(a,1,TC){
    int n, k;
    scanf("%d%d",&n,&k);
    priority_queue<int> q;
    q.push(n);
    int counter = 1;
    while(counter!=k){
      int tmp = q.top();
      // cout<<tmp<<endl;
      q.pop();
      if((tmp-1)%2==0){
        q.push((tmp-1)/2);
        q.push((tmp-1)/2);
      }
      else{
        q.push(tmp/2-1);
        q.push(tmp/2);
      }
      counter++;
    }
    int b = q.top();
    if((b-1)%2==0){
      cout<<"Case #"<<a<<": "<<(b-1)/2<<" "<<(b-1)/2<<endl;
    }
    else
      cout<<"Case #"<<a<<": "<<b/2<<" "<<b/2-1<<endl;
  }

}
