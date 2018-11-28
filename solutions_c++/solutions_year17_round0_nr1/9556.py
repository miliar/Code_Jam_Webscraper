#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	int counter;
	int k;
	string a;
	cin >>t;
	bool is_possible;
	for(int i=0;i<t;i++)
	{
		counter=0;
		is_possible=true;
		cin>>a>>k;
		for(int j=0;j<(int) (a.length()-k+1);j++)
		{
			if(a[j]=='-')
			{
				for(int b=0;b<k;b++)
				{
					a[b+j]=(a[b+j]=='+')*('-')+(a[b+j]=='-')*('+');
				}
				counter++;
			}
		}
		for(int j=(int) (a.length()-k+1);j<(int) a.length();j++)
		{
			is_possible=is_possible&&(a[j]=='+');
		}
		if(is_possible)
		{
			cout << "CASE #" << (i+1) << ": "<<counter<<endl;
		}
		else
		{
			cout << "CASE #" << (i+1) << ": IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}
