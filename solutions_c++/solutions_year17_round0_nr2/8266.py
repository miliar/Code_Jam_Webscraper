#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int digit[20];
int64_t dp[20][10];

int64_t dfs(int len,int pre,bool up)
{
    if(!len) return 1;
	if(!up && dp[len][pre]!=-1) return dp[len][pre];
	int64_t ans=0,mx=(up?digit[len]:9);
	for(int i=pre;i<=mx;i++)
		ans+=dfs(len-1,i,up && (i==mx));
	if(!up) dp[len][pre]=ans;
	return ans;
}

int64_t solve(int64_t x)
{
    for(int i=0;i<20;i++)
        for(int j=0;j<10;j++)
            dp[i][j]=-1;

	int len=0;
	while(x)
	{
		digit[++len]=x%10;
		x/=10;
	}
	return dfs(len,0,1)-1;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.txt","w",stdout);

    int T,Case=1;
    cin>>T;
    while(T--)
    {
        cout<< "Case #" << Case++ << ": ";

        int64_t n;
        cin>>n;

        //cout<<solve(n)<<endl;

        int64_t num=solve(n)-1;

        int64_t l=0,r=n-1;

        while(l<r)
        {
            int64_t m=(l+r+1)>>1;
            if(solve(m)>num) r=m-1;
            else l=m;
        }

        cout<<l+1<<endl;
    }
    return 0;
}

