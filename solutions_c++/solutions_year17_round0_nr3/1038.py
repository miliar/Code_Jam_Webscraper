#include <iostream>
#include <fstream>
using namespace std;
typedef long long ull;

ull NextPow2(ull N){
  ull ans = ull(1);
  while(ans <= N){
    ans *= ull(2);
  }
  return ans;
}

int main(){
  ifstream is("C.in");
  ofstream os("C.out");
  int T;
  is >> T;
  ull N,k,NPow2,first,second,t1,t2;
  for(int Case = 1; Case <= T; Case++){
    is >> N >> k;
    NPow2 = NextPow2(k);
    t1 = N - k + ull(1);
    if(t1%NPow2==ull(0)){
      t1-=ull(1);
    }
    t2 = N - k + ull(1) - (NPow2/ull(2));
    if(t2<=0){
      second = 0;
    }
    else{
      if(t2%NPow2==ull(0))t2-=ull(1);
      second = (t2/ NPow2) + 1;
    }
    first = t1 / NPow2;
    os << "Case #"<<Case<<": "<<second<<" "<<first<<'\n';
  }
  is.close();
  os.close();
}
