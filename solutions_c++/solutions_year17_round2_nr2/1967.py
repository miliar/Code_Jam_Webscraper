#include <bits/stdc++.h>
#define  mp make_pair
#define pb push_back
#define pf push_front
#define pp pop_back
#define ppf pop_front
#define fi first
#define se second
#define maxn 1000005

typedef long long ll;
using namespace std;
#define pi pair<int,int>


/*struct node
{
	int i;

	bool friend operator < (node a,node b)
	{
		return w[a.i]>w[b.i];
	}
};
priority_queue<node>pq;*/


int main()
{
	//ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
 	int q;
 	cin>>q;
 	int t1 = 0;
 	while(q--)
 	{
 		t1++;

 		int n;
 		cin>>n;
 		set<int> s[100];
 		s['R'-'A'].insert('B'),s['R'-'A'].insert('G'),s['R'-'A'].insert('Y');
 		s['B'-'A'].insert('O'),s['B'-'A'].insert('Y'),s['B'-'A'].insert('R');
 		s['Y'-'A'].insert('V'),s['Y'-'A'].insert('B'),s['Y'-'A'].insert('R');
 		s['V'-'A'].insert('Y'),s['O'-'A'].insert('B'),s['G'-'A'].insert('R');
 		string s1 = "ROYGBV";
 		vector<pi> v;
 		for(int i=0;i<6;i++)
 		{
 			int num;
 			cin>>num;
 			v.pb(mp(num,s1[i]-'A'));
		}
		char fin[n+1];
		sort(v.begin(),v.end());
		int x = v[5].fi;
		char ch = v[5].se+'A';
		v[5].fi--;
		fin[0] = ch;
		int flag = 0;
	//	cout<<ch<<endl;
		for(int i=4;i>=1;i--)
		{
			char ch1 = v[i].se+'A';
			//cout<<ch1<<" "<<v[i].fi<<endl;
			if(v[i].fi>0&&s[ch-'A'].find(ch1)!=s[ch-'A'].end())
			{
				fin[n-1] = ch1;
				v[i].fi--;
				flag = 1;
				break;
			}
		}
		//cout<<flag<<endl;
		//cout<<fin[n-1]<<endl;
		sort(v.begin(),v.end());
		cout<<"Case #"<<t1<<": ";
		if(!flag)
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		//set<int>::iterator it;
	//	for(int i=0;i<6;i++) ch = v[i].se+'A',cout<<v[i].fi<<" "<<ch<<endl;
		flag = 0;
		for(int i=1;i<n-1;i++)
		{
			int ch1 = fin[i-1]-'A';
			int mar = 0;
			for(int j=5;j>=0;j--)
			{
				char ch2 = v[j].se+'A';
				if(ch2==ch1) continue;
				//char ch2 = v[j].se+'A';
				//cout<<v[j].fi<<" "<<ch2<<endl;
				if(v[j].fi>0&&s[ch1].find(ch2)!=s[ch1].end())
				{
					//cout<<fin[i-1]<<" "<<v[j].fi<<" "<<ch2<<endl;
					fin[i] = ch2;
					v[j].fi--;
					mar  =1;
					break;
				}
			}
			//cout<<"y"<<fin[i-1]<<" "<<mar<<endl;
			if(mar==0)
			{
				flag = 1;
				break;
			}
			sort(v.begin(),v.end());
		}
		if(flag)
		cout<<"IMPOSSIBLE"<<endl;
		else
		{
			if(fin[n-1]==fin[n-2]) swap(fin[n-2],fin[n-3]);
			for(int i=0;i<n;i++) cout<<fin[i];
			cout<<endl;
		}
	}
}
