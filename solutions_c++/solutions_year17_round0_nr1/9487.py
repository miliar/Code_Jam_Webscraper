#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  cin >> n;
  for(int k=0;k<n;k++){
    string s;
    int a;
    cin >> s >> a;
    int co=0;
    for(int i=0;i<s.size();i++){
      if(s[i]=='-'){
	if(i+a>=s.size()+1){
	  co=-1;
	  break;
	}
	for(int j=0;j<a;j++){
	  if(s[i+j]=='+')s[i+j]='-';
	  else s[i+j]='+';
	  
	}
	co++;
      }
    }
    cout << "Case #"<<k+1<<": ";
    if(co==-1)cout << "IMPOSSIBLE" << endl;
    else cout << co << endl;
  }
  return 0;
}
