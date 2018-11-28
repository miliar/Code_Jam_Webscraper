#include<bits/stdc++.h>
using namespace std;

string N;

int main(){
	int C; cin >> C;
	for(int cas = 1; cas <= C; cas++){
		cin >> N;
		//cout << N << endl;

		for(int i=N.size()-1; i>0; i--){
			if (N[i] < N[i-1]){
				for(int j = i; j<N.size(); j++){
					N[j] = '9';
				}
				N[i-1] -=1;
			}
			//cout << N << endl;
		}

		cout << "Case #" << cas << ": ";
		if (N[0] == '0')
			cout << N.substr(1,N.size()-1) << endl;	
		else
			cout << N << endl;
	}

}
