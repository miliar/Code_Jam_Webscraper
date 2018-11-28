#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <climits>
#include <ctime>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_set>
#include <cmath>
#include <map>
#include <cstdio>

using namespace std;

struct Order
{
	bool operator()(pair<int, double> const& a, pair<int, double> const& b) const
	{
		return a.second > b.second;
	}
};

void distanc(const vector<vector<pair<int, double> > > &graphe, int depart, vector<double> &dist)
{
	priority_queue<pair<int, double>, vector<pair<int, double> >, Order> file;

	file.push(make_pair(depart, 0));

	vector<bool> marquage;

	marquage.resize(graphe.size(), false);
	dist.resize(graphe.size(), 1e18);

	dist[depart] = 0;

	while (!file.empty())
	{
		pair<int, double> actu = file.top();
		file.pop();

		if (marquage[actu.first])
			continue;

		marquage[actu.first] = true;

		for (unsigned int i = 0; i < graphe[actu.first].size(); i++)
		{
			pair<int, double> suiv = graphe[actu.first][i];


			if (marquage[suiv.first])
				continue;

			if (dist[suiv.first] > actu.second + suiv.second)
			{
				dist[suiv.first] = actu.second + suiv.second;

				file.push(make_pair(suiv.first, dist[suiv.first]));
			}
		}
	}
}

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		int n, q; // Sommet et arcs

		cin >> n >> q;

		vector<vector<pair<int, double> > > graphe;
		vector<pair<int, int> > villes;

		vector<vector<pair<int, double> > > g;

		g.resize(n);

		graphe.resize(n);

		for (int j = 0; j < n; j++)
		{
			int e, s; // Distance speed;
			cin >> e >> s;

			villes.push_back(make_pair(e, s));
		}

		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
			{
				int p;
				cin >> p;

				if (p != -1)
				{
					g[j].push_back(make_pair(k, p));
				}
			}
		}

		for (int j = 0; j < n; j++)
		{
			vector<double> dist;

			distanc(g, j, dist);

			for (int k = 0; k < n; k++)
			{
				if (villes[j].first >= (long long)dist[k] && k != j)
					graphe[j].push_back(make_pair(k, (double)dist[k] / (double)villes[j].second));
			}

		}

        vector<double> result;
		for (int j = 0; j < q; j++)
		{
			vector<double> dist;
			int depart, arrivee;

			cin >> depart >> arrivee;
			distanc(graphe, depart - 1, dist);


			result.push_back(dist[arrivee - 1]);
		}

		printf("Case #%d: ", i + 1);
		for(unsigned int j= 0; j < result.size() - 1; j++)
            printf("%f ", result[j]);

        printf("%f\n", result.back());

	}


	return 0;
}























