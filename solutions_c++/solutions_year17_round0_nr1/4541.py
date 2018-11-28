#include <iostream>

using namespace std;

int flippy(string pan, int k){
	int len = pan.length();
	int cnt = 0;
	for(int i = 0;i < len;i++){

		if(i > len - k && pan[i] == '-') return -1;
		
		if(pan[i] == '-'){
			for(int j = i;j < i + k;j++){
				pan[j] = (pan[j] == '+')?'-':'+';
			}
			cnt++;
		}
	}
	return cnt;
}

int main(){

	int T;
	string pancake;
	int K;

	cin >> T;
	for(int i = 0;i < T;i++){
		cin >> pancake >> K;
		int f = flippy(pancake, K);
		if(f == -1){
			cout <<  "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		}
		else{
			cout << "Case #" << i+1 << ": " << f << endl;
		}
	}
	return 0;
}

