#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t;
	cin>>t;
	for(int o=1;o<=t;o++)
	{
		long long n,k;
		cin>>n>>k;
		set<long long,greater<long long> > s;
		s.insert(n);
		map<long long,long long> m;
		m[n]++;
		long long ans1=0,ans2=0;
		while(1)
		{
			long long tmp=*s.begin();
			
			s.erase(s.begin());
			k-=m[tmp];
			if(k<=0)
			{
				if(tmp&1)
				{
					ans1=tmp/2;
					ans2=tmp/2;
				}
				else
				{
					ans1=tmp/2;
					ans2=tmp/2-1;
				}
				break;
			}
			if(tmp&1)
			{
				s.insert(tmp/2);
				m[tmp/2]+=m[tmp]*2;
			}
			else
			{
				s.insert(tmp/2);
				s.insert(tmp/2-1);
				m[tmp/2]+=m[tmp];
				m[tmp/2-1]+=m[tmp];
			}
		}
		cout<<"Case #"<<o<<": "<<ans1<<' '<<ans2<<'\n';
	}

}