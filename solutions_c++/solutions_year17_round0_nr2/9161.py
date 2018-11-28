#include <bits/stdc++.h>
using namespace std;

void solve()
{
	int num;
	cin>>num;
	int no;
	no=num;
	int count=0;
	int dec1=10,div1=1,dec2=dec1*10,div2=div1*10;
	while(no>0)
	{
		no=no/10;
		count++;
	}
	while(num>0)
	{
		
		if(((num%dec1)/div1)>=((num%dec2)/div2))
		{	
			dec1=dec1*10;
			dec2=dec2*10;
			div1=div1*10;
			div2=div2*10;
			count--;
			if(count==0)
			{
				cout<< num <<"\n";
				break;
			}
		}
		else
			num=num-1;
	}
	
}
int main()
{
	int tc;
	cin >> tc;
	for(int i=0;i<tc;i++)
	{
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}