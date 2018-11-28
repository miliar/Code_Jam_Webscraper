#include <iostream>
#include <cmath>
using namespace std;



bool check_tidy(long long n){
	long long check = 0;
	long long former = n % 10;
	while (true){
		check = n % 10;
		if (check > former) return false;
		if (n == 0) return true;
		former = check;
		n = n/10;
	}
}

int check_highest(long long n){
	int rsf = 0;
	int pos = 0;
	long long check = 0;
	long long former = n % 10;
	while (true){
		if (n == 0) break;
		check = n % 10;
		if (check > former) {
			if (pos > rsf)
				rsf = pos;
		}
		pos ++;
		former = check;
		n = n/10;
	}
	return rsf;
}

long long tidy(long long num){
	if (check_tidy(num)) return num;
	else{
		while (!check_tidy(num)){
			int high = check_highest(num);
			long long high_ten = (long long) pow(10,high);
			num = num / high_ten;
			num--;
			num = num * high_ten;
			for (int i = 0; i<high;i++){
				long long temp = (long long) pow(10,i);
				num = num + (9*temp);
			}
		}
		return num;
	}
}



int main(int argc, char const *argv[]){

	
	int t;
	long long m;
	cin >> t;
	for (int i =0;i<t;i++){
		cin >> m;
		cout <<"Case #" << i+1 << ": " << tidy(m);
		cout << endl;
	}
	return 0;
}