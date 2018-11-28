#include <bits/stdc++.h>
 
using namespace std;
 

 
int main() 
{
	freopen("inputCSmall.txt", "r", stdin);
	freopen("outputCSmall.txt", "a", stdout);
	int tc;
	cin >> tc;
	long n, k;
	for(int i = 1; i <= tc; i++) {
		priority_queue <int> box;
		cin >> n >> k;
		box.push(n);
		printf("Case #%d: ", i);
		while (k > 1) {
			long int x = box.top() - 1;
			box.pop();
			box.push(x / 2); 
			box.push(x - x / 2);
			k--;
		}
		long int x = box.top() - 1;
		printf("%ld %ld\n", (x- x/2), (x/2));
	}
	return 0;
}