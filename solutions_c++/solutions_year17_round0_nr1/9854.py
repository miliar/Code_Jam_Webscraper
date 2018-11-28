#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
// #include <unordered_map>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <bitset>
using namespace std;
#define ll long long int
#define MOD 1000000007
#define ull unsigned long long int
#define mp make_pair
#define pb push_back

void solve(void) {
	// ios::sync_with_stdio(false);
	string s;
	cin>>s;
	int k;
	cin>>k;

	int count=0;
	for(int i=0,j=s.size()-1;i<=j;i++,j--)
	{
		if(s[i]=='-')
		{
			int m=i;
			for(int l=0;l<k;l++)
			{
				s[m] = (s[m]=='+' ? '-':'+');
				m++;
			}
			count++;

		}
		if(s[j]=='-')
		{
			int m= j;
			for(int l=0;l<k;l++)
			{
				s[m] = (s[m]=='+' ? '-':'+');
				m--;
			}
			count++;
		}
	}
	// printf("%s\n", s);
	for(int i=0;i<s.size();i++)
	{
		if(s[i]=='-')
		{
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n", count);
	return;
}

int main(void) {
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for (int tn = 1; tn <= t; ++tn) {
		printf("Case #%d: ", tn);
		solve();
	}
	return 0;
}