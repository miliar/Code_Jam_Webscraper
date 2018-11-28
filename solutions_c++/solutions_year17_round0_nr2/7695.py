#include<bits/stdc++.h>
#define s second
using namespace std;

ifstream goo;
ofstream gle;

vector<int> v;

void solve()
{
	int n,a=0;
	goo>>n;
	while(v[a]<=n) a++;
	gle<<v[a-1]<<"\n";
	return;
}

int main()
{
	goo.open("C:\\Users\\Mateusz\\Desktop\\Testy\\B-small-attempt0 (3).in");
	gle.open("C:\\Users\\Mateusz\\Desktop\\Testy\\tak.out");
	int t;
	goo>>t;
	v.push_back(-1);
	for(int i=1; i<=1000; i++)
	{
		int a=i,b=9,c=1;
		while(a!=0)
		{
			if(a%10>b)
			{
				c=0;
				break;
			}
			b=a%10;
			a/=10;
		}
		if(c==1) v.push_back(i);
	}
	v.push_back(10000);
	for(int i=1; i<=t; i++)
	{
		gle<<"Case #"<<i<<": ";
		solve();
	}
	goo.close();
	gle.close();
	return 0;
}
