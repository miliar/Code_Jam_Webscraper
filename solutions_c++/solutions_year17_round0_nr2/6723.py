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

int n,t;
string s;

int main()
{
	ios:: sync_with_stdio(false);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin >> t;
	for(int test = 1;test<=t;test++)
	{
		cin >> s;
		n = s.size();
		for(int i = n - 2;i >= 0;i--)
			if(s[i] > s[i + 1])
			{
				s[i]--;
				for(int j=i+1;j<n;j++)
					s[j] = '9';
			}
		cout << "Case #" << test << ": ";
		if(s[0] == '0')
			for(int i=0;i<n-1;i++)
				cout << '9';
		else
			for(int i=0;i<n;i++)
				cout << s[i];
		cout << "\n";
	}
	return 0;
}
