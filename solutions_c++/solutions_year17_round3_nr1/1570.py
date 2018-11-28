#include <bits/stdc++.h>
using namespace std;

typedef pair< int , int > pii;
typedef long long ll;
typedef pair< ll , ll >  pll;
const ll MOD = 1000000007LL;
typedef pair<double ,double > pdd;
pdd array[1000];
const double PI = 3.141592653589793238462643383279502884L;


////////////////////////////////////////////
int comp (const pdd &a,const pdd &b)
{
	if(a.first != b.first)
		return a.first > b.first;
	return a.second > b.second;
}

void Solve(int Case)
{
	// input

	int N,K;
	cin>>N>>K;

	for(int i=0;i<N;++i)
	{
		cin>>array[i].first >> array[i].second;
		array[i].second =2 *  array[i].first * array[i].second;
	}

	sort(array,array+N,comp);
	int k = 0;
	
	double ans = 0;

	for(int i=0;i+K-1 < N; ++i)
	{
		double tmp = array[i].second +  array[i].first * array[i].first;
		priority_queue<double , vector<double> , less<double> > PQ;
		for(int j=i+1;j< N; ++j)
		{
			PQ.push(array[j].second);
		}
		int son = 0;
		while(son < K-1)
		{
			tmp = tmp + PQ.top();
			PQ.pop();
			son++;
		}
		ans = max( tmp , ans );
	}
	ans = ans*atan(1)*4;
	printf("Case #%d: %.8lf\n",Case,ans);

}

int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;++i)
	{
		Solve(i);
		//cout<<endl;
	}
}