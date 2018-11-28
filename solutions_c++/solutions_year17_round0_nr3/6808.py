#include <iostream>
#include <queue>
#include <vector>
#include <set>
using namespace std;

typedef long long lol;

int main(void){
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; i += 1){
		lol n = 0;
		cin >> n;
		lol k = 0;
		cin >> k;
		cout << "Case #" << i << ": ";
		priority_queue<lol> U;
		U.push(n);
		for (int u = 0; u < k; u++){
			lol c = U.top();
			U.pop();
			lol d = (c-1)/2;   //right
			lol e = c -1 - d; //left : e >= d
			if (u == k-1){
				cout << e << " " << d;
			}
			U.push(e);
			U.push(d);
		}
		cout << endl;
	}
}

