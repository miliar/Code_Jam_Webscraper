#include <bits/stdc++.h>
using namespace std;
int main(){

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin >> t;
	for(int z=1;z<=t;z++){

		int r,c;
		cin >> r >> c;
		char arr[r][c];
		int i,j,ptr;

		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				cin >> arr[i][j];
			}
		}

		i=0;
		j=0;
		ptr=0;

		for(i=0;i<r;i++){
			ptr=0;
			for(j=0;j<c;j++){
				if(arr[i][j]=='?')
					continue;
				else{
					while(ptr<j){
						arr[i][ptr] = arr[i][j]; 
						ptr++;
					}
					ptr++;
				}
			}
			while(ptr<j && ptr!=0){
				arr[i][ptr] = arr[i][ptr-1];
				ptr++;
			}
		}

		for(i=0;i<c;i++){
			ptr=0;
			for(j=0;j<r;j++){
				if(arr[j][i]=='?')
					continue;
				else{
					while(ptr<j){
						arr[ptr][i] = arr[j][i]; 
						ptr++;
					}
					ptr++;
				}
			}
			while(ptr<j && ptr!=0){
				arr[ptr][i] = arr[ptr-1][i];
				ptr++;
			}
		}

		
		cout << "Case #" << z << ":" << endl;
		for(i=0;i<r;i++){
			for(j=0;j<c;j++){

				cout << arr[i][j];
			}
			cout << endl;
		}

	}
}