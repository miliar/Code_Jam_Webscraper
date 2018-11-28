#include<bits/stdc++.h>
using namespace std;


int main()
{
	int t; cin >> t;
	for(int i = 1; i <= t; i++)
	{
		string s; int k; cin >> s >> k;

		vector<bool> v;
		bool flag1 = 0; int sindex = -1;
		int len = s.length();
		long long int flip = 0;
		bool arr[1005] = {0};

		for(int j = 0; j < len; j++)
		{
			int l = j + 1;
			if(s[j] == '+')
			{
				arr[l] = 1;
				v.push_back(1);
			}
			else
			{
				arr[l] = 0;
				if(flag1 == 0)
				{
					sindex = l;
					flag1 = 1;
				}
			}
		}

		while(v.size() != len && (len - sindex + 1 >= k))
		{
			for(int j = sindex; j <= sindex + k - 1; j++)
			{
				if(arr[j] == 1)
				{
					arr[j] = 0;
					v.pop_back();
				}
				else
				{
					arr[j] = 1;
					v.push_back(1);
				}
			}

			for(int j = sindex; j <= len; j++)
			{
				if(arr[j] == 0)
				{
					sindex = j;
					break;
				}
			}
			flip++;
		}

		if(len - sindex + 1 < k)
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": " << flip << endl;
	}
	return 0;
}