#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i = 0; i<t; i++)
	{
		long n, k, p = 0, lpos, rpos;
		cin>>n>>k;
		long a[1005];
		a[p++] = (n - 1)/2;
		lpos = a[0];
		rpos = n - a[0] - 1;
		p = p + 2;
		a[1] = -1;
		a[2] = n;
		sort(a, a+p);
		k--;
		for(int j = 0; j<k; j++)
		{
			long max = -1, pos;
			for(int u = p - 1; u>0; u--)
				if(a[u] - a[u - 1]>=max)
				{
					max = a[u] - a[u - 1];
					pos = u;
				}
			a[p++] = (a[pos] + a[pos - 1])/2;
			if(j == k - 1)
			{
				for(int e = 0; e<(p - 1); e++)
					if(a[p - 1]>a[e] && a[p - 1]<a[e + 1])
					{
						lpos = a[p - 1] - a[e] - 1;
						rpos = a[e + 1] - a[p - 1] - 1; 
					}
			}
			sort(a, a+p);
		}
		cout<<"Case #"<<i + 1<<": ";
		if(lpos<rpos)
			cout<<rpos<<" "<<lpos<<endl;
		else
			cout<<lpos<<" "<<rpos<<endl;
	}
}