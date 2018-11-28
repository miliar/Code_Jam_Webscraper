#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <bitset>
#include <math.h>
#include <stdio.h>

using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef vector<vector <int> > vvi;
typedef pair<int,int> ii;
typedef vector <ii> vii;
#define REP(i,a,b)\
for (ll i=a; i<b; i++)

ll sm(ll dec)
{
		if (dec>10){return dec/10;}
		else{return 1;}
}

ll p(int db)
{
		ll d=1;
		REP(i,0,db)
		{d*=10;}
		return d;
}

ll maxd(ll n)
{
		ll d=1;
		while (n/d>=10){d*=10;}
		return d;
}

ll lev(ll n)
{
	return n-(maxd(n)*(n/maxd(n)));
}

int holnem(ll n)
{
	char str[256];
	sprintf(str, "%lld", n);
	int h=1;
	while (n>=10){h++;n/=10;}
	int tort;
	for (int i=0; i<h-1; i++)
	{
			if (str[i]>str[i+1])return h-(i+1);
	}
	return 0;
}

int nulles9(ll n)
{
	char str[256];
	sprintf(str, "%lld", n);
	int h=1;
	while (n>=10){h++;n/=10;}
	int db=0;
	int i=h-1;
	while (i>=0 && str[i]=='0'){db++; i--;}
	while (i>0 && str[i] ==str[i-1]){db++; i--;}
	return db;
}


int main()
{
	//cout<<nulles9(770)<<" "<<nulles9(5770)<<" "<<nulles9(909900)<<nulles9(6789900)<<endl;
	int T;
	cin>>T;
	REP(i,0,T)
	{
		ll N;
		cin>>N;
		if (N<10){cout<<"Case #"<<i+1<<": "<<N<<endl;}
		else
		{
			ll newN=N;
			int db=holnem(N)-1;
			if (db==-1){
			cout<<"Case #"<<i+1<<": "<<newN<<endl;}else
			{
					newN=N/p(db+1)*p(db+1);
					int ndb=nulles9(newN);
					if (ndb>db){
					newN=newN/p(ndb)*p(ndb);}
					newN--;
					cout<<"Case #"<<i+1<<": "<<newN<<endl;
			}
		}
	}
	
 return 0;
}
