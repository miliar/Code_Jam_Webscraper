#include<iostream>
#include<queue>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	ifstream fin("C-small-2-attempt1.doc",ios::in);
	ofstream fout("b9.txt",ios::out);
	int t;
	char ch;
	fin>>t;
	fin.get(ch);
	int w=1;
	while(t--)
	{
		long long int n,k;
		fin>>n>>k;
		fin.get(ch);
	//	vector<long long int>v;

		//queue<long long int>q;
		n=n+1;
		
		
		//q.push(n);
		long long int x;
		long long int a;
		long long int left,right;
		//v.push_back(n);
		//int flag=1;
		long long int y=0;
		long long int t=0;
		long long int f=0;
		vector<long long int>arr(n+1);
		vector<long long int> v(n+1);
		fill(v.begin(),v.end(),0);
		v[n]=1;
		arr[0]=0;
		arr[1]=0;
		long long int h=n;
		int flag=0;
		long long int b=0;
		for(long long int i=0;i<k;i++)
		{
			if(v[h]>0)
			{
				x=h;
				v[h]--;
			}
		else if(v[h]==0)
			{

				h=arr[b];
				x=h;
				b++;
				v[h]--;
			}
		//cout<<x<<endl;
			a=x/2;
			left=a-0;
			right=x-a;
		//cout<<right<<" "<<left<<endl;
		v[left]++;
		v[right]++;
		//cout<<"v"<<v[7]<<endl;
		if(right>left)
		{
			flag=0;
			long long int a=f-2;
			if(a<0)
				a=0;
			for(a;a<f;a++)
			{
				if(arr[a]==right)
				{
					flag=1;
					break;
				}

			}

			if(flag==0)
					arr[f++]=right;
			flag=1;
			a=f-2;
			if(a<0)
				a=0;
			for(a;a<f;a++)
			{
				if(arr[a]==left)
				{
					flag=0;
					break;
				}

			}
			if(flag==1)
			{
				arr[f++]=left;
			}

		}
		else
		{
			flag=1;
			long long int a=f-2;
			if(a<0)
				a=0;
			for(a;a<f;a++)
			{
				if(arr[a]==left)
				{
					flag=0;
					break;
				}

			}
			if(flag==1)
			{
				arr[f++]=left;
			}
			flag=0;
			a=f-3;
			if(a<0)
				a=0;
			for(a;a<f;a++)
			{
				if(arr[a]==right)
				{
					flag=1;
					break;
				}

			}
			if(flag==0)
				arr[f++]=right;
		}

		}
		left=left-1;
		right=right-1;
		fout<< "Case #" << w << ": " ;
		fout<<max(right,left)<<" "<<min(right,left)<<endl;
		w++;
	}
}