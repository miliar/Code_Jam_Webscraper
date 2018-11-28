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
    int N, C, M; cin>>N>>C>>M;
    vi B(C,0);
    vi P(N,0);
    for (int i=0; i<M; ++i){
      int a, b; cin>>a>>b;
      P[a-1]++;
      B[b-1]++;
    }
    int ans=0;
    for (int i=0; i<C; ++i)
      ans=max(ans,B[i]);
    int prom;
    for (ans=ans; ans<1001; ++ans){
      bool ja=1; prom=0; int su=0;
      for (int j=0; ja && j<N; ++j){
	su+=P[j];
	if (su>((j+1)*ans)){
	  ja=0;
	  break;
	}
	if (P[j]>ans)
	  prom+=P[j]-ans;
	
      }
      if (ja)
	break;
    }
    cout<<"Case #"<<tc<<": "<<ans<<" "<<prom<<endl;
    





  }
  return 0;
}








