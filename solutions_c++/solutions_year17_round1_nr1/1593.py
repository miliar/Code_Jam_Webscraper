/*
TASK: Alphabet Cake
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
string tb[30];
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int i,j,k;
	cin >> T;
	int tt=0;
	while(T--)
	{
	    cin >> N >> M;
	    for(i=0;i<N;i++)
            cin >> tb[i];
for(k=0;k<5;k++)
{
        for(i=0;i<N;i++)
        {
            char ch=0;
            for(j=0;j<M;j++)
            {
                if(tb[i][j]!='?')
                    ch=tb[i][j];
                else if(ch!=0)
                    tb[i][j]=ch;
            }
            ch=0;
            for(j=M;j>=0;j--)
            {
                if(tb[i][j]!='?')
                    ch=tb[i][j];
                else if(ch!=0)
                    tb[i][j]=ch;
            }
        }
        for(j=0;j<M;j++)
        {
            char ch=0;
            for(i=0;i<N;i++)
            {
                if(tb[i][j]!='?')
                    ch=tb[i][j];
                else if(ch!=0)
                    tb[i][j]=ch;
            }
            ch=0;
            for(i=N;i>=0;i--)
            {
                if(tb[i][j]!='?')
                    ch=tb[i][j];
                else if(ch!=0)
                    tb[i][j]=ch;
            }
        }
}
        tt++;
        printf("Case #%d:\n",tt);
        for(i=0;i<N;i++)
            printf("%s\n",tb[i].c_str());
	}
	return 0;
}
