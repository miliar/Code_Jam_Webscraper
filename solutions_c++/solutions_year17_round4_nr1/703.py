#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <bitset>
#include <math.h>
#include <iomanip>

using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef vector<vector <int> > vvi;
typedef pair<int,int> ii;
typedef vector <ii> vii;
#define REP(i,a,b)\
for (ll i=a; i<b; i++)

int abs(int n)
{if (n>0){return n;}else{return -n;}}

int main()

{
	
	int T;
	cin>>T;
	REP(i,0,T)
	{
		int n,p;
		cin>>n>>p;
		int g;
		int ossz=0;
		int e=0;
		int k=0;
		vector<int> M(p,0);
		REP(j,0,n)
		{
				cin>>g;
				M[g%p]++;
		}
		ossz+=M[0];
		if (p==2)
		{
				if (M[1]>0){
				ossz+=((M[1]+1)/2);}
		}
		if (p==3)
		{
				int db=min(M[1],M[2]);
				ossz+=db;
				M[1]-=db;
				M[2]-=db;
				if (M[1]>0){ossz+=(M[1]+2)/3;}
				if (M[2]>0){ossz+=(M[2]+2)/3;}
		}
		cout<<"Case #"<<i+1<<": "<<ossz<<endl;
	}		
	return 0;	
	
}
