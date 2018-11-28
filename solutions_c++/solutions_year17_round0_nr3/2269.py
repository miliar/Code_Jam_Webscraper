#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	for(int i = 1; i<=t; ++i)
	{
		long long int n,k;
		cin>>n>>k;

		unordered_map<long long int, long long int> m;
		set<long long int> s;
		
		s.insert(n);
		m[n] = 1;
		
		int flag = 0;
		while(1)
		{	
			flag = 0;
			if(s.size()==1)
			{
				long long int l = *s.begin(); 
				
				if(k - m[l] <= 0)
				{	
					flag = 1;
					break;
				}
				k = k - m[l];
				
				s.erase(s.begin());
				if(l%2==0)
				{
					s.insert(l/2);
					s.insert(l/2 - 1);
					m[l/2]+=m[l];
					m[l/2 -1]+=m[l];
				}
		
				else
				{
					s.insert(l/2);
					m[l/2]+=2*m[l];
				}
				
			}
			
			else if(s.size()==2)
			{
				long long int l = *s.begin();
				set<long long int>::iterator it = s.begin();
				advance(it, 1);
				long long int h = *it; 
				
				//cout<<l<<" "<<h<<endl;
				//cout<<m[l]<<" "<<m[h]<<endl;
				
				if(k - m[l] - m[h] <= 0)
				{	
					flag = 2;
					break;
				}
				
				
				k = k - m[l] - m[h];
				s.erase(s.begin());
				s.erase(s.begin());
				
				if(l%2==0)
				{
					s.insert(l/2);
					s.insert(l/2 - 1);
					m[l/2]+=m[l];
					m[l/2 -1]+=m[l];
				}
		
				else
				{
					s.insert(l/2);
					m[l/2]+=2*m[l];
				}
				
				if(h%2==0)
				{
					s.insert(h/2);
					s.insert(h/2 - 1);
					m[h/2]+=m[h];
					m[h/2 -1]+=m[h];
				}
		
				else
				{
					s.insert(h/2);
					m[h/2]+=2*m[h];
				}
				
			}
			
			
			
			
		}
		
		if(flag==1)
		{
			long long int l = *(s.begin());
			s.erase(s.begin());
			if(l%2==0)
				cout<<"Case #"<<i<<": "<<l/2<<" "<<l/2 - 1<<"\n";
			else
				 cout<<"Case #"<<i<<": "<<l/2<<" "<<l/2<<"\n";	
		}
		
		else if(flag==2)
		{
			long long int l = *(s.begin());
			s.erase(s.begin());
			long long int h = *(s.begin());
			s.erase(s.begin());
			
			if(k<=m[h])
			{	
				if(h%2==0)// && h > 1)
					cout<<"Case #"<<i<<": "<<h/2<<" "<<h/2 - 1<<"\n";
				//else if(h<2)
					//cout<<"Case #"<<i<<": 0 0"<<"\n";
				else
				    cout<<"Case #"<<i<<": "<<h/2<<" "<<h/2<<"\n";
			}
			
			else
			{
				if(l%2==0)// && l>1)
					cout<<"Case #"<<i<<": "<<l/2<<" "<<l/2 - 1<<"\n";
				//else if(l<2)
					//cout<<"Case #"<<i<<": 0 0"<<"\n";
				else
				    cout<<"Case #"<<i<<": "<<l/2<<" "<<l/2<<"\n";
				
			}
		}
		
	}

	return 0;
}
