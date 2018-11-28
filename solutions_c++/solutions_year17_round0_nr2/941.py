/*
TASK: B. Tidy Numbers
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
	freopen("B-large.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int i,j,k;
	cin >> T;
	int tt=0;
	string s,a,b,c;
	while(T--)
	{
	    tt++;
	    cin >> s;
	    a="";
        for(i=0;i<s.size();i++)
        {
            if(i==0)
                a+=s[i];
            else
            {
                if(a[i-1]<=s[i])
                    a+=s[i];
                else
                {
                    b=a[i-1];
                    a=a.substr(0,a.find(b)+1);
                    a[a.size()-1]--;
                    break;
                }
            }
        }
        while(a.size()<s.size())
            a+='9';

        printf("Case #%d: %s\n",tt,a[0]=='0'? a.substr(1).c_str():a.c_str());
	}
	return 0;
}
