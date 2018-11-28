#include <iostream>
#include <string>
using namespace std;

int arr[2000], T;

int check(int x){
	for(int i=0; i<5; i++) arr[i]=0;
	int a = 0;
	while(x>0){
		arr[a] = x%10;
		//cout << arr[a] << "  ";
		x/=10;
		a++;
	} 
	//for(int i=0; i<a; i++) cout << arr[i] << " ";
	for(int i=1; i<a; i++){
		if(arr[i]>arr[i-1]) return 0;
		
	}
	return 1;
}

int main(){
	cin >> T;
	for (int t = 1; t<=T; t++){
		cout << "Case #" << t << ": ";
		int s;
		cin >> s;
		while(1){
			if(check(s)){
				cout << s;
				break;
			}
			else s--;
		}
		
		
		cout << endl;
	}
	
	
}
