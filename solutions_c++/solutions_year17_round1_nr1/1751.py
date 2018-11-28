#include <bits/stdc++.h>
 
#define long long long int
using namespace std;
 
#define Max 100005+5
#define cons 1000000000+7
#define mp make_pair
#define pb push_back
#define x first
#define y second

int main()
{
    ios::sync_with_stdio(false);cin.tie(0);

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;cin>>t;
    int case_No=0;

    while(t--)
    {
    	case_No++;   	
    	cout<<"Case #"<<case_No<<": ";

    	char arr[30][30];

    	char ans[30][30];

    	bool used[30][30];

    	int r,c;
    	cin>>r>>c;

    	for(int i=0;i<r;i++)
    		cin>>arr[i];

    	for(int i=0;i<r;i++)
    		for(int j=0;j<c;j++)
    			ans[i][j]='.';

    	// for(int i=0;i<r;i++)
    	// 	for(int j=0;j<c;j++)
    	// 		used[i][j]=false;

    		for(int i=0;i<r;i++)
    		{
    			for(int j=0;j<c;j++)
    			{
    				if(ans[i][j]=='.' && arr[i][j]=='?')
    				{
    					int row=-1,col=-1;bool flag=false;
    					
    							for(int l=j;l<c;l++)
    							if(arr[i][l]!='?')
    							{
    								row=i,col=l;
    								flag=true;
    								
    								break;
    							}
    							
    						

    						if(flag)
    						{
    							for(int k=i;k<=row;k++)
    								for(int l=j;l<=col;l++)
    									ans[k][l]=arr[row][col];
    						}
    				}
    				else if(ans[i][j]=='.' && arr[i][j]!='?')
    					ans[i][j]=arr[i][j];
    			}
    		}

    		for(int i=0;i<r;i++)
    		{
    			for(int j=0;j<c;j++)
    			{
    				if(ans[i][j]=='.' && j!=0)
    					ans[i][j]=ans[i][j-1];
    			}
    		}

    		for(int i=0;i<r;i++)
    		{
    			for(int j=0;j<c;j++)
    			{
    				if(ans[i][j]=='.' && i!=0)
    					ans[i][j]=ans[i-1][j];
    			}
    		}

    		for(int i=r-1;i>=0;i--)
    		{
    			for(int j=c-1;j>=0;j--)
    			{
    				if(ans[i][j]=='.')
    					ans[i][j]=ans[i+1][j];
    			}
    		}
    		
    		cout<<"\n";

    		for(int i=0;i<r;i++)
    		{
    			for(int j=0;j<c;j++)
    				cout<<char(ans[i][j]);
    			cout<<"\n";
    		}


    }
}





