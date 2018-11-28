#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("testcase.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	long long int N,K,a,b;
	 
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		priority_queue<long long int> L,R;
		cin>>N>>K;
		L.push(N);
		for(int i=0;i<K;i++)
		{
			long long int X=L.top();
			L.pop();
			if(X%2==0)
			{
				a=X/2;
				b=X/2 - 1;
				L.push(a);
				L.push(b);
			}
			
			else
			{
				a=X/2;
				b=X/2;
				L.push(a);
				L.push(b);
			}
		}
		
		cout<<"Case #"<<t<<": "<<a;
		cout<<" "<<b<<endl;
	} 
}
