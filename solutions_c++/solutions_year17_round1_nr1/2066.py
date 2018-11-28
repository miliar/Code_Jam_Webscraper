#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
void docopy(int r, int c, string arr[])
{
	for(int i = 0;i < r;i++)
	{
		for(int j = 0;j < c;j++)
		{
			if(arr[i][j]=='?')
			{
				int k;
				for(k = j+1;k < c;k++)
					if(arr[i][k]!='?')
					{
						arr[i][j] = arr[i][k];
						break;
					}
				if(k  == c)
				{
					for(k = j-1;k >= 0;k--)
					if(arr[i][k]!='?')
					{
						arr[i][j] = arr[i][k];
						break;
					}	
				}
			}
		}
	}
}

bool isfull(string arr[], int r, int c)
{
	for(int i = 0;i < c;i++)
		if(arr[r][i]!='?')
			return false;
			
	return true;		
}

int main(void)
{
	int t, case_no = 1;
	cin >> t;
	for(case_no; case_no <= t;case_no++)
	{
		int r, c;
		cin >> r >> c;
		string arr[r];
		for(int i = 0;i < r;i++)
			cin >> arr[i];
		
		docopy(r,c,arr);
		for(int i = 0;i < r;i++)
		{
			if(isfull(arr, i, c))
			{
				int k;
				for(k = i-1;k >= 0;k--)
					if(!isfull(arr,k,c))
					{
						arr[i] = arr[k];
						break;
					}
				if(k == -1)
				{
					for(k = i+1;k < r;k++)
					if(!isfull(arr,k,c))
					{
						arr[i] = arr[k];
						break;
					}
				
				}
			}
		}
		
		cout << "Case #" << case_no << ":" << endl;
		for(int i = 0;i < r;i++)
			cout << arr[i] << endl;
	}
}