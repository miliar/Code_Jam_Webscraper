#include <bits/stdc++.h>

using namespace std;



bool visited[100];

int horseDistance[100];

long double horseSpeed[100];

int edges[100][100];

long double horseEdges[100][100];


int N, Q;
//not dfs but dijkstra
void dijkstra(int from, int remainDistance, int root)
{
	set< pair<long double, pair<int, int> > > Q;

	Q.insert(make_pair( 0, make_pair(root, remainDistance) ));


	while(!Q.empty())
	{

		pair<long double, pair<int, int> > top = *Q.begin();


		//cout<<root<<" "<<top.first<<" "<<top.second.first<<" "<<top.second.second<<"\n";

		
		Q.erase(Q.begin());

		from = top.second.first;

		visited[from] = true;

		horseEdges[root][from] = top.first;

		for (int i = 0; i < N; ++i)
		{
			if(visited[i] || edges[from][i] == -1)
				continue;

			if(edges[from][i] > top.second.second)
				continue;

			Q.insert(make_pair( horseEdges[root][from] + edges[from][i]/horseSpeed[root], make_pair(i, top.second.second - edges[from][i]) ));


		}


	}



}


void read()
{
	cin>>N;
	cin>>Q;
	for (int i = 0; i < N; ++i)
	{
		cin>>horseDistance[i];
		cin>>horseSpeed[i];
	}

	for (int i = 0; i < N; ++i)
		for (int j = 0; j <N; ++j)
		{
			cin>>edges[i][j];
			horseEdges[i][j] = -1;
		}

}


void solve()
{

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			visited[j] = false; 
		}
		//calc horseDistance from i
		horseEdges[i][i] = 0;

		dijkstra(i, horseDistance[i], i);
	}




	for (int k = 0; k < N; ++k)
    {
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < N; ++j)
            {
            	if(horseEdges[i][k] != -1 && horseEdges[k][j] != -1)
                	if (horseEdges[i][k] + horseEdges[k][j] < horseEdges[i][j] || horseEdges[i][j] == -1)
                    	horseEdges[i][j] = horseEdges[i][k] + horseEdges[k][j];
            }
        }
    }



}



int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);

	cout.precision(10);

	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		read();
		solve();//not queries
		

		cout<<"Case #"<<t<<":";
		for (int i = 0; i < Q; ++i)
		{
			int a, b;
			cin>>a>>b;
			cout<<" "<<horseEdges[a-1][b-1];
		}
		cout<<"\n";

	}


	return 0;
}