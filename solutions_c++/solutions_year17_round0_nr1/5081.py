#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <cassert>
#include <string>
#include <bitset>

using namespace std;

void testCase(){
	string S;
    cin >> S;
    int K;
    cin >> K;

	int ans = 0;
	int L = S.size();
    vector<bool> cakes;
	cakes.reserve(L);
	for(char c: S){
		cakes.push_back(c == '+');
	}
	for(int i = 0; i < L; i++){
		if(!cakes[i]){
			ans ++;
			int j = i+1;
			int flip = i+K;
			if(flip > L){
				cout << "IMPOSSIBLE";
				return;
			}
			for(;j < flip; j++){
				cakes[j] = !cakes[j];
			}
		}
	}
	cout << ans;
}

int main(void){
    int N;
    cin >> N;
    for(int i = 1; i <= N; i++){
        cout << "Case #" << i << ": ";
        testCase();
        cout << endl;
    }
    return 0;
}
