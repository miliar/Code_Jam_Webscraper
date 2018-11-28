//i am vengence i am the night i am Batman
//ios_base::sync_with_stdio(false);cin.tie(NULL);
#include<bits/stdc++.h>
using namespace std;

int main()
{
	long long int n,d,i,j,k,r,t;
	double x,y,min,m,l;
	cin>>t;
	
	for(i=0;i<t;i++)
	{
		cin>>d>>n;
		
		min=0;
		
		vector< vector<double> >a;
		for(j=0;j<n;j++)
		{
			vector<double> b;
			cin>>l;
			cin>>m;
			y=(d-l)/m;
			
			if(y>min)
			min=y;
			
			b.push_back(l);
			b.push_back(m);
			a.push_back(b);
		}
		
		std::cout << std::setprecision(6) << std::fixed;
		x=d/min;
		cout<<"Case #"<<i+1<<": "<<x<<"\n";
		
	}
	
    return 0;
}
