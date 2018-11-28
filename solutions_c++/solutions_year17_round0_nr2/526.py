#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream file("B-large.in");
	ofstream out("output2.txt");
	long long int N, n;
	file >> N;
	for(int i=0; i<N; i++) {
		file >> n;
		long long int temp = n;
		long long int num = 0;
		while(temp > 0) {
			num = num*10 + 1;
			temp /= 10;
		}
		temp = num;
		num = 0;
		int k = 0;
		while(temp > 0) {
			for(; k<10; k++) {
				if(k == 9) break;
 				if(num + (k+1)*temp > n) break;
			}
			num += (temp - temp/10)*k;
			//cout << temp << " " << k << " " << n << " " << num << endl;			
			temp /= 10;
		}
		out << "Case #" << i+1 << ": " << num << endl;
	}
}