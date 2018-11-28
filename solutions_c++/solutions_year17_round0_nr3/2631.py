#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#include<utility>
#include<queue>
#include<set>
#include<iomanip>
#include<functional>
#include<fstream>
#include<string.h>
#define fnt(t) for(int in=0;in<t;in++)
#define fn(n) for(int i=0;i<n;i++)
#define fnj(n) for(int j=0;j<n;j++)
#define foo(a,b,c) for(int i=a;i<b;i+=c)
#define fo(a,b) for(int i=a;i<b;i++)
#define get(x) scanf("%d",&x)
#define getll(x) scanf("%lld",&x)
#define lli long long int
#define cin fin
#define cout fout
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\Sh\\Desktop\\C-large.in", ios::in);
	fout.open("C:\\Users\\Sh\\Desktop\\output.txt", ios::out);
	int t;
	cin>>t;
	
	fnt(t)
	{
		cout<<"Case #"<<in+1<<": ";
		lli n,k;
		cin>>n>>k;
		k-=1;
		lli seg;
		lli tot=0;
		if(!k)
		{
			cout<<max((n-1)/2,n-1-(n-1)/2)<<" ";
			cout<<min((n-1)/2,n-1-(n-1)/2)<<"\n";
		}
		
		else
		{
			lli x,y;
			lli nx=1,ny=1;
			x=min((n-1)/2,n-1-(n-1)/2);
			y=max((n-1)/2,n-1-(n-1)/2);
			seg=n;
			while(k>0)
			{
				//cout<<x<<" "<<y<<"\n";
				//cout<<nx<<" "<<ny<<"\n";
				//tot+=nx+ny;
				//cout<<k<<"\n";
				//cout<<tot<<"\n";
				if(ny>=k)
				{
					seg=y;
					break;
				}
				else if(nx+ny>=k)
				{
					seg=x;
					break;
				}
				pair <lli,lli> arr[5];
				arr[0].first=(x-1)/2;
				arr[1].first=x-1-(x-1)/2;
				arr[2].first=(y-1)/2;
				arr[3].first=y-1-(y-1)/2;
				arr[0].second=arr[1].second=nx;
				arr[2].second=arr[3].second=ny;
				sort(arr,arr+4);
				//fn(4)
				//cout<<arr[i].first<<" ";
				//cout<<"\n";
				int i=0;
				x=arr[0].first;
				k-=(nx+ny);
				nx=ny=0;
				while(arr[i].first==arr[0].first&&i<4)
				{
					nx+=arr[i].second;
					i++;
				}
				if(i==4)
				{
					x=arr[0].first;
					y=arr[0].first;
					nx=2*arr[0].second;
					ny=2*arr[3].second;
				}
				else
				{
					y=arr[i].first;
				while(i<4)
				{
					ny+=arr[i].second;
					i++;
				}
				
				}
				
				
			}
			//cout<<seg<<"\n";
			cout<<max((seg-1)/2,seg-1-(seg-1)/2)<<" "<<min((seg-1)/2,seg-1-(seg-1)/2)<<"\n";
		}
	}
}
