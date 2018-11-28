#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	int test;
	cin>>test;
	int k =0;
	while(test--)
	{
		k++;
		ll num;
	cin>>num;
	cout<<"Case #"<<k<<": ";
	ll temp = num;
	int cur;
	int prev = 10;
	int point = -1;
	int d_count = 0;
	int arr[50];
	while(temp>0)
	{
		cur = temp%10;
		arr[d_count] = cur;
		if(cur>prev)
		{
			point = d_count;
			prev = cur-1;
		}
		else
		prev = cur;
		d_count++;
		temp /= 10;
	}
	if(point==-1)
		cout<<num<<endl;
	else
	{
		if(point==d_count-1 && arr[d_count-1]==1)
		{
			for(int i = 0;i<d_count-1;i++)
				cout<<"9";
			cout<<endl;
		}
		else
		{
			for(int i =d_count-1;i>point;i--)
				cout<<arr[i];
			cout<<arr[point]-1;
			for(int i=point-1;i>=0;i--)
				cout<<"9";
			cout<<endl;
		}

	}
	}
	

}
