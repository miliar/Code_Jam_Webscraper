#include<iostream>
#include<fstream>

using namespace std;

int main() {
	int t;
	ifstream fin;
	ofstream fout;
	fin.open("Blarge.in",ios::in);
	fout.open("tidynum1.txt",ios::out);
	fin>>t;
	for(int i=0; i<t; i++) {
		unsigned long long N, temp, multiplier = 1;
		int d, d1;
		fin>>N;
		temp = N;
		d = temp%10;
		while(temp > 0) {
        	multiplier*=10;
        	temp = N/multiplier;
			d1 = temp%10;
			if(d1 > d){
                  N = N - (N%multiplier) - 1;
            }
			d = (N/multiplier)%10;
		}
		fout<<"Case #"<<i+1<<": "<<N<<endl;
	}
	fin.close();
	fout.close();
	system("pause");
	return 0;
}
