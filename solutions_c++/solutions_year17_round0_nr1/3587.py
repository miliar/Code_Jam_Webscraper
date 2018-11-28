#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define pb push_back
#define sz(a) ((int)(a).size())
#define mp make_pair
#define fi first
#define se second

typedef pair<int,int> pint;
typedef long long ll;
typedef vector<int> vi;


#define MAX_N 1005

int n,k;
char s[MAX_N];

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		scanf("%s %d",s,&k);
		n=strlen(s);
		int ans=0;
		for (int i=0; i+k-1<n; i++)
			if (s[i]=='-')
			{
				ans++;
				for (int j=0; j<k; j++)
					s[i+j]=s[i+j]=='+'?'-':'+';
			}
		bool work=true;
		for (int j=0; j<k-1; j++)
			work&=s[n-1-j]=='+';
		printf("Case #%d: ",asdf);
		if (work)
			printf("%d\n",ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
