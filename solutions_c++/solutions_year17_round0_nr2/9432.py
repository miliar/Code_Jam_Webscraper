#include <bits/stdc++.h>
using namespace std;
bool tidyness(int inp)
{
	int tmp = 10;
	while (inp)
	{
		if (inp % 10 > tmp)
			return false;
		else
			tmp = inp % 10;
		inp /= 10;
	}
	return true;
}
int main()
{
	int t;
	int tidy[1111] = {0};
	for (int i = 1; i < 1111; i++)
		if (tidyness(i))
			tidy[i] = i;
		else tidy[i] = tidy[i - 1];
	while (cin>>t)
		for (int cnt = 1; cnt <= t; cnt++)
		{
			int n;
			cin>> n;
			cout<<"Case #"<<cnt<<": "<<tidy[n]<<endl;
		}
}
