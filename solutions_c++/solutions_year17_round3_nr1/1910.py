/*input
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
*/

#include<bits/stdc++.h>
using namespace std;
using pii = pair< long long , long long >;
bool comp(pii &a, pii &b)
{
	if(a.first == b.first) return a.second>b.second;
	return a.first>b.first;
}
bool comp2(pii &a, pii &b)
{
	return a.first*a.second>b.first*b.second;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t, tst = 1;
    cin >> t;
    while(t--)
    {
    	int n, k;
    	cin >> n >> k;
    	pii ara[n];
    	for(int i = 0; i<n; i++)
    		cin >> ara[i].first >> ara[i].second ;
    	double ans = -1;
    	sort(ara, ara+n, comp);
    	long long maxi = 0;
    	for(int i = 0; i<n-k+1; i++)
    	{
    		long long x = 0, m = ara[i].first * ara[i].first + 2 * ara[i].first * ara[i].second;
    		vector< pii > vt;
    		for(int j = i+1; j<n; j++)
    			vt.push_back(ara[j]);
    		sort(vt.begin(), vt.end(), comp2);
    		for(int j = 0; j<k-1; j++)
    			x += vt[j].first * vt[j].second * 2;
    		if(x + m >= maxi) maxi = x + m;
    	}
    	ans = acos(-1.0) * maxi;

    	printf("Case #%d: ", tst++);
    	cout << fixed << setprecision(10) << ans << endl;
    }
	return 0;
}