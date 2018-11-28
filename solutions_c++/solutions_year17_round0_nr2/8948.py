#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <limits.h>
using namespace std;

#define all(v)     (((v).begin()),((v).end()))
#define sz(v)      ((int)((v).size()))
#define clr(v,d)   memset(v,d,sizeof(v))
#define rep(i,v)   for(int i=0;i<sz(v);++i)
#define lp(i, n)   for (int i = 0; i < (int)(n);++i)
#define lpi(i,j,n) for(int i=(j);i<(int)(n);++i)
#define lpd(i,j,n) for(i=(j);i>=(int)(n);--i)

typedef long long ll;
int numDugits(long long int num,int &fDigit)
{
	int digits[19];//max is 10^(18)
	long long int temp = num;
	int i = 0;
	while (temp != 0)
	{
		digits[i] = temp % 10;
		temp /= 10;
		i++;
	}
	fDigit = digits[i - 1];
	return i;
}

vector <long long int> tidyNumbers [19];

char digits[10] = { '0', '1','2','3','4','5','6','7','8','9' };

void genRecursive(string s, int numDigits)
{
	int i, j;
	if (s.size() == numDigits)
		tidyNumbers[numDigits].push_back(stoll(s));
	else
	{
		for (j = 1; j <= 9; j++)
			if (s[s.size() - 1] == digits[j])
			{
				for (i = j; i <= 9; i++)
					genRecursive(s + digits[i], numDigits);
			}
	}
}
/////////////////////

////////////////////////////////
/*
generate tidy numbers of 2-17 digits
(in a faster way using recursion)
then store them to a different vectors
make a read for x make the program wait
then download google code jam large test case
iterate for each test case seperately
depending on number of digits choose the test vector to iterate over
from the last to beginning
[in case the first digit is 1 iterate the vector from the first]
other wise iterate the vector from the last
*/
int main()
{
	int i;
	for (i = 0; i<=18; i++)
		tidyNumbers[i].clear();

	//cout<< "The maximum value of LONG = %ld\n"<<LLONG_MAX;
	for (int numdigits = 1; numdigits <= 18; numdigits++)
	{
		for (i = 1; i <= 9; i++)
		{
			string s = "";
			s += (digits[i]);
			genRecursive(s, numdigits);//generate all tidy of 4 digits - 
		}

		//for (int i = 0; i < tidyNumbers[numdigits].size(); i++)
		//fout2 << tidyNumbers[numdigits][i] << endl;
	}
	int x;
	cout << "Enter num" << endl;
	cin >> x;
	cout << x;
	//to make it wait until I download the large input file from GCJ


	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	//ofstream fout2("TidyNums.txt");

	int T;
	long long int num;
	unsigned int j;
	fin >> T;

	int retDigits,firstDigit=0;
	lp(i, T)
	{

		fin >> num;
	
		if (num == 10)
			num = 10;


		retDigits = numDugits(num, firstDigit);//get the number of digits in num
		 
		if(retDigits==1)
			fout << "Case #" << i + 1 << ": " << num << endl;
		else if(retDigits==19)
			fout << "Case #" << i + 1 << ": 999999999999999999" << endl;
		else
		{
			if (firstDigit == 1)
			{
				for ( j = 0; j < tidyNumbers[retDigits].size(); j++)
				{
					if ((tidyNumbers[retDigits])[j] >= num)
						break;
				}
				if(tidyNumbers[retDigits][j] == num)
					fout << "Case #" << i + 1 << ": " << num << endl;
				else 
					if(j!=0)
						fout << "Case #" << i + 1 << ": " << tidyNumbers[retDigits][j-1] << endl;
					else 
						fout << "Case #" << i + 1 << ": " << tidyNumbers[retDigits-1][tidyNumbers[retDigits-1].size()-1] << endl;
			}
			else
			{
				for (j = tidyNumbers[retDigits].size()-1; j >= 0; j--)
				{
					if (tidyNumbers[retDigits][j]  <=num)
						break;
				}
				fout << "Case #" << i + 1 << ": " << tidyNumbers[retDigits][j] << endl;

			}

		}
	}
	 
}

