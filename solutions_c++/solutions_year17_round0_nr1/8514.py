#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

int main()
{
	unsigned long int t,t1,k,n,i,count;
	string str;
	vector<bool> b;
	cin>>t;
	t1=1;
	while(t--)
	{
		cin>>str>>k;
		replace(str.begin(),str.end(),'+','0');
		replace(str.begin(),str.end(),'-','1');
		n=str.length();
		for(i=0; i<n; i++)
			b.push_back(bool(str.at(i)=='1'));
		count=0;
		for(i=0; i<n-k+1; i++)
		{
			if(b[i])
			{
				for(int j=0; j<k; j++)
				{
					b[i+j].flip();
				}
				count++;
			}
		}
		for(i=0; i<k; i++)
			if(b[n-i-1])
				break;
		if(i==k)
		cout<<"Case #"<<(t1)++<<": "<<count<<endl;
		else
		cout<<"Case #"<<(t1)++<<": IMPOSSIBLE"<<endl;
		b.clear();
	}
	return 0;
}
