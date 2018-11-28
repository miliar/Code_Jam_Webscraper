#include<iostream>
#include<fstream>
#include<vector>
#include<math.h>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	int n,k;
	ifstream fin("C-small-1-attempt1.in");
	ofstream fout("output.txt");
	fin>>t;
	
		int counter=1;
	for(int i = 1; i <= t ; i++)
	{
		fin>>n>>k;
		
		
		n=n+2;
		vector<int>vc(n,0);
		vc[0]=1;
		int lindex=0;
		int rindex=vc.size()-1;
		vc[vc.size()-1]=1;
		int total=(rindex+1)-(lindex+1);
		double mid=floor (total/2);
	//	cout<<mid<<endl;
		vc[mid]=1;
		//cout<<vc.size();
		int ls;
		int rs;	
			for(int j = 1; j < k ; j++)
	{
		
			//cout<<"now";
			int last = vc.size()-1;
			double max=-1;
			for(int inner = vc.size()-2;inner>=0;inner--)
			{
				if(vc[inner]==1)
				{
					if(distance(vc.begin()+inner+1,vc.begin()+last)>max)
					{
						max=distance(vc.begin()+inner+1,vc.begin()+last);
						lindex=inner;
						rindex=last;
						
					//	cout<<max<<endl;
						//cout<<last<<endl;
					}
					last=inner;
						
				}
			}
	//	cout<<max<<endl;
		
		 mid=lindex + ceil (max/2);
			
		 
		 //cout<<lindex<<endl;
		vc[mid]=1;
			
		
	
	//	cout<<ls<<" "<<rs<<endl;
			for(int in=0;in<vc.size();in++)
	{
		//cout<<vc[in];
	}
//	cout<<endl;
	}
	
	//cout<<rindex<<" "<<lindex<<" "<<mid<<endl;
		ls=distance(vc.begin()+lindex+1,vc.begin()+mid);
		rs=distance(vc.begin()+mid+1,vc.begin()+rindex);
		
		int lar,small;
		
		if(ls>rs)
		{
			lar=ls;
			small=rs;
		}
		else
		{
			lar=rs;
			small=ls;
		}
		fout<<"Case #"<<i<<": "<<lar<<" "<<small<<endl;
                
	
	
	
}
	
}
