#include <iostream>
#include <fstream>
using namespace std;

bool f(int long long n)
{
	int long long x = n % 10;
	while(n){
		if(n % 10 > x)
			return false;
		x = n % 10;
		n /= 10;
	}
	return true;
}

int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("output.txt");
	int long long n;
	string s;
	int t;
	fin >> t;
	for(int i = 0; i < t; i++){
		fin >> n;
		while(!f(n)) n--;
		fout << "Case #" << i + 1 << ": " << n << "\n";
	}
	fout.close();
}