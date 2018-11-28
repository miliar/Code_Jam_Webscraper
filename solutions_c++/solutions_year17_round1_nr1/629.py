#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<map>


using namespace std;

int main(){
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    int R, C; cin>>R>>C;
    vector<string> v(R,"");
    for (int i=0; i<R; ++i)
      cin>>v[i];
    for (int i=0; i<R; ++i)
      for (int j=0; j<C; ++j){
	if (v[i][j]!='?'){
	  for (int k=j-1; k>-1; --k){
	    if (v[i][k]=='?')
	      v[i][k]=v[i][j];
	    else
	      break;
	  }
	  for (int k=j+1; k<C; ++k){
	    if (v[i][k]=='?')
	      v[i][k]=v[i][j];
	    else
	      break;
	  }
	}
      }
    for (int i=0; i<R; ++i){
      for (int j=0; j<C; ++j){
	if (v[i][j]!='?'){
	  for (int k=i-1; k>-1; --k){
	    if (v[k][j]=='?')
	      v[k][j]=v[i][j];
	    else
	      break;
	  }
	  for (int k=i+1; k<R; ++k){
	    if (v[k][j]=='?')
	      v[k][j]=v[i][j];
	    else
	      break;
	  }
	}
      }
    }
    cout<<"Case #"<<tc<<":\n";
    for (int i=0; i<R; ++i)
      cout<<v[i]<<endl;


  }
  return 0;
}
