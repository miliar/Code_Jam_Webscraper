#include<iostream>
#include<fstream>
#include<queue>
#include<functional>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int main()
{
	int T;
	in >> T;
	for (int t = 0; t < T; t++)
	{
		vector<pair<int, int> > V;
		queue<pair<int, int> > Q;
		int n, m;
		in >> n >> m;
		Q.push({ n / 2,n - (n / 2) - 1 });
		int now = 0;
		while (!Q.empty())
		{
			auto a = Q.front();
			V.push_back(a);
			Q.pop();
			now++;
			/*if (now == m)
			{
				out << "Case #" << t+1 << ": "<< a.first << " " << a.second << endl;
				break;
			}*/

			if(a.first!=0){
				Q.push({ a.first / 2, a.first - (a.first / 2) - 1 });
			}
			if (a.second != 0)
				Q.push({ a.second / 2, a.second - (a.second / 2) - 1 });
		}
		sort(V.begin(), V.end(), greater<>());
		out << "Case #" << t + 1 << ": " << V[m-1].first << " " << V[m-1].second << endl;
	}
	return 0;
}