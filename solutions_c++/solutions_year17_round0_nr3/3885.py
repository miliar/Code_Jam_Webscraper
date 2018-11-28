#include <bits/stdc++.h>
 
#define long long long int
using namespace std;
 
#define Max 100005+5
#define cons 1000000000+7
#define mp make_pair
#define pb push_back
#define INF 1e12
#define INF2 1e9+9
#define pi 3.141592653589
#define x first
#define y second

int group_size[1000000+5]; 

int main()
{
    ios::sync_with_stdio(false);cin.tie(0);

    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;cin>>t;
    int case_No=0;
    // cout<<t<<endl;

    while(t--)
    {
    	case_No++;   	
    	cout<<"Case #"<<case_No<<": ";
    	// cout<<endl;

    	int n,k;cin>>n>>k;

    	for(int i=0;i<=n;i++)group_size[i]=0;
    		group_size[n]=1;

    	int i;

    	for(i=n;i>=0;i--)
    	{
    		if(group_size[i]!=0)
    		{
    			if(group_size[i]>k-1)break;
    			
    			group_size[i>>1]+=group_size[i];
    			group_size[(i-1)>>1]+=group_size[i];
    			k-=group_size[i];
    		}
    	}
    	int lenInterval=i;
    	// cout<<lenInterval<<endl;

    	if(lenInterval&1)
    	{
    		cout<<lenInterval/2<<" "<<(lenInterval>>1)<<"\n";
    	}
    	else
    	{
    		cout<<(lenInterval/2)<<" "<<(lenInterval>>1)-1<<"\n";
    	}
    }
}





