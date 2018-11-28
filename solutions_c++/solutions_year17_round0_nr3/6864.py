#include<iostream>
#include<vector>
#include<set>
#include<queue>
#include<fstream>
using namespace std;
typedef long long ll;
int main()
{
	//ofstream fout("C:\\rei\\Document.txt");
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int ii=0;ii<t;ii++)
	{
		ll n,k;
		cin>>n>>k;
		set<int> s1;
		set<int> s2;
		cout<<"Case #"<<ii+1<<": ";
 
		s1.insert(-0);
		s1.insert(-(n+1));
		s2.insert(0);
		s2.insert(n+1);
		priority_queue<pair<pair<ll,ll>,ll> > qi;
		int broj1=0;
		int broj2=n+1;
		qi.push(make_pair(make_pair(((broj1+broj2)/2-broj1),(broj2-(broj1+broj2)/2)),-(broj1+broj2)/2));
		for(int i=0;i<k;i++)
		{
			int index=-qi.top().second;
			qi.pop();
			broj1=-*s1.lower_bound(-index);
			broj2=*s2.lower_bound(index);
			if(i==k-1)
			{
				cout<<broj2-(broj1+broj2)/2-1<<' '<<(broj1+broj2)/2-broj1-1<<endl;
			}
			qi.push(make_pair(make_pair(((broj1+index)/2-broj1),(index-(broj1+index)/2)),-(broj1+index)/2));
			qi.push(make_pair(make_pair(((index+broj2)/2-index),(broj2-(index+broj2)/2)),-(index+broj2)/2));
			s1.insert(-index);
			s2.insert(index);
		}
	}
	return 0;
}