#include<iostream>
#include <fstream>
#include <cstdlib>
#include <stdint.h>

using namespace std;

int main(){
	int n; 
	ifstream fp("B-large.in");
	ofstream outfile;
	outfile.open("B-large.out"); 
	if (fp){
		fp >> n;
		int64_t *a = new int64_t [n];
		for (int i = 0; i < n; i++)
			fp >> a[i];
		for (int i = 0; i < n; i++){
			int64_t num = a[i];
			outfile << "Case #" << i+1 << ": ";
			int b[18] = {0};
			int j = 0;
			while (num){
				b[j++] = num % 10;
				num /= 10;
			}
			for (int k = 0; k < j; ){
				if (b[k] >= b[k+1]) k++;
				else {
					k++;
					b[k]--;
					for (int m = 0; m < k; m++)
						b[m] = 9;
				}
			}
			if (b[j-1]) outfile << b[j-1];
			for (int k = j - 2; k >= 0; k--)
				outfile << b[k];
			if (i < n - 1) outfile << endl;
		}
	}
	return 0;
}
