#include <iostream>

using namespace std;

int solve(char ** arr, int R, int C){
	int k;
	for (int j=0; j < R ;j++){
		for (int i=0;i<C;i++){
			if (arr[j][i] != '?'){
				k = i+1;
				while (k < C && arr[j][k] == '?'){
					arr[j][k] = arr[j][i];
				}
			
			}
		
		
		}
		for (int i=C-1;i>=0;i--){
			if (arr[j][i] != '?'){
				k=i-1;
				while (k >=0 && arr[j][k] == '?'){
					arr[j][k] = arr[j][i];
				}
			
			}
		
		
		}
	
	
	} 
	for (int i=0; i < C ;i++){
		for (int j=0;j<R;j++){
			if (arr[j][i] != '?'){
				k = j+1;
				while (k < R && arr[k][i] == '?'){
					arr[k][i] = arr[j][i];
				}
			
			}
		
		
		}
		for (int j=R-1;j>=0;j--){
			if (arr[j][i] != '?'){
				k=j-1;
				while (k >=0 && arr[k][i] == '?'){
					arr[k][i] = arr[j][i];
				}
			
			}
		
		
		}
	
	
	} 

	return -1;
}



int main (){
	int	test;
	int cur;
	int c2;
//	cin.unsetf(ios_base::skipws);
	cin >> test;
	char ** arr;
	for (int i =1;i<=test;i++){
		cin >>cur;
		cin >> c2;
		arr = new char*[cur];
		for (int l =0; l < cur;l++){
			arr[l] = new char[c2];
			for (int k =0; k < c2;k++){
				arr[l][k] = ' ';
				while (arr[l][k] != '?' &&  !(arr[l][k] >= 'A' && arr[l][k] <= 'Z'))
				{cin.get(arr[l][k]);}
			}
		}

		solve(arr, cur, c2);
		if (cur <0){
		cout << "Case #"<<i<<":"<< " "<<"IMPOSSIBLE"<<endl;
		}else{
		cout << "Case #"<<i<<":"<<endl;
		for (int l =0; l < cur;l++){
			for (int k =0; k < c2;k++){
				cout << arr[l][k];
			}
			cout <<endl;
			delete [] arr[l];
		}
		delete [] arr;
		
		}
	};

}
