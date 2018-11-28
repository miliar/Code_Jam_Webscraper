#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

long int tidy2(long int N)
{
	long int K;
	K=N;
	vector<int> digits;
	int d;

	long tmp=N;

	if(N <= 9) {
		return N;
	}
	else {

		while(tmp>0) {
			d=tmp%10;
			digits.push_back(d);
			tmp/=10;
		}

		// for(int i=0; i<digits.size()-2; ++i) {
			
			int i=0;
			while(i<digits.size()-1) {
				
				if(digits[i]<digits[i+1]) {
					digits[i]=9;
					digits[i+1]--;
		
					i=0;
					if(digits[i+1]==-1) digits[i+1]=9;
				}
				else i++;
			}
		// }

		if(digits[digits.size()-2]<digits[digits.size()-1]){
			digits[digits.size()-2]=9;
			digits[digits.size()-1]--;
			if(digits[digits.size()-1]==0) {
				digits.pop_back();
				for(int i=0; i<digits.size(); ++i) {
					digits[i]=9;
				}
			}
		}

		long int res=0;
		long int mul=1;
		for(int i=0; i<digits.size(); ++i) {
			res+=digits[i]*mul;
			mul=mul*10;
		}
		return res;
	}
}

long int tidy3(long int N)
{
	long int K;
	K=N;
	vector<int> digits;
	int d;
	long int tmp=N;

	while(tmp>0) {
			d=tmp%10;
			digits.push_back(d);
			tmp/=10;
	}
	int i=digits.size()-1;

	while(i>0) {
		if(digits[i]>digits[i-1]) {
			digits[i]--;
			if(digits[i]==0 && i==(digits.size()-1)) 
				digits.pop_back();
			for(int j=i-1; j>=0; j--) {
				digits[j]=9;
			}
		i=digits.size()-1;
		}
		else
			i--;
	}

	long int res=0;
	long int mul=1;
	for(int i=0; i<digits.size(); ++i) {
		res+=digits[i]*mul;
		mul=mul*10;
	}
	return res;

}

int main(int argc, char const *argv[])
{
	long int t, n, K;
	long int N;
	
  	cin >> t;  
  	for (int i = 1; i <= t; ++i) {
    	cin >> N ;  // read n and then m.
  
    	K=tidy3(N);
    	cout << "Case #" << i << ": " << K<< endl;
  	}

	return 0;
}
