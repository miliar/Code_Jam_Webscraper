#include <iostream>
#include <vector>

using namespace std;

int digits[19];

void readigits(unsigned long long N){
	int i;
	unsigned long long div = 10E17;
	for(i=0; i<19; i++){
		digits[i] = N/div;
		N -= digits[i]*div;
		div /= 10;
	}
}

int checkDigits(){
	int i, j;
	for(i=0; i<(19-1); i++){
		if(digits[i]>digits[i+1]){
			digits[i]--;
			for(j=i+1; j<19; digits[j++]=9);
			return 0;
		}
	}
	return 1;
}

int main(int argc, char** argv){
	int T;
	int i;
	unsigned long long N;

	cin >> T;

	i=1;
	while(T--){
		int j=0;
		cin >> N;
		readigits(N);
		while(!checkDigits());
		cout <<"Case #" << i << ": ";
		for(; j<19 && digits[j]==0; j++);
		for(; j<19; j++)
			cout << digits[j];

		cout << endl;
		i++;
	}
}