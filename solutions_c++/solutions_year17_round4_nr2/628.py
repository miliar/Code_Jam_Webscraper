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
		int N,C,M;
		cin>>N>>C>>M;
		vii Tick;
		ii p;
		int P,B;
		vi Cus(C,0);
		vi Fog(N,0);
		REP(j,0,M)
		{
			cin>>P>>B;
			P--;
			B--;
			p.first=P;
			p.second=B;
			Tick.push_back(p);
			Cus[B]++;
			Fog[P]++;
		}
		int maxC=*max_element(Cus.begin(),Cus.end());
		//cout<<maxC<<endl;
		int jar=1;
		ll sumup=0;
		ll osszcsere=0;
		for (int k=0; k<N; k++)
		{
				int j=k+1;
				sumup+=Fog[k];
				//cout<<"S "<<sumup<<" ";
				if (jar<(sumup+j-1)/j)
				{
					jar=(sumup+j-1)/j;
				}
		}
		jar=max(jar,maxC);
		for (int k=0; k<N; k++)
		{
				if (Fog[k]>jar){osszcsere+=Fog[k]-jar;}
		}
		cout<<"Case #"<<i+1<<": "<<jar<<" "<<osszcsere<<endl;
	}		
	return 0;	
	
}
