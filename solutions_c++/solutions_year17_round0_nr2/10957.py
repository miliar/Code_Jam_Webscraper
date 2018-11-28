#include <iostream>
//#include <fstream>

using namespace std;

int main(){
	//ifstream fin("inputo.in");
	//ofstream fout("small_output.txt");
	int t;
	cin >> t;
	//cout << t << endl;
	for(int j = 1; j <= t; j++){
		long long x;
		cin >> x;
		//cout << x << endl;
		for(long long i = x; i >= 0; i--){
			long long temp = i, flag = 1;
			if(temp / 10 > 0){
				long long temp0 = temp % 10, temp1;
				temp /= 10;
				temp1 = temp % 10;
				temp /= 10;
				do{
					if(temp0 >= temp1 && temp == 0){
						cout << "Case #" << j << ": " << i << endl;
						flag = 0;
						break;
					} else if(temp0 < temp1){
						break;
					}
					temp0 = temp1;
					temp1 = temp % 10;
					temp /= 10;
				} while (temp >= 0);
			} else {
				cout << "Case #" << j << ": " << i << endl;
				flag = 0;
			}
			if(flag == 0){
				break;
			}
		}
	}
	return 0;
}