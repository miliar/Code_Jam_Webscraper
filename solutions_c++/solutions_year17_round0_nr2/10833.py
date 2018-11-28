#include <iostream>
#include <string>

#define ll long long

using namespace std;

bool isTidy(unsigned __int64 n) {

	unsigned __int64 t = n % 10;
	n /= 10;
	while (n) {
		if (t < n % 10) {
			return false;
		}
		t = n % 10;n /= 10;
	}
	return true;
}

int main()
{
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small-attempt0.out", "wt", stdout);
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		unsigned __int64 n;
		cin >> n;
		while (isTidy(n)==false)
		{
			n--;
		}
		cout << "Case #" <<i+1<<": "<<n<<endl;
	}
	return 0;
	
}
