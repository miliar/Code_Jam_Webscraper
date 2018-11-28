#include <iostream>

using namespace std;

typedef pair<long long, long long> d;

d cal(long long k, long long num) {
	if (k == 1) {
		return make_pair((num)/2, (num-1)/2);
	} 
	else {
		if (num % 2 == 1)
			return cal((k)/2, (num-1)/2);
		else if (k % 2 == 1)
			return cal(k/2, (num-1)/2);
		else
			return cal(k/2, num/2);
	}
}


int main(){
	int test;
	cin >> test;
	int c=1;
	while(test--)
	{
		long long k, num;
		cin >> num >> k;
		cout << "Case #" << c++ <<": ";
		d res = cal(k, num);
		cout << res.first << " " << res.second << endl;
	}
	return 0;
}
