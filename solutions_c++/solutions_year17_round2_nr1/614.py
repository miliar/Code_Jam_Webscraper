#include <iostream>
#include <iomanip>

using namespace std;

int k,s,n,nt,d;
double ti=0;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> nt;
	for (int _=1;_<=nt;_++)
	{
		cin >> d >> n;
		ti=0;
		for (int i=1;i<=n;i++)
		{
			cin >> k >> s;
			ti=max(ti,(double)(d-k)/double(s));
		}
		cout << setprecision(9);
		cout << fixed;
		cout << "Case #" << _<< ": " << (double)d/ti << "\n";
	}
}