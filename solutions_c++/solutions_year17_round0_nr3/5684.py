# include <bits/stdc++.h>

using namespace std;
int min(int a,int b) { return a < b ? a : b;
}
int max(int a,int b) { return a > b ? a : b;
}
int n,a[100000],minn,maxx,x,y,p;
main()
{
	freopen("C-small-1-attempt1.in","r",stdin);
	freopen("C3.out","w",stdout);
	int ntest,k;
	cin >> ntest;
	for (int test = 1; test <= ntest; test++)
	{
		cin >> n >> k;
	
		cout << "Case #" << test << ": ";
		memset(a,0,sizeof a);
	a[0] = 1;
	a[n+1] = 1;
	for (int i=1; i<=n; i++)
	{
		maxx = -1;
		minn = -1;
		for (int j=1; j<=n; j++)
		if (a[j] == 0)
		{
			x = 0;
			y = 0;
			for (int k=j-1; k>=1; k--) if (a[k] == 0) x++; else break;
			for (int k=j+1; k<=n; k++) if (a[k] == 0) y++; else break;
			if (min(x,y) > minn)
			{
				p = j;
				minn = min(x,y);
				maxx = max(x,y);
			} else if (min(x,y) == minn)
			{
				if (max(x,y) > maxx)
				{
					p = j;
					minn = min(x,y);
					maxx = max(x,y);
				}
			}
		}
		a[p] = 1;
		if (i == k) {
			cout << maxx << " " << minn << "\n";
			break;
		}
	}
	}
	/*
	cin >> n;
	memset(a,0,sizeof a);
	a[0] = 1;
	a[n+1] = 1;
	for (int i=0; i<n; i++)
	{
		maxx = -1;
		minn = -1;
		for (int j=1; j<=n; j++)
		if (a[j] == 0)
		{
			x = 0;
			y = 0;
			for (int k=j-1; k>=1; k--) if (a[k] == 0) x++; else break;
			for (int k=j+1; k<=n; k++) if (a[k] == 0) y++; else break;
			if (min(x,y) > minn)
			{
				p = j;
				minn = min(x,y);
				maxx = max(x,y);
			} else if (min(x,y) == minn)
			{
				if (max(x,y) > maxx)
				{
					p = j;
					minn = min(x,y);
					maxx = max(x,y);
				}
			}
		}
		a[p] = 1;
		cout << i+1 << ": ";
		//for (int j=1; j<=n; j++) cout << a[j];
		cout  << " max = " << maxx << " min = " << minn << "\n";
	}*/
}
