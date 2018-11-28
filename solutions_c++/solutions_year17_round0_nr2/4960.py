#include <iostream>
#include <cstdio>
#include <sstream>
#include <string>
using namespace std;

int main(){
	freopen("output.txt", "w", stdout);
	freopen("input.in", "r", stdin);
	long long n;
	int t;
	scanf("%d", &t);
	stringstream ss;
	int c = 1;
	while (t--){
		scanf("%lld", &n);
		ss.clear();
		ss.str("");
		ss << n;
		string value = ss.str();
		int len = value.size();
		if (2 <= len){
			for (int i = 0; i < len-1 && i >= 0; i++){
				if (value[i]>value[i + 1]){
					value[i]--;
					for (int j = i + 1; j < len; j++){
						value[j] = '9';
					}
					len = i+1;
					i = i - 2;
				}
			}
		}
		ss.clear();
		ss.str(value);
		ss >> n;
		printf("Case #%d: %lld\n",c++,n);
	}
	return 0;
}