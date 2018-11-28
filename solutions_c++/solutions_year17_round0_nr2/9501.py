#include <bits/stdc++.h>
 
using namespace std; 
 
typedef long long ll; 
typedef pair<int, int> pii;
 
#define MOD 1000000007
#define INF 1000000000
#define pb push_back 
#define sz size() 
#define mp make_pair

#define REP(i,a,b) for(int i=a;i<b;i++)


int main()
{
	
	int t;
	unsigned long long n, a; 
	bool ok, flag;
	char c;
		
	cin >> t;
	REP(i, 0, t)
	{
		cin >> n;
		string s, p;
		
		while (true)
		{		
			flag = 0;
			stringstream ss, ss_;
			ss << n;
			ss >> s;

			REP(k,0,s.sz-1)
			{
				if (s[k]-'0' > s[k+1]-'0')
				{
					if (s[k]-'0' == 0)
					{
						p.pb('9');			
					}
					else{
						c = s[k];
						c--;
						p.pb(c);							
					}
					REP(j, k+1, s.sz)
						p.pb('9');

					flag = 1;
					break;
				}
				else 
					p.pb(s[k]);
			}
			if (p.sz < s.sz)
				p.pb(s[s.sz-1]);

			ok = true;
			REP(k,0,p.sz-1)
			{
				if (p[k]-'0' > p[k+1]-'0')
					{
						ok = false;
						break;
					}
			}			
			if(ok)
				break;

			ss_ << p;
			ss_ >> n;

			s.clear();
			p.clear();

		}
		
		stringstream ss3;
		ss3 << p;
		ss3 >> a;
	
		cout << "Case #" << i+1 << ": " << a << endl;
	}
	return 0;
}
