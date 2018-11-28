#include <bits/stdc++.h>
using namespace std;
#define rep(a,b,c) for(int a=b;a<c;++a)
#define repeq(a,b,c) for(int a=b;a<=c;++a)
#define debug(x) cerr<<(#x)<<": "<<x<<endl
typedef long long ll;
bool pg[300][300], tg[300][300], addp[300][300], addt[300][300];
bool tkrow[300], tkcol[300], tkdiag1[300], tkdiag2[300];
int main()
{
	ios::sync_with_stdio(false);
    cin.tie(NULL);
	int T;
	cin >> T;
	repeq(t,1,T)
	{
		int n, m;
		cin >> n >> m;
		rep(i,0,n)rep(j,0,n)
		{
			pg[i][j]=false, tg[i][j]=false;
			addp[i][j]=false, addt[i][j]=false;
		}
		rep(p,0,m)
		{
			int i, j;
			char type;
			cin >> type >> i >> j;
			--i, --j;
			if(type=='+' || type=='o')
				pg[i][j]=true;
			if(type=='x' || type=='o')
				tg[i][j]=true;
		}
		rep(i,0,n)
			tkrow[i] = false, tkcol[i] = false;
		rep(i,0,n)rep(j,0,n)
			if(tg[i][j])
				tkrow[i]=true, tkcol[j]=true;
		rep(i,0,n)
		    for(int j=0;j<n && !tkrow[i];++j)
				if(!tkcol[j])
				{
					addt[i][j]=true;
					tkrow[i]=true, tkcol[j]=true;
				}
		rep(i,0,2*n-1)
			tkdiag1[i] = false, tkdiag2[i] = false;
		rep(i,0,n)rep(j,0,n)
			if(pg[i][j])
				tkdiag1[i+j]=true, tkdiag2[i+n-1-j]=true;
		rep(sum,0,n)
		    for(int i=0;i<=sum;++i)
			{
				if(!tkdiag1[sum])
				{
					int j = sum-i;
					if(!tkdiag2[i+n-1-j])
					{
						addp[i][j]=true;
						tkdiag1[sum]=true, tkdiag2[i+n-1-j]=true;
					}
				}
				if(2*n-2-sum!=sum && !tkdiag1[2*n-2-sum])
				{
					int j = sum-i;
					i = n-1-i, j = n-1-j;
					if(!tkdiag2[i+n-1-j])
					{
						addp[i][j]=true;
						tkdiag1[2*n-2-sum]=true, tkdiag2[i+n-1-j]=true;
					}
				}
			}					
		int y=0, z=0;
		rep(i,0,n)rep(j,0,n)
		{
			if(addp[i][j]||addt[i][j])
				++z;
			if(tg[i][j] || addt[i][j])
				++y;
			if(pg[i][j] || addp[i][j])
				++y;
		}
		cout << "Case #" << t << ": " << y << " "<< z << endl;
		rep(i,0,n)rep(j,0,n)
			if(addp[i][j]||addt[i][j])
			{
				if((addp[i][j]||pg[i][j])&&(addt[i][j]||tg[i][j]))
					cout << "o "<< i+1<< " "<<j+1<<endl;
				else if(addp[i][j])
					cout << "+ "<< i+1<< " "<<j+1<<endl;
				else if(addt[i][j])
					cout << "x "<< i+1<< " "<<j+1<<endl;
			}
	}
	return 0;
}
