#include <iostream>
using namespace std;

string arr[1000];
int main(){
	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++){
		int r,c;
		cin>>r>>c;
		for(int i=0;i<r;i++){
			cin>>arr[i];
		}
		int fl=0;
		for(int j=0;j<c;j++){
			for(int i=0;i<r;i++){
				if(arr[i][j]!='?'){
					fl=1;
					break;
				}
			}
			if(fl==1){
				char ch='?';
				for(int i=0;i<r;i++){
					if(arr[i][j]!='?'){
						ch=arr[i][j];
					}
					else{
						arr[i][j]=ch;
					}
				}
				for(int i=r-1;i>=0;i--){
					if(arr[i][j]!='?'){
						ch=arr[i][j];
					}
					else{
						arr[i][j]=ch;
					}
				}
				for(int k=j+1;k<c;k++){
					fl=0;
					for(int t=0;t<r;t++){
						if(arr[t][k]!='?'){
							fl=1;
							break;
						}
					}
					if(fl==1){
						ch='?';
						for(int i=0;i<r;i++){
							if(arr[i][k]!='?'){
								ch=arr[i][k];
							}
							else{
								arr[i][k]=ch;
							}
						}
						for(int i=r-1;i>=0;i--){
							if(arr[i][k]!='?'){
								ch=arr[i][k];
							}
							else{
								arr[i][k]=ch;
							}
						}
					}
					else{
						for(int i=0;i<r;i++){
							arr[i][k]=arr[i][k-1];
						}
					}
				}
				for(int k=j-1;k>=0;k--){
					fl=0;
					for(int t=0;t<r;t++){
						if(arr[t][k]!='?'){
							fl=1;
							break;
						}
					}
					if(fl==1){
						ch='?';
						for(int i=0;i<r;i++){
							if(arr[i][k]!='?'){
								ch=arr[i][k];
							}
							else{
								arr[i][k]=ch;
							}
						}
						for(int i=r-1;i>=0;i--){
							if(arr[i][k]!='?'){
								ch=arr[i][k];
							}
							else{
								arr[i][k]=ch;
							}
						}
					}
					else{
						for(int i=0;i<r;i++){
							arr[i][k]=arr[i][k+1];
						}
					}
				}
				break;
			}

		}
		cout<<"Case #"<<te<<": \n";
		for(int i=0;i<r;i++){
			cout<<arr[i]<<endl;
		}
	}
	return 0; 
}