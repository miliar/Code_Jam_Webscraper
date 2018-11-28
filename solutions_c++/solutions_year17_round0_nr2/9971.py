#include <iostream>
#include <string>
using namespace std;

int N;

int isTidy(string num, int k)
{
	for(int i=0; i < k; i++)
	{
		if(num[i] > num[i+1])
			return i;
	}
	return -1;
}

string Solve(string num)
{
	int digit = num.length();
	if(digit == 1)
		return num;
	int check = isTidy(num, digit-1);
	int j;
	if(check == -1)
		return num;
	else
	{
		while(1)
		{
			num[check]--;
			j = check+1;
			check = isTidy(num, check);
			if(check == -1)
				break;
		}
	}
	for(int i=j; i < digit; i++)
		num[i] = '9';
	int i;
	for(i=0; num[i] == '0'; i++);
	num = num.substr(i);
	return num;
}

int main()
{
	cin >> N; 
	for(int i=0; i < N; i++)
	{
		string num;
		cin >> num;
		string y = Solve(num);
		cout << "Case #" << i+1 << ": " << y << endl;
	}
	return 0;
}
