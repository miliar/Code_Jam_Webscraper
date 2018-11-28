#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <bitset>
#include <math.h>

using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef vector<vector <int> > vvi;
typedef pair<int,int> ii;
typedef vector <ii> vii;
#define REP(i,a,b)\
for (ll i=a; i<b; i++)


string ford(string s, int i, int k)
{
		REP(j,i,i+k)
		{
				if (s[j]=='-'){s[j]='+';}else{s[j]='-';}
		}
		return s;
}

int main()
{
	int T;
	cin>>T;
	REP(i,0,T)
	{
			string s;
			int k;
			cin>>s>>k;
			int db=0;
			for (int j=0; j<=s.length()-k; j++)
			{
					if (s[j]=='-'){s=ford(s,j,k);db++;}
			}
			REP(j,s.length()-k,s.length())
			{
					if (s[j]=='-'){db=-1;}
			}
			if (db>=0)
			cout<<"Case #"<<i+1<<": "<<db<<endl;
			else
			cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
