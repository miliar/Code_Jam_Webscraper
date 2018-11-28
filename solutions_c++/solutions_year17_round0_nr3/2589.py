#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		uint64_t n,k,cur=0,l,r;
		cin>>n>>k;
		pair<uint64_t, uint64_t> a,b,t1,t2;
		a.first=1;
		a.second=n;
		b.first=0;
		b.second=0;
		for(;;)
		{
			t1.first=0;t2.first=0;
			t1.second=0;t2.second=0;
			cur+=a.first;

			if(a.second&1)
			{
				t1.first = 2*a.first ;
				t1.second = a.second/2;
				if(cur>=k) { l = r = a.second/2;  break; }
			}
			else
			{
				t1.first = a.first;
				t1.second = a.second/2;
				t2.first = a.first;
				t2.second = a.second/2 - 1;
				if(cur>=k) { l = a.second/2; r=l-1; break; }
			}

			if(b.first)
			{
				cur+=b.first;
				if(b.second&1)
				{
					t2.first+=b.first*2;
					if(cur>=k) { l = r = b.second/2; break; }
				}
				else
				{
					t1.first+=b.first;
					t2.first+=b.first;
					t2.second = b.second/2 -1;
					if(cur>=k) { l = b.second/2; r = l-1; break; }
				}
			}

			a.first=t1.first;a.second=t1.second;
			b.first=t2.first;b.second=t2.second;

		}
		cout<<"Case #"<<c<<": "<<l<<" "<<r<<endl;

	}
	return 0;
}
