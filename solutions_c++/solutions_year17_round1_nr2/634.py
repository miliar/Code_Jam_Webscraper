#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<map>


using namespace std;

typedef long double ld;


int main(){
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    int N, P; cin>>N>>P;
    vector<ld> R(N,0);
    for (int i=0; i<N; ++i)
      cin>>R[i];
    vector<vector<ld> > Q(N,vector<ld>(P,0));
    for (int i=0; i<N; ++i)
      for (int j=0; j<P; ++j){
	cin>>Q[i][j];
	Q[i][j]/=R[i];
      }
    vector<int> v(N,0);
    int ans=0;
    bool ja=1;
    while(ja){
      int la=0; int hi=0;
      for (int i=1; i<N; ++i){
	if (Q[i][v[i]]<Q[la][v[la]])
	  la=i;
	if (Q[i][v[i]]>Q[hi][v[hi]])
	  hi=i;	
      }
      if (Q[la][v[la]]*11>=Q[hi][v[hi]]*9){
	++ans;
	for (int i=0; i<N; ++i){
	  v[i]+=1;
	  if (v[i]==P)
	    ja=0;
	}
      }
      else{
	v[la]+=1;
	if (v[la]==P)
	  ja=0;
      }
    }
	    


    cout<<"Case #"<<tc<<": "<<ans<<endl;


  }
  return 0;
}
