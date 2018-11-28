#include<iostream>
#include<map>
using namespace std;
#define ll long long int 

void findmax(ll n ,ll v,ll k)
{
	
			if(v==n)
			{
						cout<<"Case #"<<k<<": "<<0<<" "<<0<<endl;
						return ;
			}		
	ll x = n;     		
	ll low ,hi;
	
	map<ll,ll> m1;
		if(x%2==0)
		{
			hi = x/2  ;
			low = x - hi -1;
			m1.insert(pair<ll,ll>(hi,1));
			m1.insert(pair<ll,ll>(low,1));
		}
		if(x%2!=0)
		{

			hi = x/2 ;
			low = hi;
			m1.insert(pair<ll,ll>(hi,2));
			
		}

		if(v==1)
		{
			cout<<"Case #"<<k<<": "<<hi<<" "<<low<<endl;
			return ;
		}
		map<ll,ll>::reverse_iterator  bt =  m1.rbegin();
		x = bt->first;
		
		ll flag = 0;
		for(ll j =2;j<=v;j++)
		{
			if(x==0)
			{
				flag = 1;
				break;
			}
			map<ll,ll>::reverse_iterator  rt =  m1.rbegin();
			x = rt->first;
			map<ll,ll>::iterator  it =  m1.find(x);
			if(it->second>1)
			{
				if(j+it->second-1>=v)
				{
					ll c1,c2;
					if(it->first%2==0)
					{
						c1 = it->first/2;
						c2 = it->first - c1 - 1;
					}
					if(it->first%2!=0)
					{
						c1 = it->first/2;
						c2 =  c1;
					}
					cout<<"Case #"<<k<<": "<<c1<<" "<<c2<<endl;
					return;
				}
				if((j+it->second-1)<v)
				{
					ll c1,c2;
					if(it->first%2==0)
					{
						c1 = it->first/2;
						c2 = it->first - c1 - 1;
						if(m1.count(c1)>0){ m1.at(c1)= m1.at(c1)+it->second;}
						if(m1.count(c2)>0){m1.at(c1) = m1.at(c2)+it->second;}
						if(!(m1.count(c1)>0)){m1.insert(pair<ll,ll>(c1,it->second));}
						if(!(m1.count(c2)>0)){m1.insert(pair<ll,ll>(c2,it->second));}
					}
					if(it->first%2!=0)
					{
						c1 = it->first/2;
						c2 =  c1;        
						if(m1.count(c1)>0){m1.at(c1)= m1.at(c1)+((it->second)*2);}
						else{m1.insert(pair<ll,ll>(c1,((it->second)*2)));}
					}
					j =  j+it->second-1;
					x  = c1;
					m1.erase(it);
					continue;
				}
			}
			if(it->second==1)
			{
				m1.erase(it);
			}
			if(x%2==0)
			{
				hi = x/2  ;
				low = x - hi -1;
				//cout<<hi<<" hdhh "<<low<<endl;
				if(m1.count(hi)>0){ m1.at(hi)= m1.at(hi)+1;}
				if(m1.count(low)>0){m1.at(low)= m1.at(low)+1;}
				if(!(m1.count(hi)>0)){m1.insert(pair<ll,ll>(hi,1));}
				if(!(m1.count(low)>0)){m1.insert(pair<ll,ll>(low,1));}
			
			}
			if(x%2!=0)
			{

				hi = x/2 ;
				low = hi;
				//cout<<hi<<" hdhh "<<low<<endl;
				if(m1.count(hi)>0){m1.at(hi)= m1.at(hi)+2;}
				else{m1.insert(pair<ll,ll>(hi,2));}
			}
			if(j==v)
			{
				
				cout<<"Case #"<<k<<": "<<hi<<" "<<low<<endl;
			 	return ;
			}
		}
		if(flag==1)
	{
		cout<<"Case #"<<k<<": "<<"0"<<" "<<"0"<<endl;
			return ;
	}

}







int main()
{
	ll t,k=0;
	cin>>t;
	for(ll i= 0;i<t;i++)
	{
		k++;
		ll n,v,j;
		cin>>n>>v;
		findmax(n,v,k);
	}
}
