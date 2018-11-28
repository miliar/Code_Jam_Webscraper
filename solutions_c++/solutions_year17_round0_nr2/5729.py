#include <bits/stdc++.h>
using namespace std;


int main(){
	#ifndef LOCAL
    ifstream cin("input.in");
    ofstream cout("output.out");
#endif
  int t, r;
  cin>>t;
  r = 0;
  while(t--){
  	r++;
     string z;
     cin>>z;
     for(int i = z.size() - 1;i>=1;i--){
      if(z[i] < z[i-1]){
         z[i-1]--;
         for(int j = i;j<z.size();j++){
            z[j] = 57;
         }
      }
     }
 int pos = 0;
 bool zs = false;
 cout<<"Case #"<<r<<":"<<" ";
   for(int i = 0;i<z.size();i++){
    if(z[i] == '0' && !zs){
     pos++;
    }
    else if(z[i] != 0){
    	zs++;
    }
   } 
  if(pos != 0){
  	string  k = z.substr(pos , z.size());
    cout<<k<<endl;
}
else{
	cout<<z<<endl;
}

}

 

}