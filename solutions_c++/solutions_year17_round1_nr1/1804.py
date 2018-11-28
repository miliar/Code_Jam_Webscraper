#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define pi pair<int,int>
#define pll pair<ll,ll>
#define vl vector< ll >
#define bug(a) cout<<a<<endl;
#define bug2(a,b) cout<<a<<" "<<b<<endl;
#define bug3(a,b,c) cout<<a<<" "<<b<<" "<<c<<endl;
using namespace std;
int main()
{
	int test;
	scanf("%d",&test);
	char a[30][30];
	char res[30][30];
	ofstream out("out.txt");
	for(int t=1;t<=test;t++)
	{
		int r,c;
		scanf("%d%d",&r,&c);
		for(int i=0;i<r;i++)
		{
			scanf("%s",a[i]);
		}
		queue< pair<int,int> > q;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(a[i][j]!='?')
					q.push(pi(i,j));
			}
		}
		queue< pi > qi;
		while(!q.empty())
		{
			int i=q.front().first;
			int j=q.front().second;
			char val=a[i][j];
			qi.push(pi(i,j));
			for(int cj=j-1;cj>=0 && a[i][cj]=='?';cj--)
			{
				qi.push(pi(i,cj));
				a[i][cj]=val;
			}
			for(int cj=j+1;cj<c && a[i][cj]=='?';cj++)
			{
				qi.push(pi(i,cj));
				a[i][cj]=val;
			}
			q.pop();
		}
		while(!qi.empty())
		{
			int i=qi.front().first;
			int j=qi.front().second;
			char val=a[i][j];
			for(int ci=i-1;ci>=0&&a[ci][j]=='?';ci--)
				a[ci][j]=val;
			for(int ci=i+1;ci<r&&a[ci][j]=='?';ci++)
				a[ci][j]=val;
			qi.pop();
		}
		out<<"Case #"<<t<<":"<<endl;
		for(int i=0;i<r;i++)
			out<<a[i]<<endl;
	}
	return 0;
}


