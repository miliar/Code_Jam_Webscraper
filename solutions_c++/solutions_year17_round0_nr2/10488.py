#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,k=0;
	cin>>t;
	while(t--)
	{
		long long int n, y, x, i,flag;
		vector<long long int> arr;
		cin>>n;
		k++;
		while(1)
		{
			y=n;
			i=0;
			flag=0;
			while(y!=0)
			{
				//arr[i]=y%10;
				arr.insert(arr.begin()+i,y%10);
				y=y/10;
				//cout<<arr[i]<<endl;
                if(arr[i]>arr[i-1]&&i!=0)
                {
                	flag=1;
                	break;
                }
                i++;
			}
			if(flag==1)
				n=n-1;
			else
				break;
		}
		cout<<"Case #"<<k<<": "<<n<<endl;
	}
}