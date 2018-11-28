#include <bits/stdc++.h>
using namespace std;

int main(){
	int t,r,c;
	cin>>t;
	for(int cases=1;cases<=t;cases++){
		cin>>r>>c;
		char A[r+1][c+1];
		for(int i=0;i<r;i++){
			scanf("%s",A[i]);
		}
		char C[r][c];
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				C[i][j] = A[i][j];	
			}
		}
		for(int j=0;j<c;j++){
			for(int i=0;i<r;i++){
				if(A[i][j]=='?'){
					bool a = false;
					for(int k=i-1;k>=0;k--){
						if(A[k][j]!='?' && a==false){
							a = true;
							A[i][j] = A[k][j];
						}
					}
					if(!a){
						for(int k=i+1;k<r;k++){
							if(A[k][j]!='?' && a==false){
								a = true;
								A[i][j] = A[k][j];
							}
						}
					}
					int sz = 0;
					for(int z=0;z<r;z++){
						sz++;
					}
				}
			}
		}

		for(int j=0;j<c;j++){
			bool d = false;
			for(int i=0;i<r;i++){
				if(A[i][j]=='?' && d==false){
					d = true;
				}
			}
			if(d){
				bool b = false;
				for(int k=j-1;k>=0;k--){
					if(A[0][k]!='?' && b==false){
						b = true;
						for(int y=0;y<r;y++){
							A[y][j] = A[y][k];
						}
					}
				}
				if(!b){
					for(int k=j+1;k<c;k++){
						if(A[0][k]!='?' && b==false){
							b = true;
							for(int y=0;y<r;y++){
								A[y][j] = A[y][k];
							}
						}
					}
				}
			}
		}

		cout<<"Case #"<<cases<<":\n";
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<A[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}