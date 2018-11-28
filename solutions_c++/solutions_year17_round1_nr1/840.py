#include <bits/stdc++.h>

using namespace std;
const double pi=acos(-1.0);
const double eps=1e-9;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define re return
#define vi vector <int> 
#define pii pair <int,int>
#define pll pair <long long , long long>
typedef long long ll;

const int N = 50;
int t,r,c,last;
string s[N];
bool Free[N];

void col(int t)
{
	int last = -1;
	for(int i=0;i<r;i++)
		if(s[i][t] != '?')
		{
			for(int j = last + 1;j<i;j++)
				s[j][t] = s[i][t];
			last = i;
		}
	for(int i = last + 1;i < r;i++)
		s[i][t] = s[last][t];
}

void copy(int t)
{
	for(int i=0;i<r;i++)
		s[i][t] = s[i][t + 1];
}

void revCopy(int t)
{
	for(int i=0;i<r;i++)
		s[i][t] = s[i][t - 1];
}

int main()
{
	ios:: sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> t;
	for(int test = 1;test <= t;test++)
	{
		cin >> r >> c;
		for(int i = 0;i<r;i++)
			cin >> s[i];
		for(int i=0;i<c;i++)
			Free[i] = true;
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
				if(s[i][j] != '?')Free[j] = false;
		last = -1;
		for(int i=0;i<c;i++)
		{
			if(Free[i])continue;
			col(i);
			for(int j = i -1; j > last;j--)
				copy(j);
			last = i;
		}
		for(int i=last+1;i<c;i++)
			revCopy(i);
		cout << "Case #" << test << ":\n";
		for(int i=0;i<r;i++)
			cout << s[i] << "\n";
	}
	return 0;
}
