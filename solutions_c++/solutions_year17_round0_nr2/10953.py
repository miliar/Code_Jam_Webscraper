#include <bits/stdc++.h>

using namespace std;

bool tidy(int);

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	
	int T;
	cin>>T;
	for(int tt=1; tt<=T; tt++)
	{
		cout<<"Case #"<<tt<<": ";
		int n;
		cin>>n;
		if(tidy(n))
		{
			cout<<n<<endl;
			continue;
		}
		
		while(n--)
		{
			if(tidy(n))
			{
				cout<<n<<endl;
				break;
			}
		}
	}
	return 0;
}

bool tidy(int n)
{
	int t = n, i = 1, s = 0;
	while(t!=0)
	{
		s++;
		i *= 10;
		t /= 10;
	}
	i /= 10;
	int a[s];
	for(int j=0; j<s; j++)
	{
		a[j] = (int)(n/i);
		n %= i;
		i /= 10;
		if(j!=0 && a[j]<a[j-1]) return 0;
	}
	return 1;
}