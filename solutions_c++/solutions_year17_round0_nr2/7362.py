#include <iostream>
#include <cstring>
#include <string.h>
#include <vector>
#include <map>
#include <limits>
#include <algorithm>
using namespace std;


int main()
{
	int t;
	cin>>t;
	for (int k = 0; k < t; ++k)
	{
		string s;
		cin>>s;
		vector<int> temp_vector;
		vector<int> output;
		int n=s.size();
		for (int i = 0; i < n; ++i)
		{
			temp_vector.push_back(s[i]-'0');
		}
		int i = n-1;
		while(true)
		{
			if(i!=0)
			{
				if(temp_vector[i]==-1)
				{
					temp_vector[i] = 9;
					for (int l = i; l < n; ++l)
					{
						temp_vector[l]=9;
					}
					temp_vector[i-1]--;
					continue;
				}
				else
				{
				if(temp_vector[i]<temp_vector[i-1])
				{
					temp_vector[i]=9;
					for (int l = i; l < n; ++l)
					{
						temp_vector[l]=9;
					}
					temp_vector[i-1]--;
				}
				}
				i--;
			}
			else
			{
				break;
			}

		}
		cout<<"Case #"<<k+1<<": ";
		for (int j = 0; j < temp_vector.size(); ++j)
		{
			if(j==0){
				if(temp_vector[j]!=0)
				{
					cout<<temp_vector[j];
				}
			}
			else
			{
				cout<<temp_vector[j];
			}
		}
		cout<<endl;
	}
}