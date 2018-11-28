#include <iostream>
#include <cstdio>
#define ull unsigned long long 
using namespace std;
bool hasfound = false;
bool checkinc(unsigned long long num){
	int curnum = 9;
	while(num){
		if(num%10 <= curnum) curnum = num%10;
		else return false;
		num /= 10;
	}
	return true;
}

void getans(ull num, int length){
	ull temp = num;
	int arr[20];
	for(int i = length -1; i >=0 ; i--){
		arr[i] = temp%10;
		temp /= 10;
	}

	for(int k = 0 ; k  <length; k++){
		for(int i = 0 ; i  < length - 1; i++){
			if(arr[i] <= arr[i+1]) continue;
			else{
				arr[i]--;
				for(int j = i+1; j < length; j++){
					arr[j] = 9;
				}
				break;
			}
		}
	}
	int i = 0 ; 
	if(arr[i] == 0) i++;
	for(; i < length; i++){
		cout << arr[i];
	}
	cout <<endl;
}



int main(){
	int t; cin >> t;
	int t1 = t;
	while(t--){
		unsigned long long num;
		cin >> num;
		if(checkinc(num) == true){
			cout << "Case #"<< t1 - t << ": "<< num << endl;
			continue;
		}
		int len_num = 0;
		ull temp = num;
		while(temp){
			len_num++;
			temp /= 10;
		}
		ull ans = 0;
		for(int i = 0; i < len_num; ++i){
			ans = ans*10 + 1;
		}
		if(ans > num){
			ans = ans - ans/10 - 1;
			cout << "Case #"<< t1 - t << ": "<< ans << endl;
			continue;
		}
		cout << "Case #"<< t1 - t << ": "; 
		getans(num, len_num);
	}

}