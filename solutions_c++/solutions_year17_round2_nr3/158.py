#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <deque>
#include <cmath>
#include <list>
#include <set>
#include <map>
#define rep(i,m,n) for(int i=(m),_end=(n);i < _end;++i)
#define repe(i,m,n) for(int i=(m), _end =(n);i <= _end;++i)
typedef long long ll;
using namespace std;


double dist[101][101];
double time[101][101];

double md[101];
double sp[101];

double dmax = 1e99;

void sol(ifstream& sr, ofstream& sw) {

	sw.precision(17);

	int N, Q;
	sr >> N >> Q;

	for (int i = 0; i < N; i++)
	{
		sr >> md[i] >> sp[i];
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			sr >> dist[i][j];
			if (dist[i][j] < 0)
				dist[i][j] = dmax;
			if (i == j)
				dist[i][i] = 0;
		}
	}

	for (int k = 0; k < N; k++)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (dist[i][j] > dist[i][k] + dist[k][j])
					dist[i][j] = dist[i][k] + dist[k][j];
			}
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (i == j)
				time[i][i] = 0;
			else
				if (dist[i][j] <= md[i] + 1e-7)
					time[i][j] = dist[i][j] / sp[i];
				else
					time[i][j] = dmax;
		}
	}

	for (int k = 0; k < N; k++)
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (time[i][j] > time[i][k] + time[k][j])
					time[i][j] = time[i][k] + time[k][j];
			}
		}
	}

	for (int i = 0; i < Q; i++)
	{
		int U, V;
		sr >> U >> V;
		sw << time[U - 1][V - 1];
		if (i != Q - 1)
			sw << " ";
	}

}

int main() {

	ifstream sr = ifstream("D:\\in.in");
	ofstream sw = ofstream("D:\\out.out");

	int T;
	sr >> T;
	for (int i = 0; i < T; i++)
	{
		sw << "Case #" << i + 1 << ": ";
		sol(sr, sw);
		sw << endl;
		cout << i << endl;
	}
	sr.close();
	sw.close();
	cout << "FINISHED type a number and enter to exit";
	cin >> T;

	return 0;
}
