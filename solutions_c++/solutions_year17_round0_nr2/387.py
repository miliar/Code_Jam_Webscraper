#include<iostream>
#include<string>
using namespace std;

bool check(long long int n)
{
	string find = to_string(n);
	int length = find.length();
	for (int indx = 1; indx < length; indx++)
	{
		int first = find.at(indx);
		int last = find.at(indx - 1);
		if (first < last)
		{
			return false;
		}
	}
	return true;
}

long long int findLastTidy(long long int n)
{
	long long int lastTidy = n;
	while (!check(n))
	{
		n--;
		lastTidy = n;
	}
	return lastTidy;
}



int main()
{
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
			long long int n;
			cin >> n;
			cout << "Case " << "#" << tc << ":" << " ";
			n = findLastTidy(n);
			cout << n << endl;
	}
	return 0;
}