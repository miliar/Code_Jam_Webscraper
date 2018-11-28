#include<iostream>
#include<vector>
#include<string>
using namespace std;
#define fs first
#define sc second
#define MAX 100000
#define pb push_back
#define mp make_pair
#define INF (1LL<<61)
#define MOD 1000000007
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;
int main()
{
	Int T;
	cin>>T;
	for (Int k=1;k<=T;++k)
	{
		string S;
		Int N,R,Y,B,x;
		cin>>N>>R>>x>>Y>>x>>B>>x;
		while (R--)
			S+='R';
		while (Y--)
		{
			Int n=S.size();
			bool flag=0;
			for (Int i=0;i<S.size();++i)
			{
				if (S[i]==S[(i+1)%n]&&S[i]!='Y')
				{
					S.insert((i+1)%n,"Y");
					flag=1;
					break;
				}
			}
			if (flag)
				continue;
			n=S.size();
			for (Int i=0;i<S.size();++i)
			{
				if (S[i]!='Y'&&S[(i+1)%n]!='Y')
				{
					S.insert((i+1)%n,"Y");
					flag=1;
					break;
				}
			}
			if (flag)
				continue;
			S+='Y';
		}
		while (B--)
		{
			Int n=S.size();
			bool flag=0;
			for (Int i=0;i<S.size();++i)
			{
				if (S[i]==S[(i+1)%n]&&S[i]!='B')
				{
					S.insert((i+1)%n,"B");
					flag=1;
					break;
				}
			}
			if (flag)
				continue;
			n=S.size();
			for (Int i=0;i<S.size();++i)
			{
				if (S[i]!='B'&&S[(i+1)%n]!='B')
				{
					S.insert((i+1)%n,"B");
					flag=1;
					break;
				}
			}
			if (flag)
				continue;
			S+='B';
		}
		printf("Case #%lld: ",k);
		Int n=S.size();
		bool flag=0;
		for (Int i=0;i<S.size();++i)
		{
			if (S[i]==S[(i+1)%n])
			{
				flag=1;
				break;
			}
		}
		if (flag)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		cout<<S<<"\n";
	}
	return 0;
}