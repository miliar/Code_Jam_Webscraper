#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<utility>
#include<set>
#include<queue>
#include<list>
#include<stack>

using namespace std;


void getAns(vector<string>& vs, int R, int C){
  for(int i=0; i<R; i++){
    for(int j=0; j<C; j++){
      if(vs[i][j]!='?'){
	bool stop=false;
	for(int j2=j+1; j2<C && !stop; j2++){
	  if(vs[i][j2]=='?')
	    vs[i][j2]=vs[i][j];
	  else
	    stop=true;
	}
	stop=false;
	for(int j2=j-1; j2>=0 && !stop; j2--){
	  if(vs[i][j2]=='?')
	    vs[i][j2]=vs[i][j];
	  else
	    stop=true;
	}
      }
    }
  }
  for(int i=0; i<R; i++){
    for(int j=0; j<C; j++){
      if(vs[i][j]!='?'){
	bool stop=false;
	for(int i2=i+1; i2<R && !stop; i2++){
	  if(vs[i2][j]=='?')
	    vs[i2][j]=vs[i][j];
	  else
	    stop=true;
	}
	stop=false;
	for(int i2=i-1; i2>=0 && !stop; i2--){
	  if(vs[i2][j]=='?')
	    vs[i2][j]=vs[i][j];
	  else
	    stop=true;
	}
      }
    }
  }
  
  cout<<endl;
  for(auto s:vs){
    cout<<s<<endl;
  }
  
    
}


int main(){

  int T;
  cin>>T;  

  for(int i=1; i<=T; i++){
    vector<string> vs;
    int R,C;
    cin>>R>>C;
    for(int i=0; i<R; i++){
      string s;
      cin>>s;
      vs.push_back(s);
    }
        
    
    cout<<"Case #"<<i<<": ";
    getAns(vs,R,C);
    
    
  }

  
  

  return 0;

}
    
