#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int tide_number_small_input(int n){
	int n0, n1, n2, n3;
	while(n){
		n3 = n / 1000;
		n2 = (n - n3 * 1000) / 100;
		n1 = (n - n3 * 1000 - n2 * 100) / 10;
		n0 = n - n3 * 1000 - n2 * 100 - n1 * 10;
		// cout<<n3<<" "<<n2<<" "<<n1<<" "<<n0<<endl;
		if (n3 == 0){

		}
		if (n3 <= n2 && n2 <= n1 && n1 <= n0)
			return n;
		n--;
	}
	return 0;
}

int main(){
	int T;
	int n;
	ifstream infile ("B-small-attempt1.in");
	ofstream outfile ("B-small-attempt1.out");
	infile>>T;
	cout<<T;
	for (int i = 1; i <= T; i++){
		infile>>n;
		outfile<<"Case #"<<i<<": "<<tide_number_small_input(n)<<endl;
	}
	infile.close();
	outfile.close();

	return 0;
}