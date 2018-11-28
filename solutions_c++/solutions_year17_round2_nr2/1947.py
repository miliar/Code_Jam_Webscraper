#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int gh=1;gh<=t;gh++)
	{
		int n;
		cin>>n;

		int arr2[6];
		char color[7] = "ROYGBV";


		for(int i=0;i<6;i++)
		{
			cin>>arr2[i];
		}

		cout<<"Case #"<<gh<<": ";

		vector<pair<int,char> > vec;
		for(int i=0;i<6;i++)
		{
			vec.push_back(make_pair(arr2[i],color[i]));
		}
		sort(vec.begin(),vec.end());
		reverse(vec.begin(),vec.end());

		int m = vec[0].first;
		string *arr = new string[m];

		for(int i=0;i<m;i++)
			arr[i] = "";

		bool ulta = false;
		for(int i=0;i<6;i++)
		{
			if(ulta)
			{
				for(int j=m-1,k=1;j>=0 && k<=vec[i].first;j--,k++)
				{
					arr[j]+=vec[i].second;
				}
			}
			else
			{
				for(int j=0,k=1;j<m && k<=vec[i].first;j++,k++)
				{
					arr[j]+=vec[i].second;
				}
			}

			ulta = !ulta;
		}

		bool proper = true;
		for(int i=0;i<m;i++)
		{
			if(arr[i].length()<=1)
			{
				proper = false;
				break;
			}
		}

		if(proper)	
		{
			for(int i=0;i<m;i++)
				cout<<arr[i];
			cout<<endl;
		}
		else
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
}