#include <fstream>

using namespace std;

bool isTidy(int n){
	int prev = n % 10;
	n = n / 10;
	if (n == 0){
		return true;
	}
	else{
		bool ok = true;
		while (n > 0){
			int c = n % 10;
			n = n / 10;
			if (c <= prev){
				prev = c;
			}
			else{
				ok = false;
			}
		}
		return ok;
	}
}

int main(){
	ifstream infile("B-small-attempt0.in");
	ofstream outfile("B-small-attempt0.out");
	int cases;
	infile >> cases;
	for (int t = 0; t < cases; t++){
		int N;
		infile >> N;
		int number = 0;
		for (int i = N; i >= 0; i--){
			if (isTidy(i) == true){
				number = i;
				break;
			}
		}
		outfile << "Case #" << t+1<< ": " << number << endl;
	}
	return 0;
}