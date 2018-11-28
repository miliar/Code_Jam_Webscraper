#include <bits/stdc++.h>
using namespace std;

string s;
int caso,t,r,c,lin,col;


int main()
{
	scanf("%d",&t);
	while(caso<t)
	{
		vector<string> v;
		scanf("%d%d",&r,&c);

		for(int i=0;i<r;i++)
		{
			cin >> s;
			v.push_back(s);
		}
		for(int i=0;i<r;i++) for(int j=0;j<c-1;j++) if(v[i][j]!='?' and v[i][j+1]=='?') v[i][j+1]=v[i][j];
		for(int i=0;i<r;i++) for(int j=c-1;j>0;j--) if(v[i][j]!='?' and v[i][j-1]=='?') v[i][j-1]=v[i][j];
		for(int i=0;i<r-1;i++) for(int j=0;j<c;j++) if(v[i][j]!='?' and v[i+1][j]=='?') v[i+1][j]=v[i][j];
		for(int i=r-1;i>0;i--) for(int j=0;j<c;j++) if(v[i][j]!='?' and v[i-1][j]=='?') v[i-1][j]=v[i][j];
		
		printf("Case #%d:\n",caso+1);

		for(int i=0;i<r;i++)
		{
			cout << v[i] << endl;
		}

		caso++;
	}
}