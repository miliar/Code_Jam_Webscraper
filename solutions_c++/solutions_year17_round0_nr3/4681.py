#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen ("C-small-2-attempt0.in","r",stdin);
	freopen ("Cout1.txt","w",stdout);
	int t;
	cin>>t;
	int t1=1;
	while(t--)
	{
		long long n,k;
		bool fl=true;
		cin>>n>>k;
		{
			priority_queue<long long>q;
		q.push(n);
		long long x,y;
		while(!q.empty())
		{

			long long p=q.top();
			q.pop();
			if(p%2==0)
			{
				p--;
				x = p/2+p%2;
				y = p/2;
				if(x!=0)
                    q.push(x);
                if(y!=0)
                    q.push(y);
				k--;
				if(k==0)
				{
					fl=false;
					break;
				}
			}
			else
			{
				p--;
				x = p/2;
				y = p/2;
				if(x!=0)
                    q.push(x);
                if(y!=0)
                    q.push(y);
				k--;
				if(k==0)
				{
					fl=false;
					break;
				}
			}
		}
		cout<<"Case #"<<t1<<": ";
		t1++;
		if(!fl)
		cout<<max(x,y)<<" "<<min(x,y)<<endl;
		else cout<<"0"<<" 0"<<endl;
		}
	}
	return 0;
}
