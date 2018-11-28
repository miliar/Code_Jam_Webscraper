#include <iostream>
#include <cmath>
#include <bitset>
#include <sstream>
#include <string>
using namespace std;


int solution(int *v,int n,int k){
	int i=0;
	int count=0;
	for(i=0;i<n;i++){
		if(i+k<=n){
			if(v[i]%2==1) count++;
			int j=0;
			for(j=1;j<k;j++){
				if(v[i]%2==1) v[i+j]+=v[i];	
			}
		}else{
			int j;
			for(j=0;j<k-1 && i+j<n ;j++){ //&& i+j<n
					if(v[i+j]%2==1){
						return -1;
					}
			}
		}
		/*
		for(int l=0;l<n;l++){
			cout<<v[l];
		}
		cout<<endl;
		*/
	}
	return count;
	
}


int main(){
	int t, k;
	string s;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> s >> k;  
    int *v=new int[s.size()]();
    int j=0;
	for(j=0;j<s.size();j++){
		if(s[j]=='+') {
			v[j]=0;
		}else{
			v[j]=1;
		}
	}
	int res=solution(v,s.size(),k);
	if(res==-1) {
		cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
	}else{
		cout << "Case #" << i << ": " << res << endl;
	}
  }
	return 0;
}
