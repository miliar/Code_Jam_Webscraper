#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("Input.txt","r",stdin);
	freopen("Output.txt","w",stdout);
	int t,k=1;
	cin>>t;
	while(t--)
	{
		int r,c;
		cin>>r>>c;
		char arr[30][30]={0};
		for(int i=0;i<r;i++)
			cin>>arr[i];

		for(int i=0;i<r;i++)
		{
			int last_filled=-1;
			for(int j=0;j<c;j++)
			{
				if(arr[i][j]!='?')
					{last_filled=j;}
				else
				{
					if(last_filled==-1)
					{
						int flag=-1;
						for(int k=j+1;k<c;k++)
						{
							if(arr[i][k]!='?')
							{
								flag=k;
								break;
							}
						}
						if(flag!=-1)
						{
							for(int k=j;k<=flag;k++)
								arr[i][k]=arr[i][flag];
							last_filled=flag;
						}
						else
						{
							for(int k=j;k<c;k++)
								arr[i][k]=arr[i-1][k];
						}
					}
					else
					{
						arr[i][j]=arr[i][last_filled];
						last_filled=j;
					}
				}
			}
		}
		cout<<"Case #"<<k++<<":"<<endl;
		//cout<<r<<" "<<c<<endl;
		for(int i=0;i<r;i++)
				if(strlen(arr[i])==0)
				{
					for(int j=i+1;j<r;j++)
					{
						if(strlen(arr[j])==c)
							{
								cout<<arr[j]<<endl;
								break;
							}
					}
				}
				else
					cout<<arr[i]<<endl;
	}
	return 0;
}