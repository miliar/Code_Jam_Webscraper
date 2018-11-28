#include<bits/stdc++.h>
using namespace std;
long long t,k,n,a[20],o;
bool check()
{
	for (int i = 0 ; i < o-1; i++)
	{
		if(a[i] > a[i+1])return 0;
	}
	return 1;
}
int main()
{
	ifstream cin("B-large.in");
	ofstream cout("B.out");
	cin >> t;
	for(int i = 1; i<= t; i++)
	{
		cin >> n;
		o = 0;
		a[o] = 0;
		while(n)
		{
			a[o] = n%10;
			n/=10;
			o++;
		}
		reverse(a,a+o);
		while(!check())
		{
			bool u = false;
			for(int j = 0 ; j < o; j++)
			{
				if(u)
				{
					a[j] = 9;
				}else
					if(j+1 < o && a[j] > a[j+1])
					{
						a[j]--; 
						u = true;
					}
			}
		}
		int j = 0;
		while(a[j] == 0) j++;
		cout << "Case #" << i <<": ";
		for (; j < o; j++)
			cout << a[j];
		cout << "\n";
	}
}
