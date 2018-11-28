#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[]){
	int N;
	cin >> N;
	for(int i = 1; i <= N; i++){
		string s;
		int K;
		cin >> s >> K;
		int L = s.size(), counting = 0, cur = 0;
		bool X = true;
		vector<int> flipping;
		for(int j = 0; j <= L - K; j++){
			int ind = 0;
			if(s[j] == '-') ind = 1;
			if((ind + counting)%2 != 0){ //need fliping
				flipping.push_back(j);
				counting++;
			}
			if(counting > 0 && flipping[cur] == j - K + 1){
				counting--;
				cur++;
			}
		}
		for(int j = L - K + 1; j <= L - 1; j++){
			int ind = 0;
			if(s[j] == '-') ind = 1;
			if((ind + counting)%2 != 0){ //need fliping
				X = false;
			}
			if(counting > 0 && flipping[cur] == j - K + 1){
				counting--;
				cur++;
			}
		}
		if(X){cout << "Case #" << i << ": " << flipping.size() << endl;}
		else{
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}