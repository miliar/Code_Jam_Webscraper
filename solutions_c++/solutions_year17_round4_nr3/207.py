//#define LOCAL

#ifdef LOCAL
#define _GLIBCXX_DEBUG
#pragma GCC optimize("O3")
#endif
#include<bits/stdc++.h>
#define rep(i,k,n) for(ll i= (ll) k;i< (ll) n;i++)
#define all(v) (v).begin(), (v).end()
#define SZ(v) (int)((v).size())
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const long long INF = 4e18L + 1;
const int IINF = 2e9 + 1;
using namespace std;
template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<','; _dbg(sdbg+1, a...);
}
#ifdef LOCAL
#define DBG(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define DBG(...) (__VA_ARGS__)
#define cerr if(0)cout
#endif

/*
numerujemy wierzcholki od 0
SS to vector o rozmiarze rownym liczbe sss 
SS[i] to lista wierzcholkow dla pojedynczej spojnej
ss_ind[i] mowi, jaki jest numer spojnej skladowej wierzcholki i-tego
GSS to graf na spojnych skladowych (dag)
*/
namespace NAMESPACE
{
struct SSS
{	
	vector < vector < int > >& V, W, SS, GSS;
	vector < int > odw, kol, ss_ind;
	int nr;
	SSS(int n, vector < vector < int > >& V) : V(V), W(V.size()), odw(n), kol(n), ss_ind(n, -1), nr(0) 
	{
		for(int i=0; i<n; i++)
			for(auto el : V[i])
				W[el].pb(i);	
		for(int i=0; i<n; i++)
			if(!odw[i])
				dfs(i);
				
		for(int i=n-1; i>=0; i--)
			if(-1 == ss_ind[kol[i]])
			{
				SS.resize(SS.size()+1);
				dfs_odwr(kol[i]);
			}
		GSS.resize(SS.size());
		for(int i=0; i<n; i++)
			for(auto el : V[i])
				if (ss_ind[i] != ss_ind[el])
					GSS[ss_ind[i]].pb(ss_ind[el]);
		// ta petla usuwa krawedzie wielokrotne w grafie na silnie spojnych 
		// w czasie n log n, mozna  ja usunac
		for(auto& el : GSS) 
		{
			sort(el.begin(), el.end());
			el.resize(distance(el.begin(), unique(all(el))));
		}
	}
	void dfs(int v)
	{
		odw[v] = 1;
		for(int i=0; i<SZ(V[v]); i++)
			if (!odw[V[v][i]])
				dfs(V[v][i]);
		kol[nr++] =  v;
	}
	void dfs_odwr(int v)
	{
		SS.back().push_back(v);
		ss_ind[v] = SS.size() - 1;
		for(int i=0; i<SZ(W[v]); i++)
			if(-1 == ss_ind[W[v][i]])
				dfs_odwr(W[v][i]);
	}
};

/*
Numerujemy od 0 zmienne.
Przyklad: "(x1 v x2 ) ^ (~x1 v x3)"
------------------------------
Instrukcja konstruktora:
n liczba zmiennych (dla przykladu n to 3)
------------------------------
Instrukcja uzycia:
DWASAT dwasat(n);
klauzule xi v ~xj dodajemy : dwasat.dodaj(i, i+n)
na koniec odbalamy dwasat.rob
wartosc i-tej zmiennej to dwasat.Wel[i]
*/

struct DWASAT
{
	int n;
	vector < int > Para; 
	vector < vector < int > > V;
	vector < int > Wss, Wel;
	SSS* sss;
	DWASAT(int n) : n(2*n), V(2*n), Wss(2*n, 0), Wel(2*n, 0) 
	{
		Para.resize(2*n);
		for(int i=0; i<n; i++)
			Para[i] = i + n;
		for(int i=n; i<2*n; i++)
			Para[i] = i - n;
	}
	void dodaj(int a, int b) 
	{
		V[ Para[a] ].pb(b);
		V[ Para[b] ].pb(a);
	}
	bool rob()
	{
		sss = new SSS(n, V);
		vector < int > kol = toposort(sss->SS.size(), sss->GSS);
		for(int i = SZ(kol)-1; i>=0; i--)
			if (!Wss[kol[i]])
			{
				Wss[kol[i]] = 1;
				for(auto& el : sss->SS[kol[i]])
				{
					Wel[el] = 1;
					int zaprz = Para[el];
					if (Wel[zaprz] == 1)
						return false;
					Wel[zaprz] = -1;
					Wss[sss->ss_ind[zaprz]] = -1;
				}
			}
		return true;
	}
	vector < int > toposort(int n, vector < vector < int > >& G)//grafu sa na koncu
	{
		queue < int > Q;
		vector < int > st(n, 0), odp;
		for(auto& el : G)
			for(auto v : el)
				st[v]++;
		for(int i=0; i<n; i++)
			if (st[i] == 0)
				Q.push(i);
		while(!Q.empty())
		{
			odp.pb(Q.front());
			for(auto& el : G[Q.front()])
			{
				st[el]--;
				if (!st[el]) 
					Q.push(el);
			}
			Q.pop();
		}
		return odp;
	}
};
}

char T[55][55];
int Z[55][55];
char S[55][55];
int R, C;
vector < int > V;
vector < pair < int, int > > Pola[2505];//kto, kierunek

void rusz_sie(pair < int, int >& poz, int& kier)
{
	if (T[poz.ft][poz.sd] =='/')
	{
		kier  ^= 1;
	}
	if (T[poz.ft][poz.sd] =='\\')
	{
		kier  = 3-kier;
	}
	switch(kier)
	{
	case 0:
		poz.ft--;
		break;
	case 1:
		poz.sd++;
		break;
	case 2:
		poz.ft++;
		break;
	case 3:
		poz.sd--;
		break;
	}
} 

vector < pair < int, int > > generuj(int y, int x, int q, bool& ok)
{
	vector < pair < int, int > > res;
	if (q == 0)
	{
		pair < int, int > poz(y-1, x);
		int kier = 0;
		for(int i=0; i<2501; i++)
		{
			if (poz.ft < 0 || poz.ft >= R || poz.sd < 0 || poz.sd >= C || (T[poz.ft][poz.sd] == '#'))
				break;
			if (S[poz.ft][poz.sd] == 1)
			{
				ok = false;
				return {};
			}
			if (T[poz.ft][poz.sd] == '.')
				res.pb(poz);
			rusz_sie(poz, kier);
		}
		poz = {y+1, x};
		kier = 2;
		for(int i=0; i<2501; i++)
		{
			if (poz.ft < 0 || poz.ft >= R || poz.sd < 0 || poz.sd >= C || (T[poz.ft][poz.sd] == '#'))
				break;
			if (S[poz.ft][poz.sd] == 1)
			{
				ok = false;
				return {};
			}
			if (T[poz.ft][poz.sd] == '.')
				res.pb(poz);
			rusz_sie(poz, kier);
		}
	}
	else
	{
		pair < int, int > poz(y, x-1);
		int kier = 3;
		for(int i=0; i<2501; i++)
		{
			if (poz.ft < 0 || poz.ft >= R || poz.sd < 0 || poz.sd >= C || (T[poz.ft][poz.sd] == '#'))
				break;
			if (S[poz.ft][poz.sd] == 1)
			{
				ok = false;
				return {};
			}
			if (T[poz.ft][poz.sd] == '.')
				res.pb(poz);
			rusz_sie(poz, kier);
		}
		poz = {y, x+1};
		kier = 1;
		for(int i=0; i<2501; i++)
		{
			if (poz.ft < 0 || poz.ft >= R || poz.sd < 0 || poz.sd >= C || (T[poz.ft][poz.sd] == '#'))
				break;
			if (S[poz.ft][poz.sd] == 1)
			{
				ok = false;
				return {};
			}
			if (T[poz.ft][poz.sd] == '.')
				res.pb(poz);
			rusz_sie(poz, kier);
		}
		
	}
	ok = true;
	sort(all(res));
	res.resize( distance(res.begin(), unique(all(res))) );
	return res;
}

void check()
{
	
}

int pole(int a, int b)
{
	return a + R*b;
}

int main()
{
#ifndef LOCAL
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#endif

	int t;
	cin>>t;
	for(int ii=1; ii<=t; ii++)
	{
		DBG(ii);
		int num = 0;
		cin>>R>>C;
		V.clear();
		V.resize(2501, 0);
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
			{
				cin>>T[i][j];
				S[i][j] = 0;
				if (T[i][j] == '-' || T[i][j] == '|')
				{
				//	DBG(i, j, num);
					T[i][j] = 0;
					Z[i][j] = num++;
					S[i][j] = 1;
				}
			}
		for(int i=0; i<R*C; i++)
			Pola[i].clear();
		bool da_sie_zrobic = true;
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
			{
				if (S[i][j] == 0)
					continue;
				bool ok1, ok2;
				vector < pair < int, int > > a1 = generuj(i, j, 0, ok1);//pion
				vector < pair < int, int > > a2 = generuj(i, j, 1, ok2);
				if (!ok1 && !ok2)
				{
					da_sie_zrobic = false;
				}
				if (ok1)
				{
					for(auto el : a1)
						Pola[pole(el.ft, el.sd)].pb({Z[i][j], 0});
					V[Z[i][j]] |= 1;
				}
				if (ok2)
				{
					for(auto el : a2)
						Pola[pole(el.ft, el.sd)].pb({Z[i][j], 1});
					V[Z[i][j]] |= 2;
				}
				/*
				DBG(i, j, ok1, ok2);
				for(auto el : a1)
					printf("(%d, %d) ", el.ft, el.sd);
				cout<<endl;
				for(auto el : a2)
					printf("(%d, %d) ", el.ft, el.sd);
				cout<<endl;
				*/ 
			}
		NAMESPACE::DWASAT ds(num);
		for(int i=0; i<num; i++)
		{
			//DBG(i, V[i]);
			if (V[i] == 1)
				ds.dodaj(num+i, num+i);
			if (V[i] == 2)
				ds.dodaj(i, i);
		}
		
		for(int i=0; i<R; i++)
		{
			for(int j=0; j<C; j++)
			{
				if (T[i][j] != '.' || S[i][j])
					continue;
				
				int pol = pole(i, j);
				assert(Pola[pol].size() <= 2);
				if (Pola[pol].size() == 0)
				{
					da_sie_zrobic = false;
				}
				else if (Pola[pol].size() == 1)
				{
					int kto, war;
					tie(kto, war) = Pola[pol].back();
					ds.dodaj(kto + (1-war)*num, kto + (1-war)*num);
				}
				else
				{
					int kto1, war1, kto2, war2;
					tie(kto1, war1) = Pola[pol][0];
					tie(kto2, war2) = Pola[pol][1];
					ds.dodaj(kto1 + (1-war1)*num, kto2 + (1-war2)*num);
				}
			}
		}
		if (!ds.rob())
		{
			da_sie_zrobic = false;
			DBG(ii, "AAAAAAAAAAAAAAAAAAA");
		}
		
		for(int i=0; i<R; i++)
		{
			for(int j=0; j<C; j++)
			{
				if(!S[i][j])
					continue;
				//DBG(ds.Wel[T[i][j]]);
				if (ds.Wel[Z[i][j]]== 1)
					T[i][j] = '-';
				else
					T[i][j] = '|';
			}
		}
		
		if (!da_sie_zrobic)
		{
			cout << "Case #" << ii << ": IMPOSSIBLE"<<endl;
			DBG(ii, C);
		}
		else
		{
			cout << "Case #" << ii << ": POSSIBLE"<<endl;
			for(int i=0; i<R; i++)
			{
				for(int j=0; j<C; j++)
					cout<<T[i][j];
				cout<<endl;
			}
			for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
			{
				if (S[i][j] != 1)
					continue;
				bool ok;
				vector < pair < int, int > > a;
				if (T[i][j] == '|')
					a = generuj(i, j, 0, ok);
				else
					a = generuj(i, j, 1, ok);
				assert(ok);
				for(auto& el : a)
				{
					assert(T[el.ft][el.sd] == '.');
					S[el.ft][el.sd] = 2;
				}
			}
			
				
			for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
				if(T[i][j] == '.')
					assert(S[i][j] == 2);
		}
			
		

	}
	
    return 0;
}

