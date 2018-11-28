#include <iostream>
#include<bits/stdc++.h>
using namespace std;




int main() {

 freopen("ins.in","r",stdin);
   freopen("outs.out","w",stdout);
	int n;
	cin>>n;


	for(int x=1;x<=n;x++)
	{
		long long int m;
		cin>>m;

		cout<<"Case #"<<x<<": ";

		if(m<9)
		cout<<m<<endl;

		else
		{
			int arr[100]={},temp=-1,set=0;

			while(m>0)
			{

				temp++;
				arr[temp]=m%10;
				m=m/10;
			//	cout<<"one......."<<arr[temp]<<endl;


			}

			for(int y=temp-1;y>=0;y--)
			{
				if(arr[y]<arr[y+1]||arr[y+1]==0)
				arr[y]=0;


			}


			for(int y=1;y<=temp;y++)
			{
			if(y>0)
				{
				//cout<<"if........"<<endl;
					if(set==1)
					{
						//cout<<"first"<<endl;
						if(arr[y]>0)
						{
							arr[y]--;
							set=0;
						}
						else
						arr[y]=9;
					}

					else if(arr[y-1]==0)
					{ //cout<<"second"<<endl;
						arr[y-1]=9;

						if(arr[y]>0)
						arr[y]--;
						else
						{
							arr[y]=9;
							set=1;
						}


					}

					else if(arr[y]>arr[y-1]||arr[y]==0)
					{
						//cout<<"third"<<endl;
						arr[y]--;
						arr[y-1]=9;
					}
				}
		   }


			for(int y=temp;y>=0;y--)
			{
				if(arr[y]>0)
				cout<<arr[y];
			}

			cout<<endl;

		}

	}

	return 0;
}
