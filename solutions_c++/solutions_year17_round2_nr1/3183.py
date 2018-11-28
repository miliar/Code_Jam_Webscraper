#include<bits/stdc++.h>
using namespace std;

#include <bits/stdc++.h>
using namespace std;

#ifdef DEBUG
     #define debug(args...)            {dbg,args; cerr<<endl;}
#else
    #define debug(args...)              // Just strip off all debug tokens
#endif

struct debugger
{
    template<typename T> debugger& operator , (const T& v)
    {
        cerr<<v<<" ";
        return *this;
    }
} dbg;



#define M 1000000007

int tree[1000000] = {0};

int a[100] = {0};

void build(int node, int start, int end)
{
    if(start == end)
    {

        tree[node] = a[start];
    }
    else
    {
        int mid = (start + end) / 2;

        build(2*node, start, mid);

        build(2*node+1, mid+1, end);

        tree[node] = tree[2*node] + tree[2*node+1];
    }
}

void modify(int node, int start, int end, int idx, int val)
{
    if(start == end)
    {

        a[idx] = val;
        tree[node] = val;
    }
    else
    {
        int mid = (start + end) / 2;
        if(start <= idx and idx <= mid)
        {

            modify(2*node, start, mid, idx, val);
        }
        else
        {

            modify(2*node+1, mid+1, end, idx, val);
        }

        tree[node] = tree[2*node] + tree[2*node+1];
    }
}

int query(int id,int start,int end,int l,int r)
{
    if(r < start or end < l)
    {

        return 0;
    }
    if(l <= start and end <= r)
    {

        return tree[id];
    }

    int mid = (start + end) / 2;
    int p1 = query(2*id, start, mid, l, r);
    int p2 = query(2*id+1, mid+1, end, l, r);
    return (p1 + p2);

}

bool prime [1000001];

int sieve(int a)
{
	memset(prime,true,sizeof(prime));
	int p;
	int i;
	for(p=2;p*p<=a;p++)
	{
		if(prime[p]==true)
		{
			for(i=p*2;i<=a;i+=p)
				prime[i]=false;
		}
	}
	return 0;
}

int binaryExponentiation(int x,int n)
{
    if(n==0)
        return 1;
    else if(n%2 == 0)        //n is even
        return binaryExponentiation(x*x,n/2);
    else                             //n is odd
        return x*binaryExponentiation(x*x,(n-1)/2);
}

int modularExponentiation(int x,int n)
{
    if(n==0)
        return 1;
    else if(n%2 == 0)        //n is even
        return modularExponentiation((x*x)%M,n/2);
    else                             //n is odd
        return (x*modularExponentiation((x*x)%M,(n-1)/2))%M;

}

vector <int> v[1000000];
int visited[1000000];
void dfs(int a)
{
	visited[a]=true;

	for(int i=0;i<v[a].size();i++)
	{
		if(visited[a]==false)
        {
		dfs(v[a][i]);
		visited[v[a][i]]=true;
        }
	}
}

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("output.out");
    int t;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
        double d;
        long long n;
        cin>>d>>n;
        double dis[n];
        double sp[n];
        double mx=0;
        for(long long j=0;j<n;j++)
        {
            cin>>dis[j]>>sp[n];
            dis[j]=d-dis[j];
            mx=max(mx,dis[j]/sp[n]);
        }
        //Case #1:
        cout<<"Case #"<<i<<": "<<setprecision(9)<<d/mx<<endl;
    }


}
