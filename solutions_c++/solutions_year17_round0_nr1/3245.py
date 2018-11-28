// Dont hack this or I hack ur mama
#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#define ll long long 
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
using namespace std;

////////////// END OF TEMPLATE
int flipped[1100];
int solve(string s, int N);
void read()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T, N;
	cin >> T;
	for(int i = 0 ; i < T; i++)
	{
		string s;
		cin >> s >> N;
		for(int j=0;j<=1000;j++)flipped[j] = 0;
		int ret = solve(s,N);
		if(ret == -1)
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		else
			printf("Case #%d: %d\n",i+1,ret);
	}
}
int solve(string s, int N)
{
	//cout << s << ' ' << N << endl;	
	int cnt = 0, ret = 0;
	for(int i = s.length()-1;i>=N-1;i--)
	{
		if(cnt%2==1)
			s[i] = s[i]=='+'?'-':'+';
		if(s[i] == '-')
			cnt+=1,ret++,flipped[i]=1;
		cnt-=flipped[i+N-1];
	//	cout << cnt << ' '<< flipped[i] << endl;
	}
	for(int i = N-2;i>=0;i--)
	{
	
		if(cnt%2==1)
			s[i] = s[i]=='+'?'-':'+';
		if(s[i]=='-')
			return -1;
		cnt-=flipped[i+N-1];
	}
	return ret;
}
int main()
{
	std::ios::sync_with_stdio(false);
	read();
	return 0;
}
