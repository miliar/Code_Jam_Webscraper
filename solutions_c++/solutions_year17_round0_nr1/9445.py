
//yashverma

#include<bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for(int i=a;i<b;i++)
#define F first
#define S second
#define pb push_back
#define sqr(a) (a)*(a)
#define Pi 3.141592653589793
#define MOD 1000000007
#define INF 2000000000   // 2x10^9
#define m3 1003
#define m5 100005
#define m6 1000006
// For i/o
#define sd1(a) scanf("%d",&a)
#define sd2(a,b) scanf("%d %d",&a,&b)
#define sd3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sf scanf
#define pf printf
// For debugging
#define deb(a) printf("deb%d\n",a)

typedef pair<int,int> ii;
typedef long long ll;
typedef vector<int> vi;

int main()
{
	int t,k;
	cin >> t;
	int q = 1;
	while(t--)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;
		int len = s.length();
		int i = 0;
		while(i<=len-k)
		{
			while(s[i] == '+' && i <= len-k)
				i += 1;
			if(i > len-k)break;
			ans += 1;
			for(int j=0; j<k; j++)
			{
				if(s[i+j] == '+')s[i+j] = '-';
				else s[i+j] = '+';
			}
		}
		int flag = 1;
		rep(i,0,len)if(s[i] == '-')flag = 0;
		cout << "Case #" << q++ << ": " ;
		if(flag == 1)cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
