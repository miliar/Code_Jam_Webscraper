#include <bits/stdc++.h>
using namespace std;
int main (void)
{
	int t;
	cin>>t;
	for(int x = 1 ; x <= t ; x++)
	{
		string s;
		cin>>s;
		for(int i = 0 ; i < s.size() - 1 ; i++)
		{
			if(s[i] > s[i+1])
			{
				int j;
				for(j = i+1 ; j < s.size() ; j++)
					s[j] = '9';
				
				j = i;
				while(j > 0 && s[j] == s[j-1])
				{
					s[j] = '9';
					j--;
				}
				s[j]--;
				break;
			}
		}
		cout<<"Case #"<<x<<": ";
		int size = 0;
		while(size < s.size() && (s[size] == '0'))
			size++;
		for(int k = size ; k<s.size() ; k++)
			cout<<s[k];
		cout<<endl;
	}

}