/*
TASK: Oversized Pancake Flipper
LANG: C++
*/
#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T;
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int i,j,k;
	cin >> T;
	string s;
	int tt=0,a,b,c;
	while(T--)
	{
	    tt++;
	    cin >> s >> k;
	    b=0;
	    for(i=0;i<=s.size()-k;i++)
        {
            if(s[i]=='-')
            {
                b++;
                for(j=i;j<i+k;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
//        printf("%s\n",s.c_str());
        if(s.find("-")!=-1)
            printf("Case #%d: IMPOSSIBLE\n",tt);
        else
            printf("Case #%d: %d\n",tt,b);
	}
	return 0;
}
