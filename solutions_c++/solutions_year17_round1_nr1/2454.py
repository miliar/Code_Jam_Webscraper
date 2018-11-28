#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int r,c;
bool valid(int i,int j){
	return (i>=0 && j>=0 && i<r && j<c);
}
int main(){
	int t;
	//freopen("A-small-attempt2.in","r",stdin);
	//freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>t;
	for(int tc=1;tc<=t;tc++){
		cin>>r>>c;
		char a[r][c];
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin>>a[i][j];
			}
		}
		for(int i=0;i<c;i++){
			for(int j=0;j<r-1;j++){
				if(a[j][i]!='?') if(a[j+1][i]=='?') a[j+1][i]=a[j][i];
			}
		}
		for(int i=0;i<c;i++){
			for(int j=r-1;j>=1;j--){
				if(a[j][i]!='?') if(a[j-1][i]=='?') a[j-1][i]=a[j][i];
			}
		}
		for(int i=0;i<r;i++){
			for(int j=0;j<c-1;j++){
				if(a[i][j]!='?') if(a[i][j+1]=='?') a[i][j+1]=a[i][j];
			}
		}
		for(int i=0;i<r;i++){
			for(int j=c-1;j>=1;j--){
				if(a[i][j]!='?') if(a[i][j-1]=='?') a[i][j-1]=a[i][j];
			}
		}
		cout<<"Case #"<<tc<<":"<<endl;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<a[i][j];
			}
			cout<<endl;
		}
	}
}
