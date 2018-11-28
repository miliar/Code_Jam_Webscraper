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

int maxkul(vi & S)
{
	int min=0;
	REP(i,0,S.size()-1)
	{
		if (S[min+1]-S[min]<S[i+1]-S[i]){min=i;}
	}
	return min;
}

int main()
{
	int T;
	cin>>T;
	REP(i,0,T)
	{
		int N,K;
		cin>>N>>K;
		vi S;
		S.push_back(0);
		S.push_back(N+1);
		REP(k,0,K-1)
		{
				int j=maxkul(S);
				S.push_back(S[j]+(S[j+1]-S[j])/2);
				sort(S.begin(),S.end());
		}
		int j=maxkul(S);
		/*cout<<j<<endl;
		REP(k,0,S.size()){cout<<S[k]<<" ";}
		cout<<endl;*/
		cout<<"Case #"<<i+1<<": "<<(S[j+1]-S[j]-1)/2<<" "<<(S[j+1]-S[j]-2)/2<<endl;
	}
}
