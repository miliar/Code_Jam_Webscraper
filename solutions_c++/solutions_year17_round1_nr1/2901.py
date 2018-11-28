#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
using namespace std;
void getAns(char **arr,int r,int c)
{
	std::map<char,int> temp;
	int i,j;
	bool zero = false;
	vector<int> nf;
	for(i=0;i<r;i++)
	{
		j=0;
		char wow=' ';
		bool found=false;
		while(j<c)
		{
			
			if(arr[i][j]!='?' && !found)
			{
				temp[arr[i][j]]=1;
				wow=arr[i][j];
				found=true;
				j=0;
			}
			else if(found)
			{
				int count = 1;
				while(j<c)
				{
					if(arr[i][j]=='?')
					{
						count++;
						arr[i][j]=wow;
					}
					else
					{
						wow=arr[i][j];
					}
					j++;
				}
			}
			else
			{
				j++;
			}
		}
		if(!found)
		{
			nf.push_back(i);
		}
	}
	while(nf.size()!=0)
	{
		i=nf.back();	
		if(i==0)
		{
			nf.pop_back();
			if(nf.back()!=1)
				arr[i] = arr[i+1];
			else
			{
				int last = nf.size()-1;
				int k =2;
				while(strcmp(arr[0],arr[k])==0)
					k++;
				arr[i] = arr[k];
			}
		}
		else
		{
			//cout << i <<"\n";
			nf.pop_back();
			//cout<< i-1 << ":" << nf.back() <<"\n";
			if(i-1!=nf.back())
			{
				//cout << "Here" << i <<"\n";
				arr[i]=arr[i-1];
			}
			else
			{
				//cout << "Here1 " << i <<"\n";
				int l = nf.back();
				//cout << "l:" <<l << "\n";
				while(strcmp(arr[l],arr[i])==0)
				{
					//cout<< i << ":" << l <<"\n";
					//cout << l << " ";
					if(l-1<0)
						l=r-1;
					else
						l=(l-1);
					//cout<< i << ":" << l <<"\n";
					
				}
				//cout << l;
				arr[i] = arr[l]; 
			}
		}
	}
}

int main()
{
	int j,t;
	cin>>t;
	for(j=0;j<t;j++)
	{
		int r,c,i;
		cin >> r;
		cin >> c;
		char **arr = ((char **)malloc(r * sizeof(char *))); 
		for(i=0;i<r;i++)
		{	
			arr[i]=(char *)malloc(c * sizeof(double));
		}
		for(i=0;i<r;i++)
		{	
			cin >> arr[i];
		}
		getAns(arr,r,c);
		cout<<"Case #"<<(j+1)<<":"<<"\n";
		for(i=0;i<r;i++)
			cout << arr[i]<<"\n";
	}
	return 0;
}
