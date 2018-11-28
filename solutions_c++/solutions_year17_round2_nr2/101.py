#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <fstream>
#include <iterator>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)
typedef long long ll;

const int INF=1000000000;
const int MAXN=1000000;

struct Solver
{
	string solve(int b, int y, int r)
	{
		int n=r+y+b;
		string res(n,'-');
		priority_queue<pair<int,char> > q;
		q.push(make_pair(r,'R'));
		q.push(make_pair(y,'Y'));
		q.push(make_pair(b,'B'));
		int val;
		char sym;
		val=q.top().first;
		sym=q.top().second;
		q.pop();
		for(int i=0;i<n;i++)
			if(res[i]=='-')
			{
				for(int j=i;res[j]=='-';j=(j+2)%n)
				{
					res[j]=sym;
					val--;
					if(val==0 && !q.empty())
					{
						val=q.top().first;
						sym=q.top().second;
						q.pop();
					}
				}
			}
		return res;
	}
	string solve()
	{
		ostringstream out;
		// RYB
		// 001 B
		// 010 Y
		// 011 G
		// 100 R
		// 101 V
		// 110 O
		char colors[]=" BYGRVO";
		int n;
		cin>>n;
		char order[]="ROYGBV";
		int cnt[8]={};
		bool need[8]={};
		for(int i=0;i<6;i++)
		{
			int pos=strchr(colors, order[i])-colors;
			cin>>cnt[pos];
		}

		bool ok=true;
		bool answered=false;

		for(int i:{1,2,4})
			if(cnt[i]==cnt[i^7] && n==cnt[i]+cnt[i^7])
			{
				string tmp="",t="";
				tmp+=colors[i];
				tmp+=colors[i^7];
				for(int j=0;j<cnt[i];j++)
					t+=tmp;
				out<<t<<endl;
				answered=true;
				break;
			}

		for(int i:{3,5,6})
			if(cnt[i])
			{
				cnt[i^7]-=cnt[i];
				need[i^7]=true;
			}
		for(int i:{1,2,4})
			ok&=(cnt[i]>0 || (cnt[i]==0 && !need[i]));

		if(answered)
		{}
		else if(ok)
		{
			string res=solve(cnt[1], cnt[2], cnt[4]);
			for(int i:{3,5,6})
				if(cnt[i])
				{
					size_t pos=res.find(colors[i^7]);
					string tmp="",t="";
					tmp+=colors[i];
					tmp+=colors[i^7];
					for(int j=0;j<cnt[i];j++)
						t+=tmp;
					res=res.substr(0,pos+1)+t+res.substr(pos+1, res.length()-pos-1);
				}
			for(int i=0;i<n;i++)
				if(res[i]==res[(i+1)%n])
				{
					res="IMPOSSIBLE";
					break;
				}
			out<<res<<endl;
		}
		else
			out<<"IMPOSSIBLE"<<endl;
		return out.str();
	}
};

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
		printf("Case #%d: %s",test, Solver().solve().c_str());
	return 0;
}
