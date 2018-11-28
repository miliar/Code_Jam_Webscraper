#include <iostream>
#include<bits/stdc++.h>

using namespace std;



int main() 

{
	freopen("horses.in","r",stdin);
	freopen("horses.out","w",stdout);
	
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int d,n;
		cin>>d>>n;
		vector<pair<int,double> > start_speed(n);
		double max=0.0;
		
		for(int j=0;j<n;j++)
		{
			cin>>start_speed[j].first;
			cin>>start_speed[j].second;
			start_speed[j].second=( d-start_speed[j].first)/start_speed[j].second;
			
			if(start_speed[j].second>max)
				max= start_speed[j].second;
				
			
		}
		cout << std::fixed;
		cout << std::setprecision(6);
		cout<<"Case #"<<i<<": "<<d/max<<endl;
		
		
	
		
	}
  
	
		
		
		
		
		
		
		
		
		
		
	//	cout<<"Case #"<<i<<": "<<j<<" "<<k-arr.begin()<<endl;
	//	cerr<<"Case #"<<i<<": "<<j<<" "<<k-arr.begin()<<endl;
		
		
	
	return 0;
}
