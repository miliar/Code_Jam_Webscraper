#include<bits/stdc++.h>
using namespace std;
int a[1500],mat[1500][1500][3][3];
int MM = 1000000010;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);


    int t,n,i,j,k,l,m,x;
    cin>>t;

    for(int trm=1;trm<=t;trm++)
    {
        cout<<"Case #"<<trm<<": ";
    	cin>>n>>m;

    	memset(a,0,sizeof a);

    	for(i=0;i<=1440;i++)
    	{
    		for(j=0;j<=1440;j++)
    		{
    			mat[i][j][1][1]=MM;
    			mat[i][j][1][2]=MM;

    			mat[i][j][2][1]=MM;
    			mat[i][j][2][2]=MM;
    		}
    	}


    	for(i=0;i<n;i++)
    	{
    		cin>>j>>k;

    		for(l=j;l<k;l++)
    			a[l]=1;
    	}

    	for(i=0;i<m;i++)
    	{
    		cin>>j>>k;

    		for(l=j+1;l<=k;l++)
    			a[l]=2;
    	}

        //base cases
    	if(a[1]==1)
    	{
    		mat[1][1][1][1]=0;
    	}
    	else if(a[1]==2)
    	{
    		mat[1][0][2][2]=0;
    	}
    	else
    	{
    		mat[1][1][1][1]=0;
    		mat[1][0][2][2]=0;
    	}

    	for(i=2;i<=1440;i++)
    	{
    		if(a[i]!=1)
    		{
    			mat[i][0][1][2]=mat[i-1][0][1][2];  mat[i][0][2][2]=mat[i-1][0][2][2];
    		}


    		for(j=1;j<=min(i,720);j++)
    		{
    			if(a[i]==1)
    			{
    			    mat[i][j][2][1]=min(mat[i-1][j-1][2][2]+1,mat[i-1][j-1][2][1]);
    				mat[i][j][1][1]=min(mat[i-1][j-1][1][2]+1,mat[i-1][j-1][1][1]);

    			}
    			else if(a[i]==2)
    			{
    			    mat[i][j][2][2]=min(mat[i-1][j][2][1]+1,mat[i-1][j][2][2]);
    				mat[i][j][1][2]=min(mat[i-1][j][1][1]+1,mat[i-1][j][1][2]);

    			}
    			else
    			{
    				mat[i][j][1][1]=min(mat[i-1][j-1][1][2]+1,mat[i-1][j-1][1][1]);

    				mat[i][j][2][2]=min(mat[i-1][j][2][1]+1,mat[i-1][j][2][2]);

    				mat[i][j][2][1]=min(mat[i-1][j-1][2][2]+1,mat[i-1][j-1][2][1]);

    				mat[i][j][1][2]=min(mat[i-1][j][1][1]+1,mat[i-1][j][1][2]);
    			}
    		}
    	}


    	k=MM;


    	for(i=1;i<=2;i++)
    	{
    		for(j=1;j<=2;j++)
    			k=min(k,mat[1440][720][i][j]+abs(i-j));
    	}
    	cout<<k<<endl;
    }

}
