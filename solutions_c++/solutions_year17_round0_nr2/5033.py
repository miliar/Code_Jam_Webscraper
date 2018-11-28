#include <iostream>

#define MAX 19

using namespace std;

int t;
string n;

int main()
{
	cin >> t;

	for (int i=1; i<=t; i++)
	{
		cin >> n;
		for (int i=n.length()-2; i>=0; i--)
		{
			if (n[i]>n[i+1])
			{
				for ( ; i>0 && n[i-1]==n[i]; i--);
                n[i]--;
                for (int j=i+1; j<n.length(); j++)
					n[j]='9';
			}
		}
		if (n[0]=='0') n=n.substr(1);
		cout << "Case #" << i << ": " << n << endl;
	}

}
