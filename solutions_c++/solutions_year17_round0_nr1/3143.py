#include <bits/stdc++.h>

using namespace std;

#define MAXN 1009

string cad;

int main(){
	int TC, K;

	cin>>TC;

	int NC = 1;

	while(TC--){
		cin>>cad>>K;
		int ans = 0;
		for(int i = 0 ; i + K<= cad.size() ;i++){
			if(cad[i] == '-'){
				for(int j = i ; j<i+K ;j++){
					cad[j] = (cad[j] == '-')?'+':'-';	
				}
				ans++;	
			}
		}

		bool tmp = 1;
		
		for(int i = 0 ; i<cad.size() ;i++){
			if(cad[i] == '-'){
				tmp = 0;	
			}	
		}
		
		cout<<"Case #"<<NC++<<": ";
		
		if(tmp){
			cout<<ans<<endl;	
		}else{
			cout<<"IMPOSSIBLE"<<endl;
		}
		
	}

	return 0;	
}
