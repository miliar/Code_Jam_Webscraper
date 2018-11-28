#include<iostream>
#include<map>
using namespace std;
#define ll long long int 

void undertaker(ll n ,ll v,ll k)
{
	
			if(v==n)
			{
						cout<<"Case #"<<k<<": "<<0<<" "<<0<<endl;
						return ;
			}		
	ll x = n;     		
	ll nichewala ,upper;
	
	map<ll,ll> map1val;
		if(x%2==0)
		{
			upper = x/2  ;
			nichewala = x - upper -1;
			map1val.insert(pair<ll,ll>(upper,1));
			map1val.insert(pair<ll,ll>(nichewala,1));
		}
		if(x%2!=0)
		{

			upper = x/2 ;
			nichewala = upper;
			map1val.insert(pair<ll,ll>(upper,2));
			
		}

		if(v==1)
		{
			cout<<"Case #"<<k<<": "<<upper<<" "<<nichewala<<endl;
			return ;
		}
		map<ll,ll>::reverse_iterator  bt =  map1val.rbegin();
		x = bt->first;
		
		ll flag = 0;
		for(ll j =2;j<=v;j++)
		{
			if(x==0)
			{
				flag = 1;
				break;
			}
			map<ll,ll>::reverse_iterator  rt =  map1val.rbegin();
			x = rt->first;
			map<ll,ll>::iterator  it =  map1val.find(x);
			if(it->second>1)
			{
				if(j+it->second-1>=v)
				{
					ll val1,val2;
					if(it->first%2==0)
					{
						val1 = it->first/2;
						val2 = it->first - val1 - 1;
					}
					if(it->first%2!=0)
					{
						val1 = it->first/2;
						val2 =  val1;
					}
					cout<<"Case #"<<k<<": "<<val1<<" "<<val2<<endl;
					return;
				}
				if((j+it->second-1)<v)
				{
					ll val1,val2;
					if(it->first%2==0)
					{
						val1 = it->first/2;
						val2 = it->first - val1 - 1;
						if(map1val.count(val1)>0){ map1val.at(val1)= map1val.at(val1)+it->second;}
						if(map1val.count(val2)>0){map1val.at(val1) = map1val.at(val2)+it->second;}
						if(!(map1val.count(val1)>0)){map1val.insert(pair<ll,ll>(val1,it->second));}
						if(!(map1val.count(val2)>0)){map1val.insert(pair<ll,ll>(val2,it->second));}
					}
					if(it->first%2!=0)
					{
						val1 = it->first/2;
						val2 =  val1;        
						if(map1val.count(val1)>0){map1val.at(val1)= map1val.at(val1)+((it->second)*2);}
						else{map1val.insert(pair<ll,ll>(val1,((it->second)*2)));}
					}
					j =  j+it->second-1;
					x  = val1;
					map1val.erase(it);
					continue;
				}
			}
			if(it->second==1)
			{
				map1val.erase(it);
			}
			if(x%2==0)
			{
				upper = x/2  ;
				nichewala = x - upper -1;
				//cout<<upper<<" hdhh "<<nichewala<<endl;
				if(map1val.count(upper)>0){ map1val.at(upper)= map1val.at(upper)+1;}
				if(map1val.count(nichewala)>0){map1val.at(nichewala)= map1val.at(nichewala)+1;}
				if(!(map1val.count(upper)>0)){map1val.insert(pair<ll,ll>(upper,1));}
				if(!(map1val.count(nichewala)>0)){map1val.insert(pair<ll,ll>(nichewala,1));}
			
			}
			if(x%2!=0)
			{

				upper = x/2 ;
				nichewala = upper;
				//cout<<upper<<" hdhh "<<nichewala<<endl;
				if(map1val.count(upper)>0){map1val.at(upper)= map1val.at(upper)+2;}
				else{map1val.insert(pair<ll,ll>(upper,2));}
			}
			if(j==v)
			{
				
				cout<<"Case #"<<k<<": "<<upper<<" "<<nichewala<<endl;
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
		undertaker(n,v,k);
	}
}
