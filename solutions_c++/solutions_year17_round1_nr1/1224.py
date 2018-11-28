#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int r,c, i,j,k;
		char cake[25][25];
		char now=0;
		cin>>r>>c;
		for(i=0;i<r;i++){
			scanf("%s", cake[i]);
		}
		for(i=0;i<r;i++){
			now='?';
			for(j=0;j<c;j++){
				if(cake[i][j]!='?'){
					now=cake[i][j];
					break;
				}
			}
			if(now!='?'){
				for(j=0;j<c;j++){
					if(cake[i][j]=='?'){
						cake[i][j]=now;
					}
					else now=cake[i][j];
				}
			}
		}
		for(i=0;i<r;i++){
			if(cake[i][0]!='?') break;
		}
		k=i;
		for(i=0;i<k;i++){
			for(j=0;j<c;j++){
				cake[i][j]=cake[k][j];
			}
		}
		for(i=k+1;i<r;i++){
			if(cake[i][0]=='?'){
				for(j=0;j<c;j++){
					cake[i][j]=cake[i-1][j];
				}
			}
		}
		cout<<"Case #"<<t<<":"<<endl;
		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				cout<<cake[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}
