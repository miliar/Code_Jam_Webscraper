#include <iostream>
#include <string.h>
#include <math.h>
#include <limits.h>
using namespace std;

bool check(char arr[], int start, int end)
{
	char prev = arr[start];
	char cur;
	for(int i=start+1; i<=end; i++)
	{
		cur = arr[i];
		if(cur >= prev)
			prev = cur;
		else
			return false;
	}
	return true;
}

int main(int argv, char* args[])
{
	int t;
	cin >> t;

	char num[20];
	int n;

	for(int z=1; z<=t; z++)
	{
		cin >> num;
		n = strlen(num);
		int i;
		if(check(num, 0, n-1))
		{
			
		}
		else
		{
			for(i=strlen(num) - 1; i>=0; i--)
			{
				if(check(num, i, n-1))
					continue;
				else
					break;
			}
			
			for(int j=i+1; j<n; j++)
			{
				num[j] = '9';
			}
			if(num[i] == '0')
			{
				int temp = i;
				while(num[temp] == '0' &&  temp>0)
				{
					num[temp] = '9';
					temp --;
				}
				num[temp] = num[temp] - 1;
			}
			else
			{
				num[i] = num[i] - 1;
			}
			i--;

			while(check(num, i, n-1)==false)
			{
				//cout << "first while with i = " << i << endl;
				for(; i>=0; i--)
				{
					if(check(num, i, n-1))
						continue;
					else
						break;
				}
				for(int j=i+1; j<n; j++)
				{
					num[j] = '9';
				}
				if(num[i] == '0')
				{
					int temp = i;
					while(num[temp] == '0' &&  temp>0)
					{
						num[temp] = '9';
						temp --;
					}
					num[temp] = num[temp] - 1;
					i = temp - 1;
				}
				else
				{
					num[i] = num[i] - 1;
				}
				i--;
			}
		}
		int count=0;
		for(int i=0; i<n; i++)
		{
			if(num[i] == '0')
				count++;
		}
		char ans[n - count + 1];
		for(int i=0; i<(n - count); i++)
		{
			//cout << " Assigning "<< num[i+count] << endl;
			ans[i] = num[i+count];
		}
		ans[n-count] = '\0';




		cout << "Case #" <<  z<< ": "<< ans;
		cout << endl;
	}
}