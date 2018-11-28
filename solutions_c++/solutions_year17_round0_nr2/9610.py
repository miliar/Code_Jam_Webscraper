#include <bits/stdc++.h>
#include <fstream>
using namespace std;
typedef long long int ll;
int main() {
	cin.sync_with_stdio(false);
	ofstream myfile1;
	myfile1.open ("example.txt");
	ifstream myfile("B-large.in");
    if(myfile.is_open ())
{

	int t;
	myfile>>t;
	for(int z=1;z<=t;z++)
	{
		ll n;
		myfile>>n;
			ll p=n;

			int j=0,arr[100]={0};
			while(p>0)
			{
				arr[j]=p%10;
				p=p/10;

				j++;

			}

			for(int i=j-1;i>0;i--)
			{
				if(arr[i]>arr[i-1])
				{arr[i]--;
				for(int k=i-1;k>=0;k--)
				{
					arr[k]=9;
				}
				i=j;
				}

			}
			ll x=0;
			for(int i=j-1;i>=0;i--)
			{
				x=x*10+(arr[i]);
			}
			myfile1<<"Case #"<<z<<": "<<x<<"\n";
	}
}
	myfile.close();
	myfile1.close();
	return 0;
}
