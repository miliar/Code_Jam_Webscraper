#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <cassert>
#include <string>
#include <bitset>

using namespace std;

unsigned long long testCase(){
	unsigned long long N;
	cin >> N;
	unsigned long long ans = N;
	unsigned long long tenth=10;
	int digit1 = ans%10;
	int digit2;
	while(ans/tenth){
		digit2 = (ans/tenth)%10;
		if(digit2 > digit1){
			ans = (ans / tenth)*tenth - 1;
		}
		digit1 = (ans/tenth)%10;
		tenth *= 10;
	}
	return ans;
}

int main(void){
    int N;
    cin >> N;
    for(int i = 1; i <= N; i++){
        cout << "Case #" << i << ": ";
        cout << testCase();
        cout << endl;
    }
    return 0;
}
