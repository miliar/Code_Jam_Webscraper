#include<iostream>
#include<algorithm>
#include<climits>
#include<vector>

using namespace std;

int main()
{

	int t, n, k;
	int ls_find(int [], int , int );
	int rs_find(int [], int , int );	
	cin>>t;
	
	for(int i = 1; i <= t; ++i)
	{
		cin>>n>>k;
		
		int a[n];
		int ls[n];
		int rs[n];
		int min_lr[n];
		int max_lr[n];
		int pos;
		int max1, max2;
		
		vector<int> v;
		
		for(int j = 0; j < n; j++)
		{
			a[j] = 0; 
		}
		
		for(int iter = 0; iter < k; ++iter)
		{
			v.clear();
			
			for(int j = 0; j < n; ++j)
			{
				ls[j] = ls_find(a, j, n);
				rs[j] = rs_find(a, j, n);
				min_lr[j] = min(ls[j], rs[j]);
				max_lr[j] = max(ls[j], rs[j]);
				
			}
			
			/*
			cout<<"ls : ";
			for(int j = 0; j < n; ++j)
			{
				cout<<ls[j]<<" ";
			}
			
			cout<<"\nrs : ";
			for(int j = 0; j < n; ++j)
			{
				cout<<rs[j]<<" ";
			}
			cout<<"\n";
			cout<<"min_lr : ";
			for(int j = 0; j < n; ++j)
			{
				cout<<min_lr[j]<<" ";
			}
			cout<<"\n";
			cout<<"max_lr : ";
			for(int j = 0; j < n; ++j)
			{
				cout<<max_lr[j]<<" ";
			}
			cout<<"\n";
			*/
			max1 = 0;
			for(int j = 0; j < n; ++j)
			{
				if((min_lr[j] >= max1) && (a[j] != 1))
				{
					max1 = min_lr[j];

				}
			}
			
			for(int j = 0; j < n; ++j)
			{
				if((min_lr[j] == max1) && (a[j] != 1))
				{
					v.push_back(j);
					//cout<<j<<" in vector \n";
				}
			}
			
			max2 = 0;
			pos = 0;
			for(int k = v.size() - 1; k >= 0; --k)
			{
				if(max_lr[v[k]] >= max2)
				{
					max2 = max_lr[v[k]];
					//cout<<max_lr[v[k]]<<" with max2 = "<<max2<<"\n";
					pos = v[k];
				}
				
			}
			
			a[pos] = 1; 
		}
		
		cout<<"Case #"<<i<<": "<<max(ls[pos], rs[pos])<<" "<<min(ls[pos], rs[pos])<<"\n";
			
	}	
}

int ls_find(int a[], int pos, int n)
{

	
	int count = 0;
	for(int j = pos - 1; j >= 0; --j)
	{
		if(a[j] != 1)
		{
			count += 1;
				
		}
		else break;
	}	
	return count;
}

int rs_find(int a[], int pos, int n)
{
	
	int count = 0;
	for(int j = pos + 1; j < n; ++j)
	{
		if(a[j] != 1)
		{
			count += 1;
				
		}
		else break;
	}	
	return count;
}
	
