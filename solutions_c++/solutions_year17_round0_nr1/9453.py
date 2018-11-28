// Simran Dokania
// International Institute of Information Technology Bangalore
#include <bits/stdc++.h>

using namespace std;

#define FASTER ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define pb push_back
#define mp make_pair
#define pd(x) printf("%d", x)
#define pdn(x) printf("%d\n", x)
#define plld(x) printf("%I64d", x)
#define plldn(x) printf("%I64d\n", x)
#define sd(x) scanf("%d",&x)
#define sd2(x,y) scanf("%d%d",&x,&y);
#define sd3(x,y,z) scanf("%d%d%d",&x,&y,&z); //spaces should not be there to avoid tle
#define slld(x) scanf("%I64d",&x)
#define LET(x, a)  __typeof(a) x(a)
#define foreach(it, v) for(LET(it, v.begin()); it != v.end(); it++)
#define tr(x) cout<<x<<endl;
#define tr2(x,y) cout<<x<<" "<<y<<endl;
#define tr3(x,y,z) cout<<x<<" "<<y<<" "<<z<<endl;
#define tr4(w,x,y,z) cout<<w<<" "<<x<<" "<<y<<" "<<z<<endl;
#define tr5(v,w,x,y,z) cout<<v<<" "<<w<<" "<<x<<" "<<y<<" "<<z<<endl;
#define tr6(u,v,w,x,y,z) cout<<u<<" "<<v<<" "<<w<<" "<<x<<" "<<y<<" "<<z<<endl;

/*
ifstream fin("input.txt");
ofstream fout("output.txt");
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
*/

int main()
{
	FASTER;
	int t, c = 1;
	cin >> t;
	while(t--)
	{
		int k;
		string s;
		cin >> s >> k;
		int l = s.length();
		int cnt = 0;
		for(int i = 0; i <= l-k; i++)
		{
			if(s[i] == '-')
			{
				cnt++;
				for(int j = i; j < i + k; j++)
				{
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		
		bool flag = false;
		for(int i = 0; i < l; i++)
		{
			if(s[i] == '-')
			{
				flag = true;
				break;
			}
		}
	
		cout << "Case #" << c++ << ": ";
		if(flag)
			cout << "IMPOSSIBLE\n";
		else
			cout << cnt << endl;
	}
	return 0;
}
