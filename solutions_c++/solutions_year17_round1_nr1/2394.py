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
vector<int> bl[maxn];
int sz;
int a[maxn];

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
 
	int t;
	cin>>t;
	int q =1;
	while(t--)
	{
		int r,c;
		cin>>r>>c;
		char ch[40][40];
		//int mark[100] = {0};
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				cin>>ch[i][j];
				
			}
		}
		cout<<"Case #"<<q<<":"<<endl;
		q++;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(ch[i][j]=='?')
				{
					int flag = 0;
					for(int i1=j-1;i1>=0;i1--)
					{
						if(ch[i][i1]!='?')
						{
							ch[i][j] = ch[i][i1];
							flag = 1;
							break;
						}
					}
					if(!flag)
					{
						for(int i1=j+1;i1<c;i1++)
						{
							if(ch[i][i1]!='?')
							{
								ch[i][j] = ch[i][i1];
							flag = 1;
							break;
							}
						}
						
					}
				}
			}
		}
		int mark = 0;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(ch[i][j]=='?')
				{
					 mark = 0;
					for(int k=i+1;k<r;k++)
					{
						if(ch[k][0]!='?'){
							mark = 1;
							for(int j=0;j<c;j++) ch[i][j] = ch[k][j];
							break;
						}
					}
					if(mark==0)
					{
						for(int k=i-1;k>=0;k--)
					{
						if(ch[k][0]!='?'){
							mark = 1;
							for(int j=0;j<c;j++) ch[i][j] = ch[k][j];
							break;
						}
					}
					}
				}
			}
		}
		
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++) cout<<ch[i][j];
			cout<<endl;
		}
	}
	return 0;
}  