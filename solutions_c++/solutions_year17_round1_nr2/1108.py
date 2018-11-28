#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <ctime>
#include <random>
#include <climits>
#include <queue>
#include <numeric>
#include <thread>
using namespace std;
#define MAXN 100
#define MAXP 100
int Ni[MAXN];
int NP[MAXN][MAXP];
int DATA[MAXN][MAXP];
bool canExpand(vector<vector<int> >&resnet, int s, int t, int n, vector<int> &pre)
{
	queue<int> que;
	vector<bool> visited(n + 1, false);
	que.push(s);
	visited[s] = true;
	int front;
	while (!que.empty())
	{
		front = que.front();
		que.pop();
		for (int i = 0; i < n; i++)
		{
			if (!visited[i] && resnet[front][i] > 0)
			{
				que.push(i);
				visited[i] = true;
				pre[i] = front;
			}
		}
	}
	return visited[t] == true;
}
int FordFulkerson(vector<vector<int> >&resnet, int s, int t, int n)
{
	vector<int> pre(n + 1, 0);//记录找到的路径，每个节点的前一个节点
	int total = 0, minflow, i;
	while (true)
	{
		if (!(canExpand(resnet, s, t, n, pre))) return total;
		minflow = INT_MAX;
		i = t;
		//找路径中的最小流
		while (i != s)
		{
			if (minflow > resnet[pre[i]][i]) minflow = resnet[pre[i]][i];
			i = pre[i];
		}
		i = t;
		//更新残留网络
		while (i != s)
		{
			resnet[pre[i]][i] -= minflow;
			resnet[i][pre[i]] += minflow;
			i = pre[i];
		}
		total += minflow;
	}
}
int main() {

#ifdef DEBUG
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("in.txt", "r",stdin);
	//freopen("out.txt", "w",stdout);
#endif 
	int T, N, P;
	cin >> T;
	for (size_t t = 0; t < T; t++)
	{
		cin >> N >> P;
		for (size_t i = 0; i < N; i++)
			cin >> Ni[i];
		vector<vector<int>> links(N*P+2,vector<int>(N*P+2,0));

		for (size_t i = 0; i < N; i++)
			for (size_t j = 0; j < P; j++)
			{
				cin >> DATA[i][j];
			}
		int u, v;
		int x, y,x1,y1;
		for (size_t i = 0; i < N-1; i++)
		{
			for (size_t j = 0; j < P; j++)
			{
				y = floor(double(DATA[i][j]) / (double(Ni[i])*0.9));
				x = ceil(double(DATA[i][j]) / (double(Ni[i])*1.1));
				for (size_t k = 0; k < P; k++)
				{
					y1 = floor(double(DATA[i+1][k]) / (double(Ni[i+1])*0.9));
					x1 = ceil(double(DATA[i + 1][k]) / (double(Ni[i+1])*1.1));
					if (!(y1<x||x1>y))
					{
						u = i*P + j;
						v = (i + 1)*P + k;
						links[u][v] = 1;
						links[v][u] = 1;
					}
				}
			}
		}
		int S = N*P, T = N*P + 1;
		for (size_t i = 0; i < P; i++)
		{
			y = floor(double(DATA[0][i]) / (double(Ni[0])*0.9));
			x = ceil(double(DATA[0][i]) / (double(Ni[0])*1.1));
			if (x <= y)
			{
				links[S][i] = 1;
				links[i][S] = 1;
			}
			links[(N - 1)*P + i][T] = 1;
			links[T][(N - 1)*P + i] = 1;
		}
		int ans = 0;
		ans= FordFulkerson(links, S, T, N*P + 2);
		cout <<"Case #"<<t+1<<": "<< ans << endl;

	}
	return 0;
}
