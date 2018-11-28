#include <iostream>
using namespace std;

int main() {
	// your code goes here
	char ch[30][30];
	int t,n,m,l,p,i,j,tc,k;
	cin>>t;
	tc=1;
	while(t--)
	{
	    cout<<"Case #"<<tc<<":\n";
	    tc++;
	    cin>>n>>m;
	    for(i=0;i<n;i++)
	    {
	        for(j=0;j<m;j++)
	        cin>>ch[i][j];

	    }
	    for(i=0;i<n;i++)
	    {
	        for(j=1;j<m;j++)
	        {
	            if(ch[i][j]=='?'&&ch[i][j-1]!='?')
	            ch[i][j]=ch[i][j-1];
	        }

	    }
	    for(i=0;i<n;i++)
	    {
	        for(j=m-1;j>=1;j--)
	        {
	            if((ch[i][j]!='?')&&(ch[i][j-1]=='?'))
	            ch[i][j-1]=ch[i][j];
	        }

	    }


	    for(i=0;i<m;i++)
	    {
	        for(j=0;j<n;j++)
	        {
	            if(ch[j][i]=='?')
	                   {
	                       if(j==0)
	                       {
	                           k=j;
	                           while(ch[k][i]=='?')
	                           {
	                               k++;
	                               if(k>=n)
	                               break;
	                           }

    	                       for(l=k-1;l>=0;l--)
    	                       {
    	                           for(p=0;p<m;p++)
    	                                ch[l][p]=ch[l+1][p];
    	                       }
	                       }
	                       else
	                       {
	                           k=j;
	                           while(ch[k][i]=='?')
	                           {
	                               k++;
	                               if(k>=n)
	                               break;
	                           }

    	                       for(l=j;l<k;l++)
    	                       {
    	                           for(p=0;p<m;p++)
    	                                ch[l][p]=ch[l-1][p];
    	                       }
	                       }
	                   }
	        }
	    }
	    for(i=0;i<n;i++)
	    {
	        for(j=0;j<m;j++)
	        cout<<ch[i][j];
	        cout<<"\n";
	    }

	}
	return 0;
}
