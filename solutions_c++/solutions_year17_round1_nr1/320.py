#include <iostream>

using namespace std;

int T,R,C;
char cake[26][26];

int main(){
	cin>>T;
	
	for(int cn=1;cn<=T;cn++){
		cin>>R>>C;
		
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				cin>>cake[i][j];
				if(j>0 && cake[i][j]=='?')
					cake[i][j]=cake[i][j-1];
			}
		}
		for(int i=0;i<R;i++){
			int j=0;
			while(j<C && cake[i][j]=='?')
				j++;
			if(j<C){
				for(int k=j-1;k>=0;k--){
					cake[i][k]=cake[i][j];
				}
			}
		}
		for(int i=1;i<R;i++){
			if(cake[i][0]!='?')
				continue;
			for(int j=0;j<C;j++){
				cake[i][j]=cake[i-1][j];
			}
		}
		for(int i=R-2;i>=0;i--){
			if(cake[i][0]!='?')
				continue;
			for(int j=0;j<C;j++){
				cake[i][j]=cake[i+1][j];
			}
		}		
		cout<<"Case #"<<cn<<":"<<'\n';
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++)
				cout<<cake[i][j];
			cout<<'\n';
		}

	}
	
	return 0;
}