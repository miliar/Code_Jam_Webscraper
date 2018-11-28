#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define N ((ll)1050)
#define INF ((ll)3e18)

ifstream fin("input.in");
ofstream fout("output.txt");

ll t,n,r,o,y,g,b,v;

int main()
{
	//ios_base::sync_with_stdio(0);
	fin>>t;
	for(int q=1;q<=t;q++)
	{
		r=o=y=g=b=v=0;
		fin>>n;
		fin>>r>>o>>y>>g>>b>>v;
		fout<<"Case #"<<q<<": ";
		ll sum=r+o+y+g+b+v;
		if(o && (b<o || (b==o && sum!=b+o) || (b==o+1 && sum==b+o))){fout<<"IMPOSSIBLE\n";continue;}
		if(v && (y<v || (y==v && sum!=y+v) || (y==v+1 && sum==y+v))){fout<<"IMPOSSIBLE\n";continue;}
		if(g && (r<g || (r==g && sum!=r+g) || (r==g+1 && sum==r+g))){fout<<"IMPOSSIBLE\n";continue;}
		if(o && b==o){for(int i=0;i<o;i++)fout<<"BO";fout<<"\n";continue;}
		if(v && y==v){for(int i=0;i<v;i++)fout<<"YV";fout<<"\n";continue;}
		if(g && r==g){for(int i=0;i<g;i++)fout<<"RG";fout<<"\n";continue;}
		b-=o;y-=v;r-=g;
		vector <string> blue,yellow,red;
		for(int i=0;i<b;i++)blue.push_back("B");
		for(int i=0;i<y;i++)yellow.push_back("Y");
		for(int i=0;i<r;i++)red.push_back("R");
		for(int i=0;i<o;i++)blue[0]+="OB";
		for(int i=0;i<v;i++)yellow[0]+="VY";
		for(int i=0;i<g;i++)red[0]+="GR";
		string res="";
		ll lst=-1;
		bool flg=1;
		if(blue.size()<yellow.size())blue.swap(yellow);
		if(yellow.size()<red.size())red.swap(yellow);
		if(blue.size()<yellow.size())blue.swap(yellow);
		if(yellow.size()<red.size())red.swap(yellow);
		if(blue.size()<yellow.size())blue.swap(yellow);
		if(yellow.size()<red.size())red.swap(yellow);
		while(flg)
		{
			ll _b=blue.size(),_y=yellow.size(),_r=red.size();
			ll now=-1,maxi=0;
			if(!_b && !_r && !_y)break;
			if(lst!=0 && _b>maxi)now=0,maxi=_b;
			if(lst!=1 && _y>maxi)now=1,maxi=_y;
			if(lst!=2 && _r>maxi)now=2,maxi=_r;
			if(now==0)res+=blue.back(),blue.pop_back();
			if(now==1)res+=yellow.back(),yellow.pop_back();
			if(now==2)res+=red.back(),red.pop_back();
			if(now==-1)flg=0;
			lst=now;
		}
		if(!flg || (res.size()>1 && res[0]==res[(ll)res.size()-1]))fout<<"IMPOSSIBLE\n";
		else fout<<res<<"\n";
	}
	
	return 0;
}
