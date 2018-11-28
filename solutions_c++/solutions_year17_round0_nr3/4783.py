#include<bits/stdc++.h>
using namespace std;


struct stall{
	int l,r,d;
	stall(){	}
	stall(int a,int b)
	{
		l = a , d = b , r = l + d - 1;
	}
};
struct comp {
    bool operator() (stall a, stall b) const
	{
    if(a.d > b.d)
		return true;
	if(a.d < b.d)
		return false;
	return a.l < b.l;    
    }
};
set<stall,comp> second;
set<stall,comp>::iterator it;
	
int main()
{
	
    freopen("inp21.txt", "r", stdin);
    freopen("op21.txt", "w", stdout);
    long long int a,b,i,y,n,m,t,p,q;
    i=1;
    int lf,rr,dd,r2,r1=-1,l2,l1=-1;
	int t1;
    cin >> t1; 
	for(i=1;i<=t1;i++)
	{
		second.clear();
		cin>>n>>m;
		if(n==m)
			l1 = 0 , r1 = 0;
		else
		{
		second.insert(stall(0,n));	
		
		
		while(m--)
		{
			it = second.begin();
			lf = it->l; rr = it->r; dd = it->d;
			second.erase(second.begin());
			if(dd&1)
			{
				r2 = lf + (dd/2) -1;
				second.insert(stall(lf,dd/2));
				second.insert(stall(r2+2,dd/2));
				if(m==0)
					l1= dd/2,r1 = dd/2;
			}
			else
			{
				r2 = lf + (dd/2) -1;
				second.insert(stall(lf,(dd/2)-1));
				second.insert(stall(r2+1,dd/2));
				if(m==0)
					l1= dd/2-1,r1 = dd/2;
			}
		}
		
		}
	cout<<"Case #"<<i<<": "<<max(l1,r1)<<" "<<min(l1,r1)<<"\n";
	}
}
