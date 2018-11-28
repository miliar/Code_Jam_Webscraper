#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define st first
#define nd second

const int maxn = 200;

int t,n,q,start,stop;
int zasieg[maxn], predkosc[200];
int d[maxn][maxn];
int krawedz[maxn];
double odleglosc[maxn];

vector <pair<double,int> > wektor[maxn];

bitset <maxn> zajete;

priority_queue <pair<double,int> ,vector<pair<double,int> >, greater<pair<double,int> > > Q;

int main()
{
	cin >> t;
	for(int z=1;z<=t;z++)
	{
		cin >> n >> q;
		for(int i=1;i<=n;i++)
		{
			cin >> zasieg[i] >> predkosc[i];
		}
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
			{
				cin >> d[i][j];
				if(d[i][j]>0) krawedz[j] = d[i][j];  // krawedz[j] oznacza odleglosc do wierzcholka j
			}
		}
		for(int i=1;i<=q;i++)
		{
			cin >> start >> stop;
		}
		// solution
		
		for(int i=1;i<=n;i++)
		{
			double czas=0.0;
			for(int j=i+1;j<=n;j++)
			{
				czas = czas + krawedz[j]/(double)predkosc[i];
				zasieg[i]-=krawedz[j];
				if(zasieg[i]>=0)
				{
					wektor[i].pb(mp(czas,j));
				}
				else
				{
					break;
				}
			}
		}
		
		//dijkstra
		
		/*for(int i=1;i<=n;i++)
		{
			cout << i << ": " << endl;
			for(int j=0;j<wektor[i].size();j++)
			{
				cout << setprecision(5) << fixed << wektor[i][j].st << " " << wektor[i][j].nd << endl;
			}
			cout << endl;
		}
		cout << endl;*/
		
		for(int i=1;i<=n;i++)
		{
			odleglosc[i] = 100000000000000;
		}
		odleglosc[1] = 0;
		for(int i=1;i<=n;i++)
		{
			Q.push(mp(odleglosc[i],i));
		}
		while(!Q.empty()) // odleglosc .. wierzcholek
		{
			int v = Q.top().nd;
			//Q.pop();
			//cout << Q.top().st << " " << v << endl;
			Q.pop();
			if(!zajete[v])
			{
				for(int i=0;i<wektor[v].size();i++)
				{
					if(odleglosc[v]+wektor[v][i].st<odleglosc[wektor[v][i].nd])
					{
						odleglosc[wektor[v][i].nd]=odleglosc[v]+wektor[v][i].st;
						//poprzednik[wektor[v][i].st]=v;
						Q.push(mp(odleglosc[wektor[v][i].nd],wektor[v][i].nd));
					}
				}
				zajete[v]=1;
			}
		}
		/*cout << endl << "odleglosci: " << endl;
		for(int i=1;i<=n;i++)
		{
			cout << setprecision(10) << fixed << odleglosc[i] << endl;
		}
		cout << endl;*/
		cout << "Case #" << z << ": " << setprecision(10) << fixed << odleglosc[n] << endl;
		zajete.reset();
		while(!Q.empty()) Q.pop();
		for(int i=1;i<=n;i++)
		{
			wektor[i].clear();
		}
	}
}
