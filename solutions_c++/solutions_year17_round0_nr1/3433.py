#include <cstdio>
#include <iostream>
using namespace std;
int main(){
	string s;
	int t, k, flip[1000], tflip, sum_k;
	int p[46];
	bool nope;
	p['+'] = 0;
	p['-'] = 1;
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> s;
		cin >> k;
		sum_k = tflip = 0;
		nope = false;
		for(int j = 0; j < s.size(); j++)
			flip[j] = 0;
		for(int j = 0; j < s.size(); j++){
			if(sum_k%2 == p[s[j]]) flip[j] = 0;
			else {
				flip[j] = 1; tflip++;
				if(j+k > s.size()){
					nope = true;
					break;
				}
			}
			if(j >= k-1)
				sum_k += flip[j]-flip[j-k+1];
			else
				sum_k += flip[j];
		}
		if(nope) printf("Case #%d: IMPOSSIBLE\n",i);
		else printf("Case #%d: %d\n",i,tflip);
	}
}

