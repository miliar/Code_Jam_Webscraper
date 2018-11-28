/*input
4
132
21
12323123123213233
111111111111111110
*/
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false);
	int test, z;
	cin>>test;
	for(z = 1; z <= test; z++)
	{
		cout<<"Case #"<<z<<": ";
		long long int n, ans, temp, dig, power = 0;
		cin>>n;
		temp = n;
		int i = 0, j;
		vector<long long int> v;
		while(temp)
		{
			v.insert(v.begin(), temp%10);
			temp = temp/10;
		}
		for(i = v.size()-1 ; i > 0; i--)
		{
			if(v[i] < v[i-1])
			{
				v[i-1]--;
				// v[i] = 9;
				for(j = i; j < v.size() ; j++)
				{
					v[j] = 9;
				}
			}
		}
		int flag = 0;
		for(i = 0; i < v.size() ; i++)
		{

			if(v[i]!=0)
			{
				flag = 1;
			}
			if(flag)
			{
				cout<<v[i];
			}
		}

		cout<<endl;
	}
	return 0;
}