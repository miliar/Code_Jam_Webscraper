#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> ii;
#define mp make_pair

int R,C;
char m[25][25];

int ok_ln_m(pair< char,pair<ii,ii> > c)
{
	char letter=c.first;
	ii p1=c.second.first, p2=c.second.second;
	if (p1.first-1<0) return 0;
	for (int i=p1.second;i<=p2.second;i++)
		if (m[p1.first-1][i]!='?'&&m[p1.first-1][i]!=letter)
			return 0;
	return 1;
}

int ok_ln_p(pair< char,pair<ii,ii> > c)
{
	char letter=c.first;
	ii p1=c.second.first, p2=c.second.second;
	if (p2.first+1>=R) return 0;
	for (int i=p1.second;i<=p2.second;i++)
		if (m[p2.first+1][i]!='?'&&m[p2.first+1][i]!=letter)
			return 0;
	return 1;
}

int ok_cl_m(pair< char,pair<ii,ii> > c)
{
	char letter=c.first;
	ii p1=c.second.first, p2=c.second.second;
	if (p1.second-1<0) return 0;
	for (int i=p1.first;i<=p2.first;i++)
		if (m[i][p1.second-1]!='?'&&m[i][p1.second-1]!=letter)
			return 0;
	return 1;
}

int ok_cl_p(pair< char,pair<ii,ii> > c)
{
	char letter=c.first;
	ii p1=c.second.first, p2=c.second.second;
	if (p2.second+1>=C) return 0;
	for (int i=p1.first;i<=p2.first;i++)
		if (m[i][p2.second+1]!='?'&&m[i][p2.second+1]!=letter)
			return 0;
	return 1;
}

int main()
{
	int T; cin>>T;
	for (int t=1;t<=T;t++)
	{
		cout<<"Case #"<<t<<":"<<endl;
		map< char,pair<ii,ii> > l;
		cin>>R>>C;
		for (int i=0;i<R;i++)
		{
			getchar();
			for (int j=0;j<C;j++)
			{
				cin>>m[i][j];
				if (m[i][j]=='?') continue;
				if (l.find(m[i][j])==l.end())
					l[m[i][j]]=mp(mp(i,j),mp(i,j));
				else
				{
					pair<ii,ii> p=l[m[i][j]];
					if (i<p.first.first || j<p.first.second)
						l[m[i][j]].first={min(p.first.first,i),min(p.first.second,j)};
					else if (i>p.second.first || j>p.second.second)
						l[m[i][j]].second={max(p.second.first,i),max(p.second.second,j)};
				}
			}
		}
		for (auto c:l)
		{
			for (int i=c.second.first.first;i<=c.second.second.first;i++)
				for (int j=c.second.first.second;j<=c.second.second.second;j++)
					m[i][j]=c.first;
		}
		for (auto c:l)
		{
			while (ok_ln_m(c)&&ok_cl_m(c)&&m[c.second.first.first-1][c.second.first.second-1]=='?')
			{
				for (int i=c.second.first.first-1;i<=c.second.second.first;i++)
					m[i][c.second.first.second-1]=c.first;
				for (int i=c.second.first.second-1;i<=c.second.second.second;i++)
					m[c.second.first.first-1][i]=c.first;
				c.second.first.first--; c.second.first.second--;
			}
			while (ok_ln_p(c)&&ok_cl_p(c)&&m[c.second.second.first+1][c.second.second.second+1]=='?')
			{
				for (int i=c.second.first.first;i<=c.second.second.first+1;i++)
					m[i][c.second.second.second+1]=c.first;
				for (int i=c.second.first.second;i<=c.second.second.second+1;i++)
					m[c.second.second.first+1][i]=c.first;
				c.second.second.first++; c.second.second.second++;
			}
			while (ok_ln_p(c)&&ok_cl_m(c)&&m[c.second.second.first+1][c.second.first.second-1]=='?')
			{
				for (int i=c.second.first.first;i<=c.second.second.first+1;i++)
					m[i][c.second.first.second-1]=c.first;
				for (int i=c.second.first.second-1;i<=c.second.second.second;i++)
					m[c.second.second.first+1][i]=c.first;
				c.second.second.first++; c.second.first.second--;
			}
			while (ok_ln_m(c)&&ok_cl_p(c)&&m[c.second.first.first-1][c.second.second.second+1]=='?')
			{
				for (int i=c.second.first.first-1;i<=c.second.second.first;i++)
					m[i][c.second.second.second+1]=c.first;
				for (int i=c.second.first.second;i<=c.second.second.second+1;i++)
					m[c.second.first.first-1][i]=c.first;
				c.second.first.first--; c.second.second.second++;
			}
			while (ok_ln_m(c))
			{
				for (int i=c.second.first.second;i<=c.second.second.second;i++)
					m[c.second.first.first-1][i]=c.first;
				c.second.first.first--;
			}
			while (ok_cl_m(c))
			{
				for (int i=c.second.first.first;i<=c.second.second.first;i++)
					m[i][c.second.first.second-1]=c.first;
				c.second.first.second--;
			}
			while (ok_ln_p(c))
			{
				for (int i=c.second.first.second;i<=c.second.second.second;i++)
					m[c.second.second.first+1][i]=c.first;
				c.second.second.first++;
			}
			while (ok_cl_p(c))
			{
				for (int i=c.second.first.first;i<=c.second.second.first;i++)
					m[i][c.second.second.second+1]=c.first;
				c.second.second.second++;
			}
		}
		for (int i=0;i<R;i++)
		{
			for (int j=0;j<C;j++)
				cout<<m[i][j];
			cout<<endl;
		}
	}
}