#include <iostream>
using namespace std;


int main(){
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++){
		string inp;
		cin >> inp;
		int i = 0;
		while (i<inp.length()-1 && inp[i] <= inp[i+1])
			i++;
		if (i<inp.length()-1){
			inp[i]--;
			for (int j=i+1;j<inp.length();j++)
				inp[j]='9';
			while (i > 0 && inp[i-1] > inp[i]){
				inp[i] = '9';
				inp[i-1] --;
				i--;
			}
				
		}
		i=0;
		while(i<inp.length() && inp[i] == '0')
			i++;
		cout << "Case #" << test << ": ";
		for (;i<inp.length();i++)
			cout << inp[i];
		cout << endl;
		
	}
	
	
	return 0;
}