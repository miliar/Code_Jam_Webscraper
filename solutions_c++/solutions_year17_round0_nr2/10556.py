#include<iostream>
#include<stdio.h>
using namespace std;
unsigned long long n, temp;
int main()
{
	int t, t1, t2;
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
	cin>>t;
	for(int i=0; i<t; i++)
	{
		cin>>n;
		int flag = 1;
		for(temp = n; temp > 0;temp = --n)
		{
			flag = 1;
			while(flag == 1 && temp)
			{
				t1 = temp % 10;
				t2 = (temp/10) % 10;
		//		cout<<"t1: "<<t1;
			//	cout<<"t2: "<<t2;
				if(t2 > t1)
				{
					flag = 0;
					break;
				}
				else
				{
					temp/= 10;
				}
			}
	//		cout<<n<<" ";
			if(flag == 1)
            {
				cout<<"Case #"<<i+1<<": "<<n<<"\n";
				break;
            }
		}
	}
}


