#include<bits/stdc++.h>
using namespace std;
long long int a,b,x,y,n,m,t,p,q;
struct f{
	int l,r,d;
	f(){	}
	f(int a,int b)
	{
		l = a , d = b , r = l + d - 1;
	}
};
struct comp {
    bool operator() (f a, f b) const
	{
    if(a.d > b.d)
		return true;
	if(a.d < b.d)
		return false;
	return a.l < b.l;    
    }
};
set<f,comp> second;
set<f,comp>::iterator it;
	
void disp()
{
	for(it = second.begin();it!=second.end();it++)
		cout<<it->l<<" "<<it->r<<" "<<it->d,cout<<"\n";
}
int main()
{
   freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("op.txt", "w", stdout);
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    x=1;
    int lf,rr,dd,r2,r1=-1,l2,l1=-1;
	int tes; cin >> tes; while( tes-- > 0 )
	{
		second.clear();
		cin>>n>>m;
		if(n==m)
			l1 = 0 , r1 = 0;
		else
		{
		second.insert(f(0,n));	
		
		
		while(m--)
		{
			it = second.begin();
			lf = it->l; rr = it->r; dd = it->d;
			second.erase(second.begin());
			if(dd&1)
			{
				r2 = lf + (dd/2) -1;
				second.insert(f(lf,dd/2));
				second.insert(f(r2+2,dd/2));
				if(m==0)
					l1= dd/2,r1 = dd/2;
			}
			else
			{
				r2 = lf + (dd/2) -1;
				second.insert(f(lf,(dd/2)-1));
				second.insert(f(r2+1,dd/2));
				if(m==0)
					l1= dd/2-1,r1 = dd/2;
			}
		}
		
		}
	cout<<"Case #"<<x++<<": "<<max(l1,r1)<<" "<<min(l1,r1)<<"\n";
	}
}
