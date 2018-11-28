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

int main()

{
	
	int T;
	cin>>T;
	REP(i,0,T)
	{
		int N;
		int R,O,Y,G,B,V;
		cin>>N>>R>>O>>Y>>G>>B>>V;
		char ltC;
		int m;
		vector <pair <int, char> > I;
		I.push_back(make_pair(R,'R'));
		I.push_back(make_pair(B,'B'));
		I.push_back(make_pair(Y,'Y'));
		sort(I.begin(),I.end());
		reverse(I.begin(),I.end());
		vector <char> Is;
		if (I[0].first>I[1].first+I[2].first){cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;}else
		{
			int M=N-2*I[0].first;
			while (I[0].first>0)
			{
					Is.push_back(I[0].second);
					I[0].first--;
					Is.push_back(I[1].second);
					I[1].first--;
					if (I[1].first<I[2].first){pair <int, char>  p=I[1]; I[1]=I[2]; I[2]=p;}
			}
			if (I[1].first==I[2].first){pair <int, char>  p=I[1]; I[1]=I[2]; I[2]=p;}
			bool flag=true;
			while (M>0)
			{
				if (flag){	Is.push_back(I[1].second);}else{Is.push_back(I[2].second);}
				flag=!flag;
				M--;
			}
			cout<<"Case #"<<i+1<<": ";
			REP(j,0,N)
			{
				cout<<Is[j];
			}
			cout<<endl;
		}
	}		
	return 0;	
	
}
