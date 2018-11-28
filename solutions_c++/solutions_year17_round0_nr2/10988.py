#include<iostream>
#include<stdio.h>
using namespace std;
int asc(long long int n);  // '1' for ascending
int len(long long int i);  //returns length as integer
int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	//declaration
	long long int num,temp,l;
	//end declaration
	int tt;
	cin >> tt;
		for (int i = 1; i <= tt; i++)
		{
			cout << "Case #" << i << ": ";
			
		cin >> num;
		
		temp = num;
		//start test case
		a:
		l = len(temp);
		if (asc(temp) == 1)
		{
			cout << temp << endl;
	    }
		else {
			temp--;
			goto a;
		}
        // end test case
	}
	

		
system("pause");
	return 0;
}

int asc(long long int n)
{
	int next_digit = n % 10;
	n = n / 10;
	while (n)
	{
		int digit = n % 10;
		if (digit > next_digit)
			return 0;
		next_digit = digit;
		n = n / 10;
	}
	return 1;
}
int len(long long int i){
	 int l = 0;
	for (; i; i /= 10) l++;
	return l == 0 ? 1 : l;
}