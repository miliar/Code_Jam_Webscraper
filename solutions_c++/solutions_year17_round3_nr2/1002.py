#include <bits/stdc++.h>
using namespace std;

int maxrange(vector< pair<int,int> > a)
{
	sort(a.begin(),a.end());	
	return min(a[1].second-a[0].first, 1440+a[0].second-a[1].first );
}

void query()
{
	vector< pair<int,int> > ctasks;
	vector< pair<int,int> > jtasks;
	int ac, aj;
	cin >> ac >> aj;	
	for (int i=0;i<ac;i++)
	{
		int ci, di;
		cin >> ci >> di;
		ctasks.push_back(make_pair(ci,di));
	}
	for (int i=0;i<aj;i++)
	{
		int ji, ki;
		cin >> ji >> ki;
		jtasks.push_back(make_pair(ji,ki));
	}
	int minswap=1;
	if ((ac == 0) && (aj == 0))
	{
		cout << 2 << endl;
		return;
	}
	if ((ac == 1) && (aj == 0))
	{
		cout << 2 << endl;
		return;
	}
	if ((ac == 0) && (aj == 1))
	{
		cout << 2 << endl;
		return;
	}
	if ((ac == 2) && (aj== 0))
	{
		auto k=maxrange(ctasks);
		if (k > 720)
		{
			cout << 4 << endl;
		} else
		{
			cout << 2 << endl;
		}
		return;
	}
	if ((ac == 0) && (aj== 2))
	{
		auto k=maxrange(jtasks);
		if (k > 720)
		{
			cout << 4 << endl;
		} else
		{
			cout << 2 << endl;
		}
		return;
	}
	if ((ac==1) && (aj == 1))
	{
		cout << 2 << endl;
		return;
	}
	cout << -1 << endl;
}
	
int main()
{	
	ios::sync_with_stdio(false);	
	int q;
	cin >> q;
	for (int i=0;i<q;i++)
	{
		cout << "Case #"<<i+1<<": ";
			query();
	}
}