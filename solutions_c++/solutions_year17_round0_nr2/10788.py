//B
#include<iostream>
#include<cmath>
using namespace std;

bool getBiggestTidy1(int);
int getBiggestTidy2(int);

int main()
{
	int n;
	cin >> n;
	int* a = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}
	for (int i = 0; i < n; i++)
	{
		cout << "Case #" << i + 1 << ": " << getBiggestTidy2(a[i]) << endl;
	}


	return 0;
}
bool getBiggestTidy1(int n)
{
	int temp = n;
	int NumberCount = 0;
	while (temp)
	{
		temp /= 10;
		++NumberCount;
	}
	int min = INT_MIN, currentNumber;
	bool isTidy = true;
	for (int i = NumberCount; i > 0; i--)
	{
		int mode = (int)pow(10, i - 1);
		currentNumber = (n / mode) % 10;
		if (currentNumber >= min)
			min = currentNumber;
		else
		{
			isTidy = false;
			break;
		}
	}
	return isTidy;
}
int getBiggestTidy2(int n)
{
	if (n < 10)
	{
		return n;
	}
	bool res;
	while (n >= 10)
	{
		res = getBiggestTidy1(n);
		if (res)
			return n;
		else
		{
			n--;
		}
	}
}