#include<bits/stdc++.h>
using namespace std;
typedef pair<int,char> ic;
char exc(char x)
{
	if(x >= 'a') return char(x-32);
	else return x;
}
void execute()
{
	int n,r,o,y,g,b,v;
	scanf("%d %d %d %d %d %d %d",&n,&r,&o,&y,&g,&b,&v);
	char cur = -1;
	vector<ic> a;
	string ans = "";
	a.push_back(ic(r,'R'));
	a.push_back(ic(y,'Y'));
	a.push_back(ic(b,'B'));
	sort(a.rbegin(),a.rend());
	a[0].second += 32;
	while(a[0].first>0)
	{
		bool ok = false;
		for(int i=0; i<a.size(); i++)
			if(a[i].second!=cur)
			{
				ok = true;
				ans += exc(a[i].second);
				a[i].first--;
				cur = a[i].second;
				break;
			}
		if(!ok)
		{
			printf("IMPOSSIBLE\n");
			return;
		}
		sort(a.rbegin(),a.rend());
	}
	if(ans[0] == ans[ans.size()-1] && ans.size()>1) ans = "IMPOSSIBLE";
	cout<<ans<<endl;
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++)
	{
		printf("Case #%d: ",tc);
		execute();
	}
	return 0;
}
