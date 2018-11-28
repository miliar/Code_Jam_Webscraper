#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> ii;

double m[1000];
int D,N;
ii h[1000];

int main()
{
	int T; cin>>T;
	for (int t=1;t<=T;t++)
	{
		cout<<"Case #"<<t<<": ";
		cin>>D>>N;
		for (int i=0;i<N;i++) cin>>h[i].first>>h[i].second;
		sort(h,h+N);
		m[N-1]=h[N-1].second;
		for (int i=N-2;i>=0;i--)
		{
			double c=h[i].first+h[i].second*((double)(h[i+1].first-h[i].first)/(h[i].second-m[i+1]));
			if (h[i].second<=m[i+1] || c>=D)
				m[i]=h[i].second;
			else
				m[i]=((double)D-h[i].first)/((c-h[i].first)/h[i].second + (D-c)/m[i+1]);
		}
		printf("%.6lf\n", (double)D/((D-h[0].first)/m[0]));
	}
}