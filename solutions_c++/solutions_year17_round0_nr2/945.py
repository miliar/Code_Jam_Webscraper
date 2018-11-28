#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	cin>>T;
	for (int t = 1; t <= T; t++)
	{
		string a;
		cin>>a;
		for (int i = (int)a.size()-2; i >= 0; i--)
			if (a[i] > a[i+1])
			{
				a[i]--;
				for (int j = i+1; j < a.size(); j++)
					a[j] = '9';
			}
		if (a[0] == '0')
			a = a.substr(1);
		cout<<"Case #"<<t<<": "<<a<<endl;	
	}
	return 0;
}