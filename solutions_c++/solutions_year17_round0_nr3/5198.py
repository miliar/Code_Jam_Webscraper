#include <bits/stdc++.h>
#define N 1010100
using namespace std;

vector < pair < int, int > > vet;

bool cmp(pair < int , int > a, pair < int , int > b)
{
	if(a.second-a.first+1 != b.second-b.first+1) return (a.second-a.first+1 > b.second-b.first+1);
	else if(a.first != b.first)  return (a.first < b.first);
	return a.second > b.second;
}

void back(int i, int j)
{
	if(i > j) return ;
	vet.push_back(make_pair(i, j));
	if(i == j) return ;
	int mid = (i+j)/2;
	back(i, mid-1);
	back(mid+1, j);
}

int main()
{
	int t, z=0;
	cin >> t;
	while (t--)
	{
		int n, k;
		cin >> n >> k;
		back(1, n);
		sort(vet.begin(), vet.end(), cmp);
		int x = vet[k-1].first, y = vet[k-1].second;
		int meio = (x+y)/2;
		cout << "Case #" << ++z << ": ";
		cout << max(abs(x-meio), abs(y-meio)) << ' ' << min(abs(x-meio), abs(y-meio)) << endl;
		vet.clear();
	}
}

