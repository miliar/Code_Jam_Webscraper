#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <iostream>
#include <deque>
#include <algorithm>
#include <vector>
#include <ctime>

using namespace std;

int main()
{
	int n;
	string str;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>n;
	int i,j,k;
	for (i=0;i<n;i++)
	{
		cin>>str;
		j = str.length()-1;
		while (j>0)
		{
			if (str[j] < str[j-1])
			{
				for (k=j;k<str.length();k++)
				{
					str[k] = '9';
				}
				str[j-1] --;
			}
			j--;
		}
		if (str[0] == '0')
		{
			k = str.length();
			for (j=0;j<k;j++)
			{
				str[j] = str[j+1];
			}
			str[k-1] = 0;
		}
		cout<<"Case #"<<i+1<<": ";
		for (j=0;j<str.length();j++)
		{
			if (str[j] >= '0') cout<<str[j];
			else break;
		}
		cout<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
