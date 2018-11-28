#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
int main()
{
	//ios::sync_with_stdio(0);
	int T;
	cin>>T;
	int tc = 1;
	while (T--)
	{
		int N, P;
		cin>>N>>P;
		int R[N];
		for (int i = 0; i < N; ++i)
		{
			cin>>R[i];
		}
		int Q[N][P];
		pair<int,int> q[N][P];
		//int minq[N][P], maxq[N][P];
		//memset(minq, -1, sizeof minq);
		//memset(maxq, -1, sizeof maxq);
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < P; ++j)
			{
				cin>>Q[i][j];
				float el = Q[i][j] * 100.0/110.0;
				float em = Q[i][j] * 100.0/90.0;
				el /= R[i];
				em /= R[i];
				el = ceil(el);
				em = floor(em);
				q[i][j].first = q[i][j].second = -1;
				if (em >= el)
				{
					q[i][j].first = el;
					q[i][j].second = em;
				}
			}
		}
		for (int i = 0; i < N; ++i)
		{
			sort(q[i], q[i]+P, [](auto &a, auto &b){
				if (a.first == b.first)
					return a.second < b.second;
				return a.first < b.first;
			});
			//for (int j = 0; j < P; ++j)
			//	cout<<'('<<q[i][j].first<<','<<q[i][j].second<<") ";
			//cout<<'\n';	
		}
		//cout<<"*\n";

		int ptrsx[N];
		memset(ptrsx, 0, sizeof ptrsx);
		int count = 0;

		while (ptrsx[0] < P && q[0][ptrsx[0]].first == -1)
			++ptrsx[0];

		while (true)
		{

			bool flag = false;

			for (int i = 0; i < N; ++i)
			{
				if (ptrsx[i] == P)
				{
					flag = true;
					break;
				}
			}

			if (flag) break;

			int st = q[0][ptrsx[0]].first, en = q[0][ptrsx[0]].second;
			//cout<<st<<','<<en<<'\n';
			for (int i = 1; i < N; ++i)
			{
				st = max(st, q[i][ptrsx[i]].first);
				en = min(en, q[i][ptrsx[i]].second); 
			}
			//cout<<st<<','<<en<<'\n';
			if (st > en)
			{
				int minim = q[0][ptrsx[0]].first;
				int index = 0;
				for (int i = 1; i < N; ++i)
				{
					if (q[i][ptrsx[i]].first < minim)
					{
						minim = q[i][ptrsx[i]].first;
						index = i;
					}
				}
				++ptrsx[index];
			}
			else
			{
			//	cout<<"here\n";
				++count;
				for (int i = 0; i < N; ++i)
				{
					++ptrsx[i];
				}
			}
		}

		cout<<"Case #"<<tc++<<": "<<count<<'\n';
	}	
}