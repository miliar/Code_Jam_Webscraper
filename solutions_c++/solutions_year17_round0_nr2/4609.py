#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[]) {
	/* code */
	int T;
	cin >> T;

	string N;
	int daCase = 0;
	while( daCase < T){
		
		++daCase;
		cin >> N;
		


		vector<char> num = vector<char>();
		num.push_back(N[0]);
		int L = N.size();
		//for(int i=0; i < L; ++i) num.push(N[i]);
		int i = 1;
		while( i < L && N[i-1] <= N[i]){
		 	num.push_back(N[i]);
		 	++i;
		}



		if(i == L){
			cout << "Case #" << daCase << ": " << N << endl;
		} else {
			cout << "Case #" << daCase << ": ";
			i -= 2;
			int t = 1;
			while(i >= 0 && num[i] == num[i+1] ){
				--i;
				++t;
			}

			++i;
			
			for(int k=0; k < i; ++k){
				cout << num[k];
			}


			char c = num[i] - 1;
			if( c != '0') cout << c;
			

			for(int k=i+1; k < L; ++k){
				cout << "9";
			}

			//cout << "  " << i << " " << t << endl;
			cout << endl;
		}

		
		
	} 
	return 0;
}