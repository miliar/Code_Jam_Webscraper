#include <bits/stdc++.h>
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
# define INF 0x3f3f3f3f

 
typedef pair<int, int> ii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector <int> > vvi;
typedef vector<vector <double> > vvd;
typedef vector <pair <int,int> > vii;
#define REP(i,a,b)\
for (ll i=a; i<b; i++)
 
 
 
void floyds(vvd &a )

{
		int v=a.size();
      for(int k = 0; k < v; k++)
        for(int i = 0; i < v; i++)
            for(int j = 0; j < v; j++)
                if((a[i][k]>0 && a[k][j]>0) && (a[i][j]>a[i][k]+a[k][j] ||  a[i][j]==-1))
                    {a[i][j]=a[i][k]+a[k][j];

					}
}

int main()

{
int T;
	cin>>T;
	REP(i,0,T)
	{
		ll N,Q;
		cin>>N>>Q;
		vvd A;
		REP(j,0,N)
		{vector<double> D(N,-1);
			A.push_back(D);}
		vii City;
		vii PS;
		REP(j,0,N)
		{
			ll E,S;
			cin>>E>>S;
			ii p(E,S);
			City.push_back(p);
		}
		ll s;
		REP(j,0,N)
		{
				REP(k,0,N)
				{
					
					cin>>s;
					A[j][k]=s;
				}
				A[j][j]=0;
		}
		REP(j,0,Q)
		{
			ll E,S;
			cin>>E>>S;
			ii p(E,S);
			PS.push_back(p);
		}
		/*REP(j,0,N)
		{
			REP(k,0,N)
			cout<<A[j][k]<<" ";
			cout<<endl;
		}*/
		floyds(A);
		/*REP(j,0,N)
		{
			REP(k,0,N)
			cout<<A[j][k]<<" ";
			cout<<endl;
		}*/
		vvd G;
		REP(j,0,N)
		{vector<double> D(N,-1);
			G.push_back(D);}
		REP(j,0,N)
		{
				REP(k,0,N)
				{
					if (City[j].first>=A[j][k]-0.01)
					{
						if (G[j][k]==-1 || G[j][k]>A[j][k]/City[j].second)
							G[j][k]=A[j][k]/City[j].second;
					}
				}
		}
		floyds(G);
		cout<<"Case #"<<i+1<<": ";
		REP(j,0,Q)
		{
				cout<<setprecision(7)<<fixed<<G[PS[j].first-1][PS[j].second-1]<<" ";
		}
		cout<<endl;
	}		
	return 0;	
}
