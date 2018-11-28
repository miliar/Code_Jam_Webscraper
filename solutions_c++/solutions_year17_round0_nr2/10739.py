#include <iostream>

using namespace std;

int main() 
{
	int n;

	int temp = 10; int prev = 10; bool mis; int a; bool found = false;
	int Test;
	cin >> Test;
	for (int i = 1; i <= Test; ++i) {
		cin >> n; found = false;
		while (n >= 0 && !found)
		{
			a = n;
			mis = true;
			prev = 10;
			while (a > 0 && mis)
			{
				temp = a % 10;
				mis = (prev >= temp);
				a = a / 10;
				prev = temp;
			}
			found = mis;
			--n;
		}
		cout << "Case #" << i << ": " << (n+1) << endl;
	}
}