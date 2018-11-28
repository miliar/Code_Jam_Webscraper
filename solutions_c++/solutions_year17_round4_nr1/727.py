#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
#include<queue>
#include<iomanip>
#include<map>
#include<cmath>



using namespace std;

typedef long long ll;
typedef long double ld;

typedef vector<int> vi;
typedef vector<vi> wi;



int main(){
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    cout<<"Case #"<<tc<<": ";
    int N, P; cin>>N>>P;
    vi v(P,0);
    int a;
    for (int i=0; i<N; ++i){
      cin>>a;
      v[a%P]+=1;
    }
    if (P==2){
      cout<<v[0]+(v[1]+1)/2<<endl;
      continue;
    }
    if (P==3){
      a=min(v[1],v[2]);
      int b=max(v[1],v[2])-a;
      int ans=v[0]+a;
      if (b)
	ans+=(b-1)/3+1;
      cout<<ans<<endl;
      continue;
    }
    if (P==4){
      a=min(v[1],v[3]);
      int b=max(v[1],v[3])-a;
      int c=v[2]%2;
      int ans=v[0]+v[2]/2;
      if (2*c+a)
	ans+=(2*c+a-1)/4+1;
      cout<<ans<<endl;
    }





  }
  return 0;
}








