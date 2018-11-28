#include<bits/stdc++.h>
#define ull long long 
using namespace std;

int main()
{
	freopen("output.txt", "w", stdout);
	ifstream fin;
	fin.open ("input.txt");
	
	int t;
	fin>>t;
	map<ull, ull, greater<ull> > :: iterator itr,prev_itr;
	//cin>>t;
	int l=1;
	while(l<=t)
	{
		ull n,k,temp1,temp2;
		fin>>n>>k;
		
		map<ull, ull, greater<ull> > arr;
		
		temp1 = n;
		temp2 = n;
		
		int i = 0;
		
		arr.insert(pair<ull, ull>(n,1));
		
		while(temp1>0)
		{
			ull prev_temp1 = temp1;
			ull prev_temp2 = temp2;
			
			temp1 = prev_temp1 / 2;
			arr.insert(pair<ull, ull>(temp1,arr[prev_temp1]));
			
			int rem = prev_temp1 % 2;
			if(rem == 0)
			{
				temp2 = temp1 - 1;	
				if(temp1 == 0 )
					temp2 = 0;
			}
			else temp2 = temp1;
			itr = arr.find(temp2);
			if(itr==arr.end())
				arr.insert(pair<ull, ull>(temp2,arr[prev_temp1]));
			else arr[itr->first] = arr[itr->first] + arr[prev_temp1];
			
			ull temp = temp1;
			
			if(prev_temp1!=prev_temp2)
			{
				temp1 = prev_temp2 / 2;
				itr = arr.find(temp1);
				if(itr==arr.end())
					arr.insert(pair<ull, ull>(temp1,arr[prev_temp2]));
				else arr[itr->first] = arr[itr->first] + arr[prev_temp2];
				
				int rem = prev_temp2 % 2;
				if(rem == 0)
				{
					temp2 = temp1 - 1;	
					if(temp1 == 0 )
						temp2 = 0;
				}
				else temp2 = temp1;
				map<ull, ull> :: iterator itr;
				itr = arr.find(temp2);
				if(itr==arr.end())
					arr.insert(pair<ull, ull>(temp2,arr[prev_temp2]));
				else arr[itr->first] = arr[itr->first] + arr[prev_temp2];
				
				temp1 = temp;
			}
		}
		
		cout<<"Case #"<<l<<": ";
		{
			itr = arr.begin();
			while(k>1)
			{
				ull prev_k = k;
				k = k - itr->second;
				prev_itr = itr;
				itr++;
				if(itr == arr.end())
					break;
			}
			ull max, min;
			if(itr == arr.end())
			{
				max = min = 0;
			}
			if(k==1)
			{
				max = itr->first/2;
				if(itr->first%2 == 0)
					min = max - 1;
				else min = max;
				if(max == 0)
					min = 0;
			}
			else
			{
				max = prev_itr->first/2;
				if(prev_itr->first%2 == 0)
					min = max - 1;
				else min = max;
				if(max == 0)
					min = 0;
			}
			cout<<max<<" "<<min<<endl;
		}
		
		l++;
		/*
		for(itr = arr.begin();itr!=arr.end();itr++)
		{
			cout  <<  '\t' << itr->first<<  '\t' << itr->second << '\n';
		}*/
	}
}
