#include<bits/stdc++.h>
using namespace std;
int main(){
	long  t,a1=0;
	cin>>t;
	while(a1<t)
	{
		long  n,k,l,m;
		cin>>n>>k;	
		a1++;
		priority_queue <long > q;
		q.push(n);
		for(long  i=0;i<k-1;i++)
		{
			l=q.top();
			q.pop();

			q.push(l/2);
			if(l%2)
				q.push(l/2);
			else if(l/2)
				q.push(l/2-1);
			else q.push(0);

			
		}
		m=q.top();
		l=m/2;
		if(m%2)
			m=m/2;
		else if(m/2)
			m=m/2 -1;
		else
			m=0;		
		cout<<"CASE #"<<a1<<": "<<l<<" "<<m<<endl;

	}
	
	return 0;
}
