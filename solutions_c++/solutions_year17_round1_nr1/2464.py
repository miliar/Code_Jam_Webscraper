#include<iostream>
using namespace std;

int main(){
	
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int r,c;
		cin>>r>>c;
		char a[r][c];
		for(int j=0;j<r;j++){
			for(int k=0;k<c;k++){
				cin>>a[j][k];
			}
		}
		for(int j=0;j<r;j++){
			for(int k=0;k<c;k++){
				char ch='?';
				int p,q;
				if(a[j][k]=='?'){
					for(p=k+1;p<c;p++){
						if(a[j][p]!='?'){
							ch=a[j][p];
							break;
						}
					}
					if(ch!='?'){
						for(q=k;q<p;q++){
							a[j][q]=ch;
						}
						k=q-1;
					}
				}
			}
		}
		for(int j=0;j<r;j++){
			for(int k=c-1;k>=0;k--){
				char ch='?';
				int p,q;
				if(a[j][k]=='?'){
					for(p=k-1;p>=0;p--){
						if(a[j][p]!='?'){
							ch=a[j][p];
							break;
						}
					}
					if(ch!='?'){
						for(q=k;q>p;q--){
							a[j][q]=ch;
						}
						k=q+1;
					}
				}
			}
		}
		for(int k=0;k<c;k++){
			for(int j=0;j<r;j++){
				char ch='?';
				int p,q;
				if(a[j][k]=='?'){
					for(p=j+1;p<r;p++){
						if(a[p][k]!='?'){
							ch=a[p][k];
							break;
						}
					}
					if(ch!='?'){
						for(q=j;q<p;q++){
							a[q][k]=ch;
						}
						j=q-1;
					}
				}
			}
		}
		for(int k=0;k<c;k++){
			for(int j=r-1;j>=0;j--){
				char ch='?';
				int p,q;
				if(a[j][k]=='?'){
					for(p=j-1;p>=0;p--){
						if(a[p][k]!='?'){
							ch=a[p][k];
							break;
						}
					}
					if(ch!='?'){
						for(q=j;q>p;q--){
							a[q][k]=ch;
						}
						j=q+1;
					}
				}
			}
		}
		cout<<"Case #"<<i<<":\n";
		for(int j=0;j<r;j++){
			for(int k=0;k<c;k++){
				cout<<a[j][k];
			}
			cout<<"\n";
		}
	}
	return 0;
}
