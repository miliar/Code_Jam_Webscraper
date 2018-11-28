//#include <algorithm>
//#include <cctype>
//#include <cmath>
//#include <cstdio>
//#include <cstdlib>
//#include <cstring>
//#include <iomanip>
//#include <iostream>
//#include <map>
//#include <queue>
//#include <string>
//#include <set>
//#include <stack>
//#include <vector>
//using namespace std;
//
//
//
//struct Point
//{
//	int x, y;
//	Point(int a = 0, int b = 0)
//	{
//		x = a;
//		y = b;
//	};
//};
//
//int t, m, n;
//int dx[] = { 0, 0, 1, -1 };
//int dy[] = { 1, -1, 0, 0 };
//int c;
//#define MAX 22
//char maze[MAX][MAX];
//bool visited[MAX][MAX];
//
//void bfs(Point s)
//{
//	stack<Point> q;
//	q.push(s);
//	int x, y;
//	Point u;
//	visited[s.x][s.y] = 1;
//	while (!q.empty())
//	{
//		u = q.top();
//		q.pop();
//		for (int i = 0; i<4; i++)
//		{
//			x = u.x + dx[i];
//			y = u.y + dy[i];
//			if (x >= 0 && x<n && y >= 0 && y<m)
//			{
//				if (!visited[x][y] && maze[x][y] == '.')
//				{
//					visited[x][y] = 1;
//					c++;
//					q.push(Point(x, y));
//				}
//			}
//		}
//	}
//}
//
//int main11111()
//{
//	//freopen("INPUT.txt", "rt", stdin);
//	vector<Point> points;
//	scanf("%d", &t);
//	for(int h = 1 ; h<=t;h++)
//	{
//		scanf("%d %d", &m, &n);
//		points.clear();
//		for (int i = 0; i<n; i++)
//		{
//			for (int j = 0; j<m; j++)
//			{
//				scanf("\n%c", &maze[i][j]);
//				if (maze[i][j] == '@')
//				{
//					points.push_back(Point(i, j));
//				}
//				visited[i][j] = 0;
//			}
//		}
//		c = 1;
//		bfs(points[0]);
//		cout << "Case " << h << ": " << c << endl;
//	}
//
//	return 0;
//}

#include <iostream>
#include <vector>
#include <string>
using namespace std;
int n;
int length;
int Oversized(string str, int k)
{
	length = str.length();
	int c = 0;
	for (int i = 0; i <= length - k; i++)
	{
		if (str[i] == '-')
		{
			c++;
			for (int j = 0; j < k; j++)
			{
				if (str[i+j] == '-')
					str[i+j] = '+';
				else
					str[i+j] = '-';
			}
		}
	}
	for (int i = 0; i<k; i++)
	{
		if (str[length - 1 - i] == '-')
		{
			c = -1;
			break;
		}
	}
	return c;
}

int main()
{
	//freopen("A-large.in", "rt", stdin);
	int n, k;
	int res;
	cin >> n;
	for(int i =1;i<=n;i++)
	{
		string temp;
		cin >> temp >> k;
		cout << "Case #" << i << ": ";
		res = Oversized(temp, k);
		if (res == -1)
		{
			cout << "IMPOSSIBLE";
		}
		else
			cout << res;
		cout << endl;
	}
	return 0;
}
