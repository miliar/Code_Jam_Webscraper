#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;


long long solve(long long s1)
{
		string n=to_string(s1);
		long long solution=n[0]-'0';
			bool flag=false;
			for (int i=1;i<n.size();i++)
			{
				
				if (flag) 
					solution=solution*10+9;	
				else if (n[i]<n[i-1])
				{
					solution=solve(solution-1)*10+9;
					flag=true;
				}
				else if (!flag)
					solution=solution*10+n[i]-'0';
				
			}

	return solution;
}
int main()
{
	
	int n;
	cin>>n;
	for (int t=1;t<=n;t++)
	{
		long long n;
		cin>>n;

		cout<<"Case #"<<t<<": ";
		if(n<10)
			cout<<n<<endl;
		else
		{
					
			cout<<solve(n)<<endl;

		}
	}
	
	return 0;
}
