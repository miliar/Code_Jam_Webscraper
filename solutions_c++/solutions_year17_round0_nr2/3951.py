#define ull unsigned long long
#define _DEBUG_ false
#include <iostream>
#include <string>
#include <sstream>
using namespace std;



int T;

int digits[20];

int numDigits;

inline void SplitNumber(string num)
{
	numDigits = num.size();
	for (int i = 0; i < numDigits; i++)
	{
		digits[numDigits - i - 1] = num[i]-'0';
	}

}

inline void Answer()
{
	int carry = 0;
	for (int i = 0; i < numDigits-1; i++)
	{
		digits[i] -= carry;
		if (digits[i] < digits[i + 1] || digits[i] <= 0)
		{
			for(int j = i; j>=0; j--)
				digits[j] = 9;
			carry = 1;
		}
		else
		{
			carry = 0;
		}
	}
	digits[numDigits-1] -= carry;
}

ull AsInteger()
{
	ull res = 0;
	ull exp = 1;
	for (int i = 0; i < numDigits; i++)
	{
		res += (digits[i] * exp);
		exp *= 10;
	}
	return res;
}

#if _DEBUG_
bool IsNonDescending(ull num)
{
	if (num == 10) return false;
	int old, cur;

	old = num % 10;
	ull cn = num/10;
	while (cn > 0)
	{
		cur = cn % 10;
		cn /= 10;
		if (cur > old) return false;
		old = cur;
	}
	return true;
}

ull Brute(string num)
{
	stringstream s(num);
	ull n;
	s >> n;
	s.clear();
	while (n > 0)
	{
		if (IsNonDescending(n)) return n;
		n--;
	}
	return 0;
}
#endif

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		string number;
		number.reserve(20);
		cin >> number;//scanf("%llu", &number);
		
		SplitNumber(number);
		Answer();
		cout << "Case #" << i << ": " << AsInteger() << "\n";
		
	}
	return 0;
}