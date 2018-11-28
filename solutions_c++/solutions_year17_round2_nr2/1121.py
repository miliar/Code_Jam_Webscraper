#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define cerr while(0)cerr
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		int N;
		cin>>N;
		int r, o, y, g, b, v;
		cin>>r>>o>>y>>g>>b>>v;
		cout<<"Case #"<<t<<": ";
		if (r > N/2 || b > N/2 || y > N/2)
		{	
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		pair<int, char> p[3];
		p[0] = make_pair(r, 'R');
		p[1] = make_pair(b, 'B');
		p[2] = make_pair(y, 'Y');
		sort(p, p+3);
		reverse(p, p+3);
		cerr<<p[0].first<<' '<<p[1].first<<' '<<p[2].first<<'\n';
		cerr<<p[0].second<<' '<<p[1].second<<' '<<p[2].second<<'\n';
		char arr[N];
		memset(arr, -1, sizeof arr);
		for (int i = 0; i < p[0].first; ++i)
		{
			cerr<<2*i<<' ';
			arr[2*i] = p[0].second;
		}
		cerr<<'\n';
		int start = N-1;
		if (N % 2 == 1) --start;
		for (int i = 0; i < p[1].first; ++i)
		{
			cerr<<start-2*i<<' ';
			arr[start - 2*i] = p[1].second;
		}
		cerr<<'\n';
		for (int i = 0; i < N; ++i)
		{
			if (arr[i] == -1)
				{
					cerr<<i<<' ';
				arr[i] = p[2].second;
				}
		}
		cerr<<'\n';
		for (int i = 0; i < N; ++i)
		{
			cout<<arr[i];
		}
		cout<<'\n';
	}
}