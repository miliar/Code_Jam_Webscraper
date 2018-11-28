#include<bits/stdc++.h>

using namespace std;

int n,t;

bool uredan(int t)
{
	vector <int> v;
	bool tidy=true;
	while (t>0)
	{
		v.push_back(t%10);
		t/=10;
	}
	reverse(v.begin(),v.end());
	int last = v[0];
	for (int i=1; i<v.size(); ++i)
	{
		if (v[i]<last)tidy=false;
		last=v[i];
	}
	return tidy;
}

int main ()
{
	cin >>n;
	for (int i=0; i<n; ++i)
	{
		cin >>t;
		for (int j=t; j>-1; --j)
		{
			t=j;
			if (uredan(t))
			{
				cout <<"Case #"<<i+1<<": "<<t<<endl;
				break;
			}
		}
	}
	return 0;
}
