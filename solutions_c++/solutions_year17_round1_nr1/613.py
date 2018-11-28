#include <bits/stdc++.h>
using namespace std;
#define rep(a,b,c) for(int a=b;a<c;++a)
#define repeq(a,b,c) for(int a=b;a<=c;++a)
#define debug(x) cerr<<(#x)<<": "<<x<<endl
typedef long long ll;
const int SZ = 50;
char grid[SZ][SZ];
int main()
{
	ios::sync_with_stdio(false);
    cin.tie(NULL);
	int T;
	cin >> T;

	repeq(testcase,1,T)
	{
		int firstRow = -1;
		int R, C;
		cin >> R >> C;
		string s;
		bool empty[SZ];
		rep(i,0,R)
		{
			empty[i] = true;
			cin >> s;
			rep(j,0,C)
			{
				grid[i][j] = s[j];
				if(s[j]!='?')
					empty[i]=false;
			}
			if(!empty[i] && firstRow==-1)
				firstRow = i;
		}
		rep(i,0,R)
			if(!empty[i])
			{
				int first = -1;
				rep(j,0,C)
					if(first==-1 && grid[i][j]!='?')
						first = j;
				rep(j,0,C)
					if(j<first)
						grid[i][j]=grid[i][first];
					else if(grid[i][j]=='?')
						grid[i][j]=grid[i][j-1];				
			}
		rep(i,0,R)
			if(empty[i])
			{
				if(i<firstRow)
					rep(j,0,C)
						grid[i][j]=grid[firstRow][j];
				else
					rep(j,0,C)
						grid[i][j]=grid[i-1][j];
			}
		printf("Case #%d: \n",testcase);
		rep(i,0,R)
		{
			rep(j,0,C)
				printf("%c",grid[i][j]);
			printf("\n");
		}
	}
	return 0;
}
