#include<iostream>
#include<stdio.h>
#include<string>
typedef unsigned long long ull;
typedef long long ll;

using namespace std;
int main()
{
	int t,case_num=1;
	cin>>t;

	char num[20];
	string str;
	while(t--)
	{
		ll d,n , k , s;
		double answer = 0;
		cin>>d>>n;

		while(n--)
		{
			cin>>k>>s;

			double temp = ((double)(d-k))/s;
			if(temp > answer)
				answer = temp;
		}

		printf("Case #%d: %.6f\n" , case_num++ , ((double)d)/answer);
		//cout<<"Case #"<<case_num++<<": "<<((double)d)/answer<<"\n";
	}
	return 0;
}