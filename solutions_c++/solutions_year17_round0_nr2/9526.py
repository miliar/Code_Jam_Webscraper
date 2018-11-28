#include<iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		long long z;
		cin >> z;
		bool l = false;
		while (1) {
			long long nn = z;
			int amari = 10;
			while(1) {
				if (nn % 10 > amari)break;
				if (amari == 0)break;
				amari = nn % 10;
				nn = nn / 10;
				if (nn == 0) { cout <<"Case #"<<i+1<<": "<< z << endl; l = true; break; }
			}
			z-=1;
			if (l == true) {
				break;
			}
		}
	}
    return 0;
}

