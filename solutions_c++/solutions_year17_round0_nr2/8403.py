#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int place(long int a, int pl){
	return fmod(a, pow(10, pl+1)) / pow(10, pl);
}

long int tidy(long int num){
	int i = 0;
	while (pow(10, i) <= num){
		if (place(num, i) < place(num, i+1)){
			num -= fmod(num, pow(10, i+1)) + 1;
		}
		i++;
	}
	return num;
}

int main(){
	int count;
	cin >> count;
	for (int i = 0; i < count; i++){
		long int num;
		cin >> num;
		long int res = tidy(num);
		cout << "Case #" << i + 1 << ": " << res << endl;

	}
	return 0;
}
