// Dont hack this or I hack ur mama
#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#define ll long long 
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
using namespace std;

////////////// END OF TEMPLATE
int T;
int c[6], N;
int sz[6] = {3,1,3,1,3,1};
int C[6][3] = {{2,3,4},{4,-1,-1},{0,4,5},{4,-1,-1},{0,2,1},{2,-1,-1}};
void solve();
void read()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);

	cin >> T;
	for(int i = 0 ; i < T; i++)
	{
		cin >> N;
		for(int j=0;j<6;j++)
			cin >> c[j];
		
		printf("Case #%d: ",i+1);
		solve();
	}
}
string g(int val)
{
	switch(val)
	{
		case 0:
			return "R";
		case 1:
			return "O";
		case 2: 
			return "Y";
		case 3:
			return "G";
		case 4:
			return "B";
		case 5:
			return "V";
	}
}
string ret = "";
bool found = false;
int zero;
void solve(int rec, int l, string t)
{
	if(found)
		return;
	if(rec == (N-1))
	{
		
		bool ttt = false;
		for(int j = 0 ; j < sz[zero]; j++)
		{
			if( C[zero][j] == l)
			{
			  ttt =true;
			  break;
			}
		}	
		if(ttt)
		{
		//	cout << "IM HREERE DICKSCUKER\n";
			ret=t;
			ret+=g(l);
			found = true;
		}
	}else{
		c[l] --;
		string TZ = t;
		TZ+=g(l);
		//cout << TZ << endl;	
		vector < pair < int , int > > v;
		for(int i = 0 ; i < sz[l] && !found; i++)
		{
			if(c[C[l][i]] >0 )
			{
				v.pb(mp(c[C[l][i]],C[l][i]));
			}
		}	
		sort(v.begin(),v.end());
		for(int i = v.size() - 1; i >=0 ; i--)
		{
			solve(rec+1,v[i].second,TZ);
		}
		c[l]++;
	}
}
void solve()
{
	ret = "IMPOSSIBLE";
	int next = 0;
	found = false;
	//prep();
	if((c[0] + c[2]) < c[4] || (c[0] + c[4]) < c[2] || (c[2] + c[4]) < c[0])
	{
		cout << ret << endl;
	}else{
	for(int i = 0 ; i < 6; i++) if(c[i] != 0){ next = i;}
	zero= next;
	solve(0,next,"");
	cout << ret << endl;
	}
}
int main()
{
	std::ios::sync_with_stdio(false);
	read();
	return 0;
}
