#include<bits/stdc++.h>
using namespace std;

string s[50];
int row[50];

int main(){
	freopen("cj.in","r",stdin);
	freopen("cj.out","w",stdout);
	int t;
	cin>>t;
	for(int te=1;te<=t;te++){
		int r,c,flag=0;
		char prevc='0';
		fill(row,row+45,0);
		cin>>r>>c;
		for(int i=0;i<r;i++){
			cin>>s[i];
		}
		for(int i=0;i<r;i++){
			int flag=0;
			for(int j=0;j<c;j++){
				if(s[i][j]=='?' && flag==1){
					s[i][j]=prevc;
				}
				else if(s[i][j]!='?'){
					flag=1;
					prevc=s[i][j];
				}
			}flag=0;prevc='0';
			for(int j=c-1;j>=0;j--){
				if(s[i][j]=='?' && flag==1){
					s[i][j]=prevc;
				}
				else if(s[i][j]!='?'){
					flag=1;
					prevc=s[i][j];
				}
			}
			if(flag==0)
				row[i]=1;
		}
		flag=0;
		for(int i=0;i<r;i++){
			if(row[i] && flag==1){
				for(int j=0;j<c;j++){
					s[i][j]=s[i-1][j];
				}
			}
			else if(row[i]==0){
				flag=1;
			}
		}flag=0;
		for(int i=r-1;i>=0;i--){
			if(row[i] && flag==1){
				for(int j=0;j<c;j++){
					s[i][j]=s[i+1][j];
				}
			}
			else if(row[i]==0){
				flag=1;
			}
		}
		cout<<"Case #"<<te<<":\n";
		for(int i=0;i<r;i++){
			cout<<s[i]<<'\n';
		}
	}
}
