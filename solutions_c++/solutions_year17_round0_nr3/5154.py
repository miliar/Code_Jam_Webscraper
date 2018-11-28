#include <bits/stdc++.h>

using namespace std;

int main()
{
	long long int t, n, k, temp1 = 0, temp2 = 0, temp_flag, temp_max, temp_min, max, min, j, i, mul1, mul2, m1, m2, flag;
	cin >> t;
	long long int a = 0;
	long long int max_min[t][2];
	for(i = 0; i < t; i++)
	{
		max_min[i][0] = 0;
		max_min[i][1] = 0;
	}
	for(i = 0; i < t; i++)
	{
		////cout << "hello" << endl;
		temp1 = 0;
		temp2 = 0;
		flag = 0;
		cin >> n >> k;
		m1 = n;
		m2 = n;
		temp_max = n;
		temp_min = n;
		mul1 = 1;
		mul2 = 0;
		a = 0;
		while(a < k)
		{
			
			
			temp_flag = 0;
			for(j = 1; j <= mul1; j++)
			{
				if(m1 % 2 == 1)
				{
					max = (m1-1)/2;
					min = max;
					//cout << "here1" << endl;
				}
				else
				{
					max = m1/2;
					min = max - 1;
					temp_max = max;
					temp_min = min;
					temp_flag = 1;
					//cout << "here2" << endl;
				}
				a++;
				//cout << "hello2" << endl;
				if(a == k)
				{
					//cout << "ok" << mul1 << m1 << endl;
					max_min[i][0] = max;
					max_min[i][1] = min;
					flag = 1;
					break;
				}
				if(max == min)
				{
					//cout << "lol1" << endl;
				temp1 += 2;
				}
				else
				{
					//cout << "lol2" << endl;
					temp1++;
					temp2++;
				}
			}
			if(flag == 1) break;
			for(j = 1; j <= mul2; j++)
			{
				if(m2 % 2 == 1)
				{
					max = (m1-1)/2;
					min = max;
				}
				else
				{
					max = m2/2;
					min = max - 1;
					temp_max = max;
					temp_min = min;
					temp_flag = 1;
				}
				a++;
				//cout << "hello2re" << endl;
				if(a == k)
				{
					//cout << max <<" blah "<< min << endl;
					max_min[i][0] = max;
					max_min[i][1] = min;
					flag = 1;
					break;
				}
				if(max == min) 
					{
						//cout << "lol3" << endl;
						temp2 += 2;
					}
				else
				{
					//cout << "lol4" << endl;
					temp1++;
					temp2++;
				}
			}
			if(flag == 1) break;
			if(temp_flag == 1)
			{
				m1 = temp_max;
				m2 = temp_min;
			}
			else
			{
				m1 = max;
				m2 = min;
			}
			mul1 = temp1;
			mul2 = temp2;
			temp1 = 0;
			temp2 = 0;
		}
	}
	for(i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": " << max_min[i][0] << " " << max_min[i][1] << endl;
	}
	return 0;
}