#include <bits/stdc++.h>
using namespace std;


int main(){
#ifndef LOCAL
    ifstream cin("input.in");
    ofstream cout("output.out");
#endif
	int t, r;
	r = 0;
	cin>>t;
	while(t--){
		r++;
		string z;
		int k;
		cin>>z>>k;
		int resp = 0 , flag = 0;
		for(int i = 0;i<z.size();i++){
          if(z[i] == '-'){
          	if(i+k-1<z.size()){
          		resp++;
          		for(int j = i;j<=i+k-1;j++){
                  if(z[j] == '-') z[j] = '+';
                  else z[j] = '-';
          		}
          	}
          	else{
          		flag++;
          	}
          }
		}
		cout<<"Case #"<<r<<":"<<" ";
		flag ? cout<<"IMPOSSIBLE"<<endl : cout<<resp<<endl;
	}
}