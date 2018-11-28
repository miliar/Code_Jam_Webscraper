#include <iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i =1;i<=t;i++){
		cout << "Case #" << i << ": \n";
		int r,c;
		cin >> r >> c;
		char arr[r][c];
		for(int j=0;j<r;j++)
			for(int k=0;k<c;k++)
				cin >> arr[j][k];

		for(int j=0;j<r;j++){
			for(int k=0;k<c;k++){
				if(arr[j][k] != '?'){
					for(int l=k+1;l<c;l++){
						if(arr[j][l] == '?')
							arr[j][l] = arr[j][k];
						else
							break;
					}
				}
			}
		}

		for(int j=0;j<r;j++){
			for(int k=c-1;k>=0;k--){
				if(arr[j][k] != '?'){
					for(int l=k-1;l>=0;l--){
						if(arr[j][l] == '?')
							arr[j][l] = arr[j][k];
						else
							break;
					}
				}
			}
		}

		for(int j=0;j<c;j++){
			for(int k=0;k<r;k++){
				if(arr[k][j] != '?'){
					for(int l=k+1;l<r;l++){
						if(arr[l][j] == '?')
							arr[l][j] = arr[k][j];
						else
							break;
					}
				}
			}
		}


		for(int j=0;j<c;j++){
			for(int k=r-1;k>=0;k--){
				if(arr[k][j] != '?'){
					for(int l=k-1;l>=0;l--){
						if(arr[l][j] == '?')
							arr[l][j] = arr[k][j];
						else
							break;
					}
				}
			}
		}

		for(int j=0;j<r;j++){
			for(int k=0;k<c;k++)
				cout << arr[j][k];
			cout << endl;
		}
	}

	return 0;
}