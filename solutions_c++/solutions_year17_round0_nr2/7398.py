#include<iostream>
#include<string>

using namespace std;

int main()
{
	int t;
	string num, ans;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>num;
		ans.clear();
		if (num.length() == 1)
			ans = num;
		else
		{
			bool flag = false, equal = false;
			short count = 0;
			for (size_t j=0;j<num.length();j++)
			{
				if (flag)
				{
					ans.push_back('9');
					continue;
				}
				if (num[j]<num[j+1] || j == num.length()-1)
				{
					if (equal)
					{
						ans.append(count, num[j]);
						equal = false;
						count = 0;
					}
					ans.push_back(num[j]);
				}
				else if (num[j] == num[j+1])
				{
					count++;
					equal = true;
				}
				else
				{
					if (equal)
					{
						if (num[j]!='1') ans.push_back(num[j]-1);
						ans.append(count, '9');
						equal = false;
						count = 0;
					}
					else
						if (num[j]!='1') ans.push_back(num[j]-1);
					flag = true;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}

