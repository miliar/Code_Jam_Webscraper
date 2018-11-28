#include <bits/stdc++.h>
#define ii pair<int, int>
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define vii vector< pair<int, int> >
typedef long long ll;
using namespace std;
int main()
{
    int tt;
    scanf("%d", &tt);
    for(int qq = 1; qq<= tt; qq++)
    {
        double clock_start = clock();
		int r, b, y, o, g, v;
		int n;
		vector<string> Red;
		vector<string> Blue;
		vector<string> Yell;
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		/*bool fail = 0;
		for(int i = 1; i<= 3; i++)
		{
			int x1, x2;
			switch(i)
			{
				case 1: x2 = o, x1 = b; break;
				case 2: x2 = g, x1 = r; break;
				case 3: x2 = v, x1 = y; break;
			}
			if(x2 == 0) continue;
			if(x1< x2+1) fail = 1;
			if(fail) break;
			int components = x1-x2;
			string c1, c2;
			switch(i)
			{
				case 1: c2 = 'O', c1 = 'B'; break;
				case 2: c2 = 'G', c1 = 'R'; break;
				case 3: c2 = 'V', c1 = 'Y'; break;
			}
			for(int j = 0; j< components-1; j++)
			{
				string top = c1+c2+c1;
				if(i == 1) Blue.pb(top);
				if(i == 2) Red.pb(top);
				if(i == 3) Yell.pb(top);
			}
			x1 -= components-1;
			string shi;
			for(int j = 0; j< x2; j++)
			{
				shi += c1+c2;
				x1--;
			}
			shi += c1; x1--;
			if(i == 1) Blue.pb(shi);
			if(i == 2) Red.pb(shi);
			if(i == 3) Yell.pb(shi);
			if(i == 1) b = x1;
			if(i == 2) r = x1;
			if(i == 3) y = x1;
		}
		while(b--) Blue.pb("B");
		while(r--) Red.pb("R");
		while(y--) Yell.pb("Y");
		b = Blue.size(); r = Red.size(); y = Yell.size();*/
		int sm = r+b+y;
		int mx = max(r, max(b, y));
		bool fail = 0;
		if(mx> sm-mx) fail = 1;
		char c1, c2, c3;
		int a1, a2, a3;
		if(mx == r)
		{
			c1 = 'R'; c2 = 'B'; c3 = 'Y';
			a1 = r; a2 = b; a3 = y;
		}
		else if(mx == b)
		{
			c1 = 'B'; c2 = 'R'; c3 = 'Y';
			a1 = b; a2 = r; a3 = y;
		}
		else if(mx == y)
		{
			c1 = 'Y'; c2 = 'R'; c3 = 'B';
			a1 = y; a2 = r; a3 = b;
		}
		int shi = sm-mx-mx;
		string res;
		for(int i = 0; i< mx; i++)
		{
			res += c1;
			if(i< a2) res += c2;
			else res += c3;
			if(i< shi) res += c3;
		}
		printf("Case #%d: ", qq);
		if(fail) printf("IMPOSSIBLE\n");
		else printf("%s\n", res.c_str());
		fprintf(stderr, "Test %d solved in %.2lf s.\n", qq, (clock()-clock_start)/CLOCKS_PER_SEC);
    }
	return 0;
}
