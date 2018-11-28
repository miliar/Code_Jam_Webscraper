#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
string onecolor(int one,int doubl,char f,char s)
{
	string res;
	for(int i=0;i<doubl;i++)
		res=(res+f)+s;
	for(int i=0;i<one-doubl;i++)
		res+=f;
	return res;
}
string build(int r,int b,int y,string R,string B,string Y)
{
	vector<pair<int,pair<char,string>>>V={{r,{'R',R}},{b,{'B',B}},{y,{'Y',Y}}};
	sort(V.begin(),V.end());
	if (V[2].first>V[1].first+V[0].first)
		return "IMPOSSIBLE";

	string res;
	bool avail[3]={true,true,true};
	for(int i=0;i<V[2].first;i++)
	{
		if(avail[2])
		{
			res+=V[2].second.second;
			avail[2]=false;
		}
		else
			res.push_back(V[2].second.first);
		if(i<V[0].first)
		{
			if(avail[0])
			{
				res+=V[0].second.second;
				avail[0]=false;
			}
			else
				res.push_back(V[0].second.first);
		}
		if(i>=V[2].first-V[1].first)
		{
			if(avail[1])
			{

				res+=V[1].second.second;
				avail[1]=false;
			}
			else
				res.push_back(V[1].second.first);
		}
	}
	return res;
}
string test()
{
	int n,r,nb,y,nr,b,ny;
	scanf("%d%d%d%d%d%d%d",&n,&r,&nb,&y,&nr,&b,&ny);
	//return onecolor(r,nr,'R','G')+onecolor(b,nb,'B','O')+onecolor(y,ny,'Y','V');
	if(y+ny+r+nr==0 and b==nb)return onecolor(b,nb,'B','O');
	if(r+nr+b+nb==0 and y==ny)return onecolor(y,ny,'Y','V');
	if(y+ny+b+nb==0 and r==nr)return onecolor(r,nr,'R','G');
	string R,B,Y;
	if(nr and r<nr+1)return "IMPOSSIBLE";
	if(nb and b<nb+1)return "IMPOSSIBLE";
	if(ny and y<ny+1)return "IMPOSSIBLE";
	R=onecolor(nr+1,nr,'R','G');
	B=onecolor(nb+1,nb,'B','O');
	Y=onecolor(ny+1,ny,'Y','V');
	r-=nr;
	y-=ny;
	b-=nb;
	return build(r,b,y,R,B,Y);

}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		auto res=test();
		printf("Case #%d: %s\n",i,res.c_str());
	}
}
