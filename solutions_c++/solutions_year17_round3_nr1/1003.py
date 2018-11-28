#include <bits/stdc++.h>
using namespace std;


void query()
{	
	vector< pair<long long, long long> > pancake;	
	vector< long long > area;
	int n, k;
	cin >> n >> k;
	for (int i=0;i<n;i++)
	{
		int ri;
		int hi;
		cin >> ri >> hi;
		pancake.push_back(make_pair(ri,hi));		
	}	
	sort(pancake.begin(),pancake.end(),greater< pair<int,int> > () );
	area.resize((n)*(k+1),-1);
	double max_area=0;
	//cout << endl;
	for (int i=0;i<n;i++)
	{
		//cout << i << ":";
		area[i*(k+1)]=0;
		for (int j=1;j<k+1;j++)
		{			
			long long a=0;
			long long b=0;
			if (i>0)
			{	
				a=area[(i-1)*(k+1)+j];
				if (j>1)
				{
					b=area[(i-1)*(k+1)+(j-1)]+2*pancake[i].first*pancake[i].second;					
				} else
				{
					b=2*pancake[i].first*pancake[i].second+pancake[i].first*pancake[i].first;			
				}
			} else if (j==1)
			{			
				b=2*pancake[i].first*pancake[i].second+pancake[i].first*pancake[i].first;			
			}
			area[i*(k+1)+j]=max(a,b);
			//cout << max(a,b) << " ";
		}
		//cout << endl;
	}
	
	max_area=M_PI*area[(n-1)*(k+1)+k];
	
	cout << setprecision(25) << max_area << endl;
}


int main()
{	
	ios::sync_with_stdio(false);	
	int q;
	cin >> q;
	for (int i=0;i<q;i++)
	{
		cout << "Case #"<<i+1<<": ";
			query();
	}
}