		/*masterwayne*/
#include<bits/stdc++.h>
using namespace std;
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define pf(x) printf("%d",x)
#define pf2(x,y) printf("%d %d",x,y)
#define pf3(x,y,z) printf("%d %d %d",x,y,z)
#define fr(i,x,n) for(int i=x;i<n;i++)
#define fre(i,x,n) for(int i=x;i<=n;i++)
#define fb(i,x,n) for(int i=n-1;i>=x;i--)
#define fbe(i,x,n) for(int i=n;i>=x;i--)
#define pfn() printf("\n")
#define pfs() printf(" ")
#define pb push_back
#define f_in(st) freopen(st,"r",stdin)
#define f_out(st) freopen(st,"w",stdout)
#define mod 1000000007
int mycompare(pair<int,int> p1,pair<int,int> p2)
{
	if(p1.first>=p2.second)
	{
		if(p1.first==p2.second)
		{
			return p1.second<p2.second;
		}
		return 1;
	}
	return 0;
}
struct lex_compare {
    bool operator() (const pair<int,int> &p1, const pair<int,int> &p2) const{
    	if(p1.first==p2.first)
    	return p1.second>p2.second;
    	return p1.first<p2.first;
    }
};
void solve(string input,string output)
{
	f_in(input.c_str());
	f_out(output.c_str());
	int t;
	cin>>t;
	int c=1;
	while(c<=t)
	{
		int n,k;
		cin>>n>>k;
		priority_queue<pair<int,int>,vector<pair<int,int>>,lex_compare> pq;
		pq.push({n,1});
		while(k)
		{
			pair<int,int> pi = pq.top();
			//cout<<pi.first<<" "<<pi.second<<endl;
			pq.pop();
			n = pi.first;
			int idx = pi.second;
			int left;
			int right;
			if(n&1)
			{
				left=n/2;
				right=n/2;
				if(left!=0)
				{
					pq.push({left,idx});
				}
				if(right!=0)
				{
					pq.push({right,idx+left+1});
				}
			}
			else
			{
				left = (n/2)-1;
				right = n/2;
				if(left!=0)
				{
					pq.push({left,idx});
				}
				if(right!=0)
				{
					pq.push({right,idx+left+1});
				}
			}
			k=k-1;
			if(k==0)
			{
				cout<<"Case #"<<c<<": "<<max(left,right)<<" "<<min(left,right)<<endl;
			}
		}
			//cout<<idx<<endl;
		c++;
	}
}
int main()
{
	solve("csmall2.in","cout22.txt");
	return 0;
}