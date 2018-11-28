#include <bits/stdc++.h>
using namespace std;
multiset<string> rs;
multiset<string> rys;
#define mp(a,b) make_pair(a,b)
#define X first
#define Y second
int main()
{
	int t;
	cin>>t;
	int ci=1;
	while(t--)
	{
		int n;
		int r,o,y,g,b,v;
		int n1;
		cin>>n>>r>>o>>y>>g>>b>>v;
		n1=n;
		cout<<"Case #"<<ci<<": ";
		ci++;
		vector<pair<int,string> > s;
		vector<pair<int,string> > q;
		s.push_back(make_pair(r,"R") );
		s.push_back(make_pair(y,"Y") );
		s.push_back(make_pair(b,"B") );
		q.push_back(make_pair(g,"G") );
		q.push_back(make_pair(v,"V") );
		q.push_back(make_pair(o,"O") );
		bool impos=false;
		for(int i=0;i<=2;i++)
		{
			if(q[i].X>s[i].X)
			{
				impos=true;
				cout<<"IMPOSSIBLE"<<endl;
				break;
			}
			if(s[i].X==0&&q[i].X!=0)
			{
				impos=true;
				cout<<"IMPOSSIBLE"<<endl;
				break;
			}
			if(s[i].X==0&&q[i].X==0)
				continue;
			if(s[i].X==q[i].X)
			{
				if((s[i].X+q[i].X)!=n)
				{
					//cout<<(s[i].X+q[i].X)<<endl;
					//cout<<n<<endl;
					cout<<"IMPOSSIBLE"<<endl;
					//cout<<"here"<<endl;
					impos=true;
					break;
				}
				//check other non-zero values
				bool posi=true;
				for(int j=0;j<=2;j++)
				{
					if(j==i)
						continue;
					if(s[j].X!=0||q[j].X!=0)
						posi=false;
				}
				if(!posi)
				{
					impos=true;
					cout<<"IMPOSSIBLE"<<endl;
					//cout<<"asa"<<endl;
					break;
				}
				string ret="";
				for(int j=0;j<s[i].X;j++)
					ret+=(s[i].Y+q[i].Y);
				cout<<ret<<endl;
				impos=true;
			}
		}
		if(impos)
			continue;
		//q[i].X<s[i].X || both are 0
		for(int i=0;i<=2;i++)
			s[i].X-=q[i].X;
		sort(s.begin(),s.end());
		n=s[0].X+s[1].X+s[2].X;
		//cout<<(n/2)<<endl;
		if((s[2].first)>(n/2))
		{
			//cout<<s[2].first<<endl;
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		int cur=0;
		rs.clear();
		rys.clear();
		for(int i=1;i<=s[2].first;i++)
			rs.insert(s[2].second);
		for(int i=1;i<=s[1].first;i++)
		{
			set<string>::iterator it=rs.begin();
			string x=*it;
			rs.erase(it);
			x=s[1].second+x;
			rys.insert(x);
		}
		string ans="";
		for(int i=1;i<=s[0].first;i++)
		{
			if((int)rs.size()==0)
			{
				set<string>::iterator it=rys.begin();
				string x=*it;
				rys.erase(it);
				x=s[0].second+x;
				ans+=x;
			}
			else
			{
				set<string>::iterator it=rs.begin();
				string x=*it;
				rs.erase(it);
				x=s[0].second+x;
				ans+=x;
			}
		}
		while(!rys.empty())
		{
			set<string>::iterator it=rys.begin();
			string x=(*it);
			ans+=x;
			rys.erase(it);
		}
		while(!rs.empty())
		{
			set<string>::iterator it=rs.begin();
			string x=(*it);
			ans+=x;
			rs.erase(it);
		}
		//s.push_back(make_pair(r,"R") );
		//s.push_back(make_pair(y,"Y") );
		//s.push_back(make_pair(b,"B") );
		//reinsert into ans
		int yy=0;
		for(int i=0;i<ans.size();i++)
		{
			int oth;
			if(ans[i]=='R')
				oth=0;
			if(ans[i]=='Y')
				oth=1;
			if(ans[i]=='B')
				oth=2;
			yy++;
			if(q[oth].X==0)
				cout<<ans[i];
			else{
				cout<<ans[i];
				while(q[oth].X>0)
				{
					cout<<q[oth].Y<<ans[i];
					q[oth].X--;
					yy+=2;
				}
			}
		}
		cout<<endl;
		assert(yy==n1);
		//cout<<ans<<endl;
	}
	return 0;
}
