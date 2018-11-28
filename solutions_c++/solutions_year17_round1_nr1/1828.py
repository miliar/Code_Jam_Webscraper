#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int times=0;times<t;times++){
		int r,c;
		cin>>r>>c;
		char cake[26][26];
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin>>cake[i][j];
			}
		}
		
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(cake[i][j]=='?'){
					continue;
				}
				int k=j;
				while(k-1>=0){
					if(cake[i][k-1]=='?'){
						cake[i][k-1]=cake[i][j];
						k--;
					}
					else{
						break;
					}
				}
				k=j;
				while(k+1<c){
					if(cake[i][k+1]=='?'){
						cake[i][k+1]=cake[i][j];
						k++;
					}
					else{
						break;
					}
				}
			}
		}
		
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(cake[i][j]!='?')continue;
				int k=i;
				if(i-1>=0)cake[i][j]=cake[i-1][j];
				else{
					while(k+1<c){
						if(cake[k+1][j]!='?'){
							cake[i][j]=cake[k+1][j];
							break;
						}
						k++;
					}
				}
			}
		}
		
		cout<<"Case #"<<times+1<<":"<<endl;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<cake[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}

