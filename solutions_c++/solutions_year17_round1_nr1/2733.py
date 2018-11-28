#include <iostream>
#include <vector>
#include <set>
#include <map>
#include  <bits/stdc++.h>
#define FOR(i,n) for(int i=0;i<(int)n;i++)
#define ALL(v) v.begin(),v.end()
#define UNIQUE(c) (c).resize(distance((c).begin(), unique(ALL(c))))
using namespace std;

typedef long long int LL;
typedef long long unsigned int LLU;

typedef vector<int>   VI;       typedef vector<bool> VB;
typedef vector<VI>   VVI;       typedef vector<double> VD;
typedef vector<VVI> VVVI;       typedef vector<VD> VDD;

typedef vector<char> VC;
typedef vector<VC> VVC;

typedef pair<int,int> PI;       typedef pair<double,double> PD;
typedef pair<PI,int> PII;

template<typename T>
void r(T& o)
{
	cin >> o;
}
template<typename T>
void rv( int n, vector<T> &o)
{
	for(int bal=0; bal<n;bal++)
	{
		int j=0;
		r(j);
		o.push_back(j);
	}
}
template<typename T>
void rv(vector<T> &o)
{
	int t;
	r(t);
	rv(t,o);
}

template<typename T>
void ov(const vector<T> &i)
{
	for(auto v: i)
	{
		cout << v << " ";
	}
}

void proc()
{
    int r, c;
    cin >> r >> c;
    VVC m(r, VC(c,'?'));
    VVC mr(r, VC(c,'?'));
    FOR(i,r)
    {
        FOR(j,c)
        {
            cin >> m[i][j];
        }
    }

    FOR(i,r)
    {
        FOR(j,c)
        {
        cerr << m[i][j] << endl;
            if(m[i][j] != '?')
            {
                int mk = 0, Mk = c;
                for(int k=j+1; k<Mk; k++)
                {
                    cerr << k;
                    if(mr[i][k] == '?' and m[i][k] == '?')
                    {
                        mr[i][k] = m[i][j];
                    }
                    else
                    {
                        Mk = k-1;
                    }
                    cerr << " Mk " << Mk << endl;
                }
                for(int k=j-1; k>=mk; k--)
                {
                    if(mr[i][k] == '?' and m[i][k] == '?')
                    {
                        mr[i][k] = m[i][j];
                    }
                    else
                    {
                        mk = k+1;
                    }
                }
                cerr << i << " " << j<< " "  << mk << " " << Mk << endl;
                for(int k=i+1; k<r; k++)
                {
                    if(find_if_not(mr[k].begin() + mk, min(mr[k].end(), mr[k].begin() + Mk + 1), [](char c){return c == '?';} ) == min(mr[k].end(), mr[k].begin() + Mk + 1) and
                    find_if_not(m[k].begin() + mk, min(m[k].end(), m[k].begin() + Mk + 1), [](char c){return c == '?';} ) == min(m[k].end(), m[k].begin() + Mk + 1) )
                    {
                        for(int l = mk; l <= Mk; l++) mr[k][l] = m[i][j];
                    }
                    else break;
                }
                for(int k=i-1; k>=0; k--)
                {
                    if(find_if_not(mr[k].begin() + mk, min(mr[k].end(), mr[k].begin() + Mk + 1), [](char c){return c == '?';} ) == min(mr[k].end(), mr[k].begin() + Mk + 1) and
                    find_if_not(m[k].begin() + mk, min(m[k].end(), m[k].begin() + Mk + 1), [](char c){return c == '?';} ) == min(m[k].end(), m[k].begin() + Mk + 1) )
                    {
                        for(int l = mk; l <= Mk; l++) mr[k][l] = m[i][j];
                    }
                    else break;
                }
                mr[i][j] = m[i][j];
            }
        }
    }

    cout << endl;
	for(auto vi: mr){ for (auto v: vi) cout << v ; cout <<endl; }
}

int main()
{
	int t;
	int n;
	int j;
	r(t);
	cerr << "Going for " << t << " cases" << endl;
	for(int i = 1; i<t+1; i++)
	{
		cerr << "Starting case " << i << endl;
		cout << "Case #" << i << ":";
		proc();
		//cout << endl;
	}
	return 0;
}
