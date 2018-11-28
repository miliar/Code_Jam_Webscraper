#include <bits/stdc++.h>
using namespace std;

int t,r,c;
string s;


int main()
{
	int caso=1;
	scanf("%d",&t);
	while(t--)
	{
		vector<string> v;
		scanf("%d%d",&r,&c);

		for(int i=0;i<r;i++)
		{
			cin >> s;
			v.push_back(s);
		}
		for(int i=0;i<r;i++) for(int j=c-1;j>0;j--) if(v[i][j]!='?' and v[i][j-1]=='?') v[i][j-1]=v[i][j];
		for(int i=0;i<r;i++) for(int j=0;j<c-1;j++) if(v[i][j]!='?' and v[i][j+1]=='?') v[i][j+1]=v[i][j];
		for(int i=r-1;i>0;i--) for(int j=0;j<c;j++) if(v[i][j]!='?' and v[i-1][j]=='?') v[i-1][j]=v[i][j];
		for(int i=0;i<r-1;i++) for(int j=0;j<c;j++) if(v[i][j]!='?' and v[i+1][j]=='?') v[i+1][j]=v[i][j];
		
		printf("Case #%d:\n",caso);

		for(int i=0;i<r;i++)
		{
			cout << v[i] << endl;
		}
		caso++;
	}
}