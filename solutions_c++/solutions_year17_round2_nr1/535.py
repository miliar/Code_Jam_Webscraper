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

int main()

{
	
	int T;
	cin>>T;
	REP(i,0,T)
	{
		ll D,N;
		cin>>D>>N;
		vii Lovas;
		vector <double> Ido;
		ll k,s;
		REP(j,0,N)
		{
			cin>>k>>s;
			double I=(double(D)-k)/s;
			Ido.push_back(I);
		}	
		sort(Ido.begin(),Ido.end());
		double H=Ido[Ido.size()-1];//legtobb ido
		double mo=D/H;
		cout<<"Case #"<<i+1<<": "<<fixed<<mo<<endl;
	}		
	return 0;	
	
}
