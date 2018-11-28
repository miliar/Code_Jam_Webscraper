#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <numeric>
#include <queue>
#include <map> 
#include <set>
#include <string>
using namespace std;
const int INF = 1e+8;

bool check(long long num){
	std::string s;
	s = std::to_string(num);
	int mae = -1;
	for (size_t i=0; i < s.size(); i++){
		if (s[i] < mae) return false;
		mae = s[i];
	}
	return true;
}

int main(){
	long long N;
	int num;
	cin >> num;
	for (int j = 0; j < num; j++){
		cin >> N;
		for (int i = N; i >0; i--){
			if (check(i)) { 
				cout << "Case #"<<j+1<<": "<< i << "\n";
				break;
			}
		}
	}

	return 0;
}