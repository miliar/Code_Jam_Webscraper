#include<iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <functional>
#include <windows.h>
//#include <array>

using namespace std;
struct Node
{
	int pos;
	double speed,c_t;
};
bool cmp(Node a,Node b)
{
	if(a.pos!=b.pos)return a.pos<b.pos;
	return a.c_t<b.c_t;
}
int main()
{
	int T;
	freopen("d:/codejam/A-large.in","r",stdin);
	freopen("d:/codejam/ALarge.out","w",stdout);
	cin>>T;
	int way_lens,N;
	for(int cas = 1;cas<=T;cas++)
	{
		cin>>way_lens>>N;
		vector<Node> nodes;
		double max_t = INT_MIN;
		for(int i=0;i<N;i++)
		{
			Node tmp;
			cin>>tmp.pos>>tmp.speed;
			tmp.c_t = (way_lens - tmp.pos)*1.0/tmp.speed;
			nodes.push_back(tmp);
			max_t = max(max_t,tmp.c_t);
		}
//		sort(nodes.begin(),nodes.end(),cmp);
//		double res = way_lens;;
//		if(max_t!=0)
		double	res = way_lens*1.0/max_t;
		printf("Case #%d: %.6f\n",cas,res);
	}
}
