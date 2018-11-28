#include<bits/stdc++.h>
using namespace std;
#define pp pair<int,int>

class Compare
{
public:
    bool operator()(pp n1,pp n2) {
    	if (n1.second!=n2.second)
        	return n1.second<n2.second;
        else
        	return n1.first<n2.first;
    }
};

int main()
{
	int test;
	cin>>test;
	int g=1;
	while (test--)
	{
		int n,k;
		cin>>n>>k;
		cout<<"Case #"<<g<<": ";
		g++;
		int temp=1;
        int cnt=0;
        int iter=1;
        priority_queue<pp,vector<pp>,Compare>q;
		int m1,m2;
		if (n%2==0)
			q.push(pp(n/2,n/2-1));
		else
			q.push(pp(n/2,n/2));
		while (1)
		{
			pp temp=q.top();
			q.pop();
			cnt++;
			if (cnt==k)
			{
				m1=temp.first;
				m2=temp.second;
				break;
			}
			if (temp.first==temp.second)
			{
				pp p1;
				int x=temp.first;
				if (x%2==0)
				{
					q.push(pp(x/2,x/2-1));
					q.push(pp(x/2,x/2-1));
				}
				else
				{
					q.push(pp(x/2,x/2));
					q.push(pp(x/2,x/2));
				}
			}
			else
			{
				int x=temp.first;
				int y=temp.second;
				if (x%2==0)
				{
					if (x/2>y/2)
					{
						q.push(pp(x/2,x/2-1));
						q.push(pp(y/2,y/2));
					}
					else
					{
						q.push(pp(y/2,y/2));
						q.push(pp(x/2,x/2-1));
					}
				}
				else
				{
					if (y/2>x/2)
					{
						q.push(pp(y/2,y/2-1));
						q.push(pp(x/2,x/2));
					}
					else
					{
						q.push(pp(x/2,x/2));
						q.push(pp(y/2,y/2-1));
					}
				}
			}
		}
		cout<<m1<<" "<<m2<<endl;
	}
	return 0;
}