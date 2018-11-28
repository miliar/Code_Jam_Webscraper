#include <iostream>
using namespace std;
char a[30][30];
int r,c;

bool check(){
	for(int i=0;i<r;i++) for(int j=0;j<c;j++) if(a[i][j]=='?') return true;
	return false;
	}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		
		cin>>r>>c;
		
		for(int i=0;i<r;i++) for(int j=0;j<c;j++) cin>>a[i][j];
		while(check()){

			for(int i=0;i<r;i++){
				for(int j=0;j<c;j++){
					char ch;
					if(a[i][j]>='A'&&a[i][j]<='Z'){
						ch=a[i][j];
						int n=j-1,m=j+1;
						while(a[i][n]=='?'&&n>=0) a[i][n]=ch,--n;
						while(a[i][m]=='?'&&m<c) a[i][m]=ch,++m;
						}
					}
				}

			for(int i=0;i<c;i++){
				for(int j=0;j<r;j++){
					char ch;
					if(a[j][i]>='A'&&a[j][i]<='Z'){
						ch=a[j][i];
						int n=j-1,m=j+1;
						while(a[n][i]=='?'&&n>=0) a[n][i]=ch,--n;
						while(a[m][i]=='?'&&m<r) a[m][i]=ch,++m;
						}
					}
				}
		/*
		for(int i=0;i<r;i++){
			
			for(int j=0;j<c;j++){
				if(a[i][j]>='A'&&a[i][j]<='Z'){
					char ch=a[i][j];
					int k=j+1;
					while(a[i][k]=='?'&&k<c) a[i][k]=ch,++k;
					}
				}
			}
			for(int i=r;i>=0;i--){
			
			for(int j=c;j>=0;j--){
				if(a[j][i]>='A'&&a[j][i]<='Z'){
					char ch=a[j][i];
					int k=j-1;
					while(a[k][j]=='?'&&k>=0) a[k][j]=ch,--k;
					}
				}
			}
			for(int i=0;i<c;i++){
			for(int j=0;j<r;j++){
				if(a[j][i]>='A'&&a[j][i]<='Z'){
					char ch=a[j][i];
					int k=j+1;
					while(a[k][j]=='?'&&k<r) a[k][j]=ch,++k;
					}
				}
			}
		
		for(int i=c;i>=0;i--){
			for(int j=r;j>=0;j--){
				if(a[j][i]>='A'&&a[j][i]<='Z'){
					char ch=a[j][i];
					int k=j-1;
					while(a[k][j]=='?'&&k>=0) a[k][j]=ch,--k;
					}
				}
			}
		*/

		
		}
		cout<<"Case #"<<t<<": "<<endl;
		for(int i=0;i<r;i++){ for(int j=0;j<c;j++){
			cout<<a[i][j];
			}cout<<endl;
		}
		}
	return 0;
	}
