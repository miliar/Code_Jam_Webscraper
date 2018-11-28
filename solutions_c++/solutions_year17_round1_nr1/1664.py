#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n, m;
	int  k, p;
	cin>>n>>m>>k;
	int arr[1000];
	for(int i = 1; i<=n; i++)cin>>arr[i];
	p = n + 1;
	int i;
	for(i = 1; i<=n; i++)
		if(arr[i]<=k && abs(m - i)<p && arr[i]!=0)
			p = abs(m - i);
	cout<<p*10<<endl;
	return 0;
}
