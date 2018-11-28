#include <iostream>
#include <string>
#include<vector>
using namespace std;

bool tidy(vector <int> l);
void split(long long int num, vector <int> &v);
int main()
{
	long long int *lastnumber = nullptr;
	int numbertests;
	vector <int> num;
	num.resize(0);
	cin >> numbertests;
	long long int max_tidy;
	lastnumber = new (nothrow) long long int[numbertests];
	for (int i = 0; i < numbertests; i++)
	{
		cin >> lastnumber[i];
	}
	
	//solve
	for (int i = 0; i < numbertests; i++)
	{
		max_tidy = -1;
		for (long long int k = 0; k <= lastnumber[i]; k++)
		{
			split(k, num);
			if (tidy(num))
			{
				if (k >= max_tidy)
				max_tidy = k;
			}
			num.clear();
		}
		cout << "Case #" << i + 1 << ": " << max_tidy << endl;
	}
}
void split(int long long num, vector <int> &v)
{
	int x;
	while (num != 0)
	{
		x = num % 10;
		v.insert(v.begin(), x);
		num = num / 10;
	}
}
bool tidy(vector <int> l)
{
	if (l.size() == 1)
		return true;
	for (unsigned long long int i = 1; i < l.size(); i++)
	{
		if (l[i - 1] > l[i])
			return false;
	}
	return true;
}