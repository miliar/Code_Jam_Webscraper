#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int _=1;_<=T;_++){
		printf("Case #%d: ",_);
		int n, k;
		cin >> n >> k;
		int lvl = 1;
		while(n){
			if(k > lvl){
				n -= lvl;
				k -= lvl;
				lvl *= 2;
			}
			else{
				int t = n / lvl;
				if(k <= n % lvl)
					t++;
				// cout << " !! " << t << " !!";
				if(t & 1)
					cout << t/2 << " " << t/2 << endl;
				else
					cout << t/2 << " " << t/2 - 1 << endl;
				break;
			}
		}
	}
	return 0;
}