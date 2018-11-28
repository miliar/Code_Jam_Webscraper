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
		vector<int> v;
		vector<int> output;
		int n=s.size();
		for (int i = 0; i < n; ++i)
		{
			v.push_back(s[i]-'0');
		}
		int i = n-1;
		while(true)
		{
			if(i!=0)
			{
				// cout<<i<<endl;
				// cout<<"before:";
				// for (int j = 0; j < n; ++j)
				// {
				// 	cout<<v[j];
				// }
				// cout<<endl;	
				if(v[i]==-1)
				{
					v[i] = 9;
					for (int l = i; l < n; ++l)
					{
						v[l]=9;
					}
					v[i-1]--;
					continue;
				}
				else
				{
				if(v[i]<v[i-1])
				{
					v[i]=9;
					for (int l = i; l < n; ++l)
					{
						v[l]=9;
					}
					v[i-1]--;
				}
				}
				// cout<<"after:";
				// for (int j = 0; j < n; ++j)
				// {
				// 	cout<<v[j];
				// }
				// cout<<endl;	
				i--;
			}
			else
			{
				break;
			}

		}
		cout<<"Case #"<<k+1<<": ";
		for (int j = 0; j < v.size(); ++j)
		{
			if(j==0){
				if(v[j]!=0)
				{
					cout<<v[j];
				}
			}
			else
			{
				cout<<v[j];
			}
		}
		cout<<endl;
	}
}