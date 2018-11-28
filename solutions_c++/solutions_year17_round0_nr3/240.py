/*
*/

#pragma GCC optimize("O3")
#define _CRT_SECURE_NO_WARNINGS
#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>

#include <memory.h>
#include <assert.h>

#define y0 sdkfaslhagaklsldk

#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
#define norm asdfasdgasdgsd
#define have adsgagshdshfhds
#define ends asdgahhfdsfshdshfd

#define eps 1e-12
#define M_PI 3.141592653589793
#define bs 1000000007
#define bsize 200

#define ldouble long double

using namespace std;

long long INF = 1e9;
const int N = 500031;

int tests;
long long n,k;
set<pair<long long, long long> > S;
map<long long, long long> cnt;
set<pair<long long, long long> > ::iterator it;
int ts;
long long ans;

void update1(long long val,long long am)
{
	if (cnt[val])
	{
		S.erase(make_pair(val,cnt[val]));
	}
	cnt[val]+=am;
	S.insert(make_pair(val,cnt[val]));
}

int main(){
	//freopen("tree.in","r",stdin);
	//freopen("tree.out","w",stdout);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	//cin.tie(0);

	cin>>tests;
	for (;tests;--tests)
	{
		S.clear();
		cnt.clear();

		cin>>n>>k;
		S.insert(make_pair(n,1));

		while (S.size())
		{
			it=S.end();
			--it;
			pair<long long, long long> p=(*it);
			S.erase(it);
			cnt[p.first]=0;

			if (p.second>=k)
			{
				ans=p.first;
				break;
			}
			k-=p.second;
			long long half1=(p.first-1)/2;
			long long half2=p.first-half1-1;

			update1(half1,p.second);
			update1(half2,p.second);
		}
		++ts;
		long long l,r;
		r=(ans-1)/2;
		l=ans-r-1;

		cout<<"Case #"<<ts<<": "<<l<<" "<<r<<endl;;
	}

	cin.get(); cin.get();
	return 0;
}
