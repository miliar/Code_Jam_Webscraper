#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

long long int lasttidy(long long int x){
  long long int i,size,j,r;
  bool resp;
  string s;
  for(i=x;i>9;i--){
    if(i % 10 == 0)
      continue;
    s=to_string(i);
    size=s.size();
    resp=true;
    for(j=1;j<size;j++){
      if(s[j-1]>s[j]){
        resp=false;
        r=atoll(s.substr(j,size-j).c_str());
        i-=r;
        break;
      }
    }
    if(resp==true)
      return i;
  }
  return i;
}

int main( void ) {

  int T;
  long long int x;

  scanf("%d",&T);

  for(int t=0;t<T;t++){
    scanf("%lli",&x);
    cout << "Case #" << t+1 << ": " << lasttidy(x) << endl;
  }

  return 0;
}
