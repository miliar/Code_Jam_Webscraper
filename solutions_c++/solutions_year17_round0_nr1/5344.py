#include<bits/stdc++.h>
using namespace std;
char x[1005];
string s,tmp,com;
int main()
{
	int t;
	scanf("%d",&t);
//	freopen("w","op.txt",stdout);
	for(int l=1;l<=t;l++)
	{
		bool chk=true;
		queue<pair<string,int> > q;
		map<string,int> mp;
		int n;
		com="";
		scanf("%s",x);
		s=x;
		for(int i=0;i<s.size();i++)
		{
			com+="+";
		}
		scanf("%d",&n);
		q.push(make_pair(s,0));
//		printf("%s\n",com.c_str());
		while(!q.empty())
		{
			tmp=q.front().first;
			int mov=q.front().second;
			q.pop();
//			printf("%s\n",tmp.c_str());
			if(tmp==com)
			{
				printf("Case #%d: %d\n",l,mov);
				chk=false;
				break;
			}
			string tmp2;
//			printf("C\n");
			for(int i=0;i<s.size()-n+1;i++)
			{
				tmp2=tmp;
				for(int j=i;j<i+n;j++)
				{
					if(tmp2[j]=='+')
					{
						tmp2[j]='-';
					}
					else
					{
						tmp2[j]='+';
					}
				}
//				printf("%s %s\n",tmp.c_str(),tmp2.c_str());
				if(mp.find(tmp2)==mp.end())
				{
					mp[tmp2]=1;
					q.push(make_pair(tmp2,mov+1));
				}
			}
		}
		while(!q.empty())
			q.pop();
		if(chk)
		{
			printf("Case #%d: IMPOSSIBLE\n",l);
		}
	}
}
