#include <iostream>
#include <utility>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[]){
	int T = 0;
	cin >> T;
	for(int I = 1; I <= T; I++){
		int N, M;
		cin >> N >> M;
		int state[101], c0 = -1, count = 0, ind = 0;
		for(int i = 1; i <= N; i++) {state[i] = 0;}

		for(int i = 0; i < M; i++){
			char s;
			int r, c;
			cin >> s >> r >> c;
			if(s == 'x'){
				state[c] = 2;
				c0 = c;
			}
			else if(s == 'o'){
				c0 = c;
				state[c] = 1;
			}
			else{
				state[c] = 1;
			}
		}
		if(c0 == -1){
			c0 = 1;
			state[1] = 2;
		}
		for(int i = 1; i <= N; i++){
			if(state[i] == 0){
				count ++;
			}
			else if(state[i] == 2){
				count ++;
			}
		}
		for(int i = 2; i < N; i++){
			count ++;
		}
		if(c0 != N){
			for(int i = 2; i <= N; i++){
				count ++;
			}
		}
		else{
			for(int i = 2; i <= N; i++){
				count ++;
			}
		}
		cout << "Case #" << I << ": " << 3 * N - 2 + (int)(N == 1) << " " << count << endl;
		for(int i = 1; i <= N; i++){
			if(state[i] == 0){
				cout << "+ " << 1 << " " << i << endl;
			}
			else if(state[i] == 2){
				cout << "o " << 1 << " " << i << endl;
			}
		}
		for(int i = 2; i < N; i++){
			cout << "+ " << N << " " << i << endl;
		}
		if(c0 != N){
			for(int i = 2; i <= N; i++){
				cout << "x " << i << " " << i - int(i <= c0) << endl;
			}
		}
		else{
			for(int i = 2; i <= N; i++){
				cout << "x " << i << " " << N + 1 - i << endl;
			}
		}
	
	}
	return 0;
}