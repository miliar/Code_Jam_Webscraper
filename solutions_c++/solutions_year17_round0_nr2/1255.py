/*===============================================================
*  Filename£ºb.cpp
*  Author£ºzhuyutian
*  Date£º2017Äê04ÔÂ08ÈÕ
================================================================*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const int maxn = 100005;

int T;
char s[20];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	cin>>T;
	for(int kase = 1; kase <= T; kase ++)
	{
		cin>>s;
		printf("Case #%d: ",kase);
		int n = strlen(s);
		int p = 1;
		while(p < n)
		{
			if(s[p] < s[p-1]) break;
			p++;
		}
		if(p == n) cout<<s<<endl;
		else 
		{
			p -= 1;
			while(s[p] == s[p-1] && p) p--;
			s[p] -= 1;
			for(int i = p + 1; i < n; i++) s[i] = '9';
			if(p == 0 && s[p] == '0') p = 1;
			else p = 0;
			cout<<(s + p)<<endl;
		}
	}
    return 0;
}
