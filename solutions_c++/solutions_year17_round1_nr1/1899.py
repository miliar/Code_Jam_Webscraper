#include<bits/stdc++.h>
using namespace std;
char cake[26][26];

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;i++){
		int R,C;
		cin >> R >> C;
		for(int j = 0;j<R;j++){
			cin >> cake[j];	
		}
		
		for(int j = 0;j<R;j++){
			int flag = 1;
			if(cake[j][0] != '?') flag = 0;
			for(int k = 1;k<C;k++){
				if(cake[j][k] == '?'){
					cake[j][k] = cake[j][k-1];
				}
				else flag = 0;
			}
			for(int k = C-2;k>=0;k--){
				if(cake[j][k] == '?'){
					cake[j][k] = cake[j][k+1];
				}
			}
		
			if(flag && j>0){
				for(int k = 0;k<C;k++){
					if(cake[j][k] == '?'){
						cake[j][k] = cake[j-1][k];
					}
				
				}
			}
		}
		for(int j = R-2;j>=0;j--){
			
			
				for(int k = 0;k<C;k++){
					if(cake[j][k] == '?'){
						cake[j][k] = cake[j+1][k];
					}
				
				}
			
		}
		cout << "Case #"<<i<<":"<<endl;
		for(int j = 0;j<R;j++){
			cout << cake[j]<< endl;
		}
	}
}
