#include <cstdio>
#include <string>
#include <queue>

std::string rgb(int r, int y, int b)
{
    std::string cr = "R", cy = "Y", cb = "B";
    if(r < y) { std::swap(r, y); std::swap(cr, cy); }
    if(r < b) { std::swap(r, b); std::swap(cr, cb); }
    //if(y < b) { std::swap(y, b); std::swap(cy, cb); }

    //fprintf(stderr, "ryb = %d %d %d\n", r, y, b);
    if(r > y + b) return "";
    
    std::string res = "";
    while(r)
    {
	if(r == y && r == b) { res += cr + cy + cb; r--; y--; b--; }
	else if(y > b) { res += cr + cy; r--; y--; }
	else { res += cr + cb; r--; b--; }

	if(r < y || r < b) { fprintf(stderr, "wtf\n"); }
    }

    if(r || y || b) { fprintf(stderr, "wat\n"); }
    
    return res;
}

std::string alt(int n, char a, char b)
{
    std::string res = "";
    while(n--)
    {
	res += a; res += b;
    }
    return res;
}

bool check(int r, int y, int b, std::string s)
{
    int n = s.length();
    char prev = s[n - 1];
    for(char c : s)
    {
	if(c == prev) return false;
	if(c == 'R') r--;
	else if(c == 'Y') y--;
	else if(c == 'B') b--;
	else return false;
	prev = c;
    }

    if(r || y || b) return false;
    return true;
}

int main()
{
    int tests;
    scanf("%d", &tests);
    for(int test = 1; test <= tests; test++)
    {
	printf("Case #%d: ", test);
	
	int n, r, o, y, g, b, v;
	scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);

	std::string res;
	if(r + g == n)
	{
	    if(r == g) res = alt(r, 'R', 'G');
	    else res = "";
	}
	else if(b + o == n)
	{
	    if(b == o) res = alt(b, 'B', 'O');
	    else res = "";
	}
	else if(y + v == n)
	{
	    if(y == v) res = alt(y, 'Y', 'V');
	    else res = "";
	}
	else
	{
	    r -= g;
	    b -= o;
	    y -= v;

	    if((r <= 0 && g) || (y <= 0 && v) || (b <= 0 && o)) res = "";
	    else
	    {
		std::string t = rgb(r, y, b);
	        res = "";

		if(t.length())
		{
		    for(char c : t)
		    {
			res += c;
			while(c == 'R' && g) { res += "GR"; g--; }
			while(c == 'B' && o) { res += "OB"; o--; }
			while(c == 'Y' && v) { res += "VY"; v--; }
		    }

		    if(g || o || v) fprintf(stderr, "g||o||v: %d %d %d!\n", g, o, v);
		}
	    }
	}
	
	if(res.length())
	{
	    //if(!g && !v && !o) if(!check(r, y, b, res)) fprintf(stderr, "err @ %d\n", test);
	    printf("%s\n", res.c_str());
	}
	else
	{
	    fprintf(stderr, "imp %d %d %d\n", r, y, b);
	    printf("IMPOSSIBLE\n");
	}
    }

    return 0;
}
