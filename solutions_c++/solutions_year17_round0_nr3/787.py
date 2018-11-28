#include <bits/stdc++.h>
using namespace std;
typedef map<long,long>::iterator it;
int main(){
  int n;
  cin>>n;
  for(int i=0;i<n;i++){
    long a,b;
    long x,y;
    long max;
    map<long,long> space;
    cin>>a>>b;
    x=y=a;
    y = (x%2?x/2:x/2-1);
    x/=2;
    space[x]++;
    space[y]++;
    for(long j=1;j<b;){
      // cout<<"max = "<<max<<endl;
      // cout<<"second_max = "<<second_max<<endl;
      if(space.size()==0){
        x=0;
        y=0;
        break;
      }
      it i=space.end();
      i--;
      max = i->first;
      
      y = (max%2?max/2:max/2-1);
      x=max/2;
      if(x)
        space[x]+=i->second;
      if(y)
        space[y]+=i->second;
      j+=i->second;
      space.erase(i);
      
      //cout<<"map size = "<<space.size();
    }
    // }
    cout<<"Case #"<<i+1<<": "<<x<<" "<<y<<endl;
  }
  return 0;
}