/*   ______________
	| Program Name |
	 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯
*/

#include <bits/stdc++.h>
using namespace std;
vector<int > digits;
void convert(long long int n)
{
	while(n>0)
	{
		digits.push_back(n%10);
		n=n/10;

	}
	reverse(digits.begin(), digits.end());
}
unsigned long long int convert_to_number()
{
	unsigned long long int i, number = 0;
	for (i = 0; i < digits.size(); i++)
	{
	    number = 10 * number + digits[i];
	}
	return number;
}
int main()
{
	
	int t;
	cin>>t;
	for(int test=0;test<t;test++)
	{
		long long int n;
		cin>>n;
		bool flag=0;
		convert(n);
		// cout<<"after conversion  size = "<<digits.size()<<endl;
		while(flag==0)
		{
			flag=1;
			for(int i=1;i<digits.size();i++)
			{
				if(digits[i]<digits[i-1])
				{
					digits[i-1]--;
					for(int j=i;j<digits.size();j++)
					{
						digits[j]=9;
					}	
					flag=0;
				}
			}
		}
		// cout<<digits.size()<<endl;
		// for(int i=0;i<digits.size();i++)
		// {
		// 	cout<<digits[i]<<" ";
		// }
		// cout<<endl;
		cout<<"Case #"<<test+1<<": "<<convert_to_number()<<endl;
		// cout<<convert_to_number()<<endl;
		digits.clear();


	}
	return 0;
}