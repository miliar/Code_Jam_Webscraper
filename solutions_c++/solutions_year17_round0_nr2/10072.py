#include <iostream>
#include <fstream>
#define MAX(x,y) (x)>(y)?(x):(y)
using namespace std;


int main(){

	int t;
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");

	fin >> t;
	for(int o=1;o<=t;o++){
		
		long long n;
		fin >> n;

		fout << "Case #"<< o << ": ";
		if( n < 10 ){ fout << n << endl; continue; }

		long long mx = 9;
		for(long long z=10;z<=n;z++){

			long long prev = z % 10;
			long long temp = z / 10;
			for(temp; temp > 0 ; temp= temp/10){
				if( prev < temp % 10) break;
				prev = temp%10;
				}
			if( temp == 0) mx = z;
		}
		fout << mx << endl;
	}
	fin.close();
	fout.close();
	return 0;
}