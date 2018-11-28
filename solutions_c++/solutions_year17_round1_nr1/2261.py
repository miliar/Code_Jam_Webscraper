#include<iostream>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int k=1;k<=t;k++){
		int r,c;
		cin>>r>>c;
		char arr[25][26];
		for(int i =0;i<r;i++){
			for(int j=0;j<c;j++)
				cin>>arr[i][j];
		}
	/*	for(int i =0;i<r;i++){
			for(int j=0;j<c;j++)
				cout<<arr[i][j];
		}*/
		int i,j;
		for(i = 0;i<r;i++){
			for(j=0;j<c;j++){
				while(arr[i][j]=='?'){
					j++;
				}
				if(j<c){
					int k = j+1;
					while(arr[i][k] == '?'&&k<c){
						arr[i][k] = arr[i][j];
						k++;
					}
					k = j-1;
					while(arr[i][k] == '?'&&k>=0){
						arr[i][k] = arr[i][j];
						k--;
					}
				}
			}
		}
		for(int i = 0;i<r;i++){
			if(arr[i][0]=='?'){
				if(i!=0){
					for(int j = 0;j<c;j++){
						arr[i][j] = arr[i-1][j];
					}				
				}
				else{
					int k = i+1;
					while(arr[k][0]=='?'){
						k++;
					}
					for(int j = 0;j<c;j++){
						arr[i][j] = arr[k][j];
					}
				}
			}
		}
		cout<<"case #"<<k<<": \n";
		for(int i =0;i<r;i++){
			for(int j=0;j<c;j++)
				cout<<arr[i][j];
			cout<<endl;
		}
	}
}
