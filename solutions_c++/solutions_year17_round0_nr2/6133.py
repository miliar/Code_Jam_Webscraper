#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<string.h>

using namespace std;
typedef unsigned long long int ulli;

int main()
{
	freopen("G:\\PDF\\Electronics\\6th sem Electronics\\Digital Communication\\B-large.in", "r", stdin);
	freopen("G:\\PDF\\Electronics\\6th sem Electronics\\Digital Communication\\output_file_name1.out", "w", stdout);
	int t;
	int cont = 0;
	cin >> t;
	while (t--)
	{
		cont++;
		ulli x,y;
		cin >> x;
		vector<int>arr;
		y = x;
		while (y > 0)
		{
			arr.push_back(y % 10);
			y = y / 10;
		}
		
		ulli ans;
		if (arr.size() == 1)
		{
			ans = arr[0];
		}
		else
		{
			int n = arr.size();
			int m = arr[n - 1];
			int i = n - 1;
			
			while (i >= 0 && m <= arr[i])
			{
				
				m = arr[i];
				i--;
			}
			if (i < 0)
			{
				ans = x;
			}
			else
			{
				int j = i;
				while (i >= 0)
				{
					arr[i] = 9;
					i--;
				}
				j++;
				arr[j]--;
				while (j < n-1)
				{
					if (arr[j + 1] > arr[j])
					{
						arr[j] = 9;
						arr[j + 1]--;
					}
					j++;
				}
			}
			ans = 0;
			for (int i = n-1; i>=0; i--)
			{
				ans = ans * 10 + arr[i];
			}
		}
		cout << "Case #" << cont << ": " << ans << endl;
	}
	return 0;
}