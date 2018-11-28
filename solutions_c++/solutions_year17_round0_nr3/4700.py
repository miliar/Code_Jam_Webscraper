#include <bits/stdc++.h>
using namespace std;

#define nl cout<<"\n"


int main()
{
	int t,cnt=1;
	cin>>t;
	while(t--)
	{
		int n,m,i,k,x,lol;
		cin>>n>>k;
		
		cout<<"Case #"<<cnt<<": ";

		multiset<int> st;
		st.insert(n);

		for(i=1 ; i<=k ; i++)
		{
			lol = *st.rbegin();
			if(i==k)
			{
				x = lol/2;
				if(lol%2 == 0)
				{
					cout<<x<<" ";
					if(x==0)	cout<<0;
					else	cout<<x-1;
				}
				else	cout<<x<<" "<<x;
				nl;
			}
			else
			{
				auto iter = st.find(lol);
				st.erase(iter);
				if(lol%2 == 1)
				{
					if(lol/2>0){
						st.insert(lol/2);
						st.insert(lol/2);
					}
				}
				else{
					if(lol/2>0)
						st.insert(lol/2);
					if(lol/2>1)
						st.insert(lol/2-1);
				}
			}
		}
		cnt++;
	}
	return 0;
} 