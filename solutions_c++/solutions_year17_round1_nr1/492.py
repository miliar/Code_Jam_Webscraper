#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;

char buffer[30][30];
int label[30][30];
int dp[30][30];

int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};

int main()
{
	int t;
	cin >> t;

	for(int cn=1; cn<=t; cn++)
	{
		int r,c;
		cin >> r >> c;

		for(int i=0; i<r; i++)
			cin >> buffer[i];

		for(int i=0; i<r; i++)
		{
			dp[i][0] = buffer[i][0]!='?';
			for(int j=1; j<c; j++)
				dp[i][j] = dp[i][j-1]+(buffer[i][j]!='?');
		}

		for(int i=1; i<r; i++)
			for(int j=0; j<c; j++)
				dp[i][j] += dp[i-1][j];

		deque<ii> rdiv;
		int last = 0;
		int lastpos = -1;
		for(int i=0; i<r-1; i++)
			if(dp[i][c-1]-last>0 && dp[r-1][c-1]-dp[i][c-1]>0)
			{
				rdiv.push_back(ii(lastpos+1,i));
				last = dp[i][c-1];
				lastpos = i;
			}
		rdiv.push_back(ii(lastpos+1,r-1));

		int label_cnt = 0;

		for(int i=0; i<rdiv.size(); i++)
		{
			last = 0;
			lastpos = -1;

			int a = rdiv[i].first;
			int b = rdiv[i].second;
			for(int j=0; j<c-1; j++)
			{
				int temp = dp[b][j]-(a==0?0:dp[a-1][j]);
				if(temp-last>0 && dp[b][c-1]-(a==0?0:dp[a-1][c-1])-temp>0)
				{
					for(int x=a; x<=b; x++)
						for(int y=lastpos+1; y<=j; y++)
							label[x][y] = label_cnt;
					label_cnt++;

					last = temp;
					lastpos = j;
				}
			}

			for(int x=a; x<=b; x++)
				for(int y=lastpos+1; y<=c-1; y++)
					label[x][y] = label_cnt;
			label_cnt++;
		}

		for(int i=0; i<r; i++)
			for(int j=0; j<c; j++)
				if(buffer[i][j]!='?')
				{
					char ch = buffer[i][j];
					int lb = label[i][j];

					deque<ii> dq(1,ii(i,j));

					while(dq.size())
					{
						ii pos = dq.front();
						dq.pop_front();

						for(int i=0; i<4; i++)
						{
							int nx = pos.first+dx[i];
							int ny = pos.second+dy[i];

							if(nx<0 || nx==r || ny<0 || ny==c || label[nx][ny]!=lb || buffer[nx][ny]!='?')
								continue;
							buffer[nx][ny] = ch;
							dq.push_back(ii(nx,ny));
						}
					}
				}

		cout << "Case #" << cn << ":" << endl;
		for(int i=0; i<r; i++)
			cout << buffer[i] << endl;

	}
}