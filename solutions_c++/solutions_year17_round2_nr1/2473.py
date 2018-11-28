#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cassert>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl

void test(int cse)
{
    cout<<"Case #"<<cse<<": ";
    int D,N; cin>>D>>N;
    pair<int,int> KS[N];
    REP(i, N)
	cin>>KS[i].first>>KS[i].second;

/*    sort(KS,KS+N,[](const pair<int,int> &a,const pair<int,int> &b)->int {
	return a.first>b.first; // reverse sort by position
    });*/
    double max_time=0;
    REP(i, N) {
	double t=double(D-KS[i].first)/KS[i].second; // time to reach
	if(max_time<t)
	    max_time=t;
    }
    cout<<fixed<<setprecision(6)<<D/max_time;

    cout<<endl;
}

int main()
{
    int T; cin>>T;
    for(int i=1; i<=T; i++)
	test(i);
    return 0;
}
