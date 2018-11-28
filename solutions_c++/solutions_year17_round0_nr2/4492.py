#include <iostream>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int t,i,p;
	cin >> t;
	for(p=1;p<=t;p++)
	{
		string x;
		cin >> x;
		int n=x.length();
		int arr[n];
		for(i=0;i<n;i++){arr[i]=x[i]-'0';}
		for(i=n-1;i>=1;i--)
		{
			if(arr[i]<arr[i-1])
			{
				arr[i-1]--;
				for(int j=i;j<n;j++){ arr[j]=9;}
			}
		}
		cout << "Case #" <<p<<": ";
		if(arr[0]!=0){cout<<arr[0];}
		for(int j=1;j<n;j++){cout<<arr[j];}
		cout << endl;
	}
	return 0;
}