#include <iostream>
using namespace std;
typedef long long int ll;
int main()
{
	ll t, n, ans[20], prev, flag, count, digits[20], count1;
	cin>>t;
	for (int i = 0; i < t; i++)
	{
		cin>>n;
		flag = count = count1 = 0;
		for (int j = 0; j < 20; j++)
			ans[j] = 0;
		for (int j = 0; n != 0; j++)
		{
			digits[count1] = n % 10;
			n /= 10;
			count1++;
		}
		for (int j = count1-1; j >= 0; j--)
		{
			ll temp = digits[j];
			if (flag)
			{
				ans[count] = 9;
			}
			else if (count != 0)
			{
				if (ans[count-1] <= temp)
				{
					ans[count] = temp;
				}
				else
				{	
					ll temp2 = count-1;
					while (true)
					{
						if (ans[temp2] != 0 and (temp2 == 0 or (ans[temp2-1] < ans[temp2])))
						{
							ans[temp2]--;
							break;
						}
						temp2--;
					}
					temp2++;
					for ( ; temp2 < count; temp2++)
						ans[temp2] = 9;
					flag = 1;
					ans[count] = 9;
				}
			}
			else
				ans[count] = temp;
			count++;
		}
		ll start = 0;
		for (int y = 0; y < count; y++)
		{
			if (ans[y] != 0)
				break;
			start++;
		}
		cout<<"Case #"<<i+1<<": ";
		for (int j = start; j < count; j++)
			cout<<ans[j];
		cout<<"\n";
	}
}