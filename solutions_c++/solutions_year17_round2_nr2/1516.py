#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int it=1;
	while(it<=t)
	{
		int n,r,o,y,g,b,v,i;
		cin>>n>>r>>o>>y>>g>>b>>v;
		int a[3];//ryb

		cout<<"Case #"<<it<<": ";
		if(r>n/2 || y>n/2 || b>n/2)
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			a[0]=r;a[1]=y;a[2]=b;
			char c[3];
			c[0]='R'; c[1]='Y'; c[2]='B';
			int beg=0;
			int inbeg;
			if(b==max(r,max(y,b)))
			{
				beg=2;
			}

			if(y==max(r,max(y,b)))
			{
				beg=1;
			}

			if(r==max(r,max(y,b)))
			{
				beg=0;
			}
			inbeg=beg;

			for(i=0;i<n;i++)
			{
				a[beg]-=1;
				cout<<c[beg];
				int w,e;
				w=beg+1;e=beg+2;
				w=w%3; e=e%3;
				if(a[w]>a[e])
				{
					beg=w;
				}
				if(a[w]<a[e])
				{
					beg=e;
				}

				if(a[w]==a[e])
				{
					if(beg!=inbeg)
					beg=inbeg;
				else {beg=min(w,e);}
				}
			}
			cout<<endl;

		}
		

		it++;
	}

	return 0;
}