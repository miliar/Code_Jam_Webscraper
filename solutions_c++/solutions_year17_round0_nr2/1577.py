#include<bits/stdc++.h>
using namespace std;
#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)
#define FOD(i,s,e) for(int i = (s); i >= (e); i--)
#define ll long long
#define pb push_back

int tc, tt;
char s[20], ans[20];
int n, x, w, k;

void output()
{
	printf("Case #%d: ", ++tt);
}

int main ()
{
	scanf("%d", &tc);
	
	while (tc--)
	{
		scanf("%s", s);
		n = strlen(s);
		
		output();
		
		x = -1;
		FOR(i, 1, n) if (s[i] < s[i - 1]) { x = i; break; }
		
		if (x == -1)
		{
			printf("%s\n", s);
			continue;
		}
	
		FOR(i, 0, n) ans[i] = s[i];
		
		FOD(i, n - 1, 0)
		{
			if (s[i] == '0') continue;
			s[i]--;
			FOR(j, i + 1, n) s[j] = '9';
			x = 0;
			FOR(j, 1, n) if (s[j] < s[j - 1]) x = 1;
			if (x == 0) break;
			FOR(j, 0, n) s[j] = ans[j]; 
		}
		
		FOR(i, 0, n) if (s[i] == '0') continue; else printf("%c", s[i]); 
		printf("\n");
	}
	
	return 0;
}
