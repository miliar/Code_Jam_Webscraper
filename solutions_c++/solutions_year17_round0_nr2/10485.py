//============================================================================
// Name        : codejam2.cpp
// Author      : Utsav Baghela
// Version     :
// Copyright   : Your copyright notice
//============================================================================

#include <iostream>
#include <string>
using namespace std;

int main() {
	freopen("B-small-attempt2.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long long int t;
	cin>>t;
	int aa=1;
	while(t--)
	{

		long long int n;
		cin>>n;

		while(n!=0)
		{

					long long int digit=0;
					long long int q=n;
					while(q!=0)
					{
					if(q/10!=0)
						digit++;
						q=q/10;
					}
					digit++;
					//cout<<"digit : "<<digit<<endl;
					long long int a[digit];
					q=n;
					for(long long int i=digit-1;i>=0;i--)
					{
						a[i]=q%10;
						q=q/10;
					}
					long long int j=0;

			for(j=0;j<digit-1;j++)
			{

			if(a[j]<=a[j+1])
			{
				continue;
			}
			else
			{
				n--;
				break;
			}

			}


			if(j==digit-1)
			{
				cout<<"Case #"<<aa<<": ";
				for(long long int i=0;i<digit;i++)
				{
					cout<<a[i];

				}
				aa++;
				cout<<endl;
				break;
			}


		}







	}
	return 0;
}
