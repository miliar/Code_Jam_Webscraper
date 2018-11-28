#include<iostream>
#include<string>

using namespace std;

int main(){
	int T, len, index;
	bool check;
	string N;
	
	cin >> T;
	
	for(int x = 0; x < T; x ++){
		cin >> N;
		len = N.length();
		check = true;
		
		if(len == 1){
			cout << "Case #" << x+1 << ": " << N << endl;
		}else{
			for(int i = 0; i < len-1; i ++){
				if(N[i] > N[i+1]){
					check = false;
					index = i;
					break;
				}
			}
			if(check == false){
				for(int i = index+1; i < len; i ++){
					N[i] = '9';
				}
				N[index] -= 1;
				//cout << "<change> N : " << N << endl;
				for(int i = index; i > 0;i --){
					if(N[i] < N[i-1]){
						N[i] = '9';
						N[i-1] -= 1;
					}else{
						break;
					}
				}
				if(N[0] == '0'){
					cout << "Case #" << x+1 << ": ";	
					for(int i = 1; i < len; i ++){
						cout << N[i];
					}
					cout << endl;
				}
				else
					cout << "Case #" << x+1 << ": " << N << endl;				
			}else{
				cout << "Case #" << x+1 << ": " << N << endl;
			}
		}
	}
	
	
	return 0;
}