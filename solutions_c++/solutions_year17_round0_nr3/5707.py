#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
  
  int T; cin >> T;  
  for(int i=0; i<T; ++i){

    int n, k; cin>>n; cin>>k;
    vector<int> v1(n), v2(n), p(n, 0);    
    for(int r=0; r<k; ++r){

      for(int m=0; m<n; ++m){
	int le=0, re=0;
	for(int j=m-1; j>=0; j--)if(p[j]==0)le++;else break;
	for(int j=m+1; j<n; j++)if(p[j]==0)re++;else break;
	v1[m]=max(le, re);
	v2[m]=min(le, re);
      }

      int t=-1;
      for(int j=0; j<n; ++j){
	if(p[j]==0 && t==-1){
	  t=j;
	}else if(p[j]==0 && (v2[t]<v2[j] || v2[t]==v2[j]&&v1[t]<v1[j])){
	  t=j;
	}
      }
      p[t]=1;

      if(r==k-1){
	int a1=v1[t], a2=v2[t];
	cout << "Case #" << i+1 << ": " << a1 << " " << a2 << endl;
      }
      
    }//K
  }//T
  
  return 0;
}

