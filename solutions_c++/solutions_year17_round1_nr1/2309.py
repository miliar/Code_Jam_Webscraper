#include <bits/stdc++.h>
using namespace std;

int main() 
{
    std::ios::sync_with_stdio(false);
	
	int t, r, c, i, j, k, index;
	char ch;
	cin>>t;
	for(k=1; k<=t; k++)
	{
	    cin>>r>>c;
	    std::vector<string> a(r);
	    //char a[r][c];
	    for(i=0; i<r; i++)
	        cin>>a[i];
	        
	    /*for(i=0; i<r; i++)
	        cout<<a[i]<<" \n";
	        cout<<"\n";*/
	        
	    for(i=0; i<r; i++)
	    {
	        ch = '0';
	        for(j=0; j<c; j++)
	        {
	            if(a[i][j] != '?')
	            {
	                ch = a[i][j];
	            }
	            else
	            {
	                a[i][j] = ch;
	            } 
	        }
	        for(j=c-2; j>=0; j--)
	        {
	            if(a[i][j] == '0')
	                a[i][j] = a[i][j+1];
	        }
	    }
	    
	    for(i=0; i<r; i++)
	    {
	        for(j=0; a[i][j]=='0' && j<c; j++);
	        if(j!=c)
	        {
	            index = i;
	            break;
	        }
	    }
	    
	        if(a[0][0] == '0')
	        {
	            for(j=0; j<c; j++)
	             {
	                a[0][j] = a[index][j];
	             }
	        }
	    
	    
	    for(i=0; i<r; i++)
	    {
	        if(a[i][0] == '0')
	        {
	            //cout<<"lol\n";
	         for(j=0; j<c; j++)
	         {
	            a[i][j] = a[i-1][j];
	            //cout<<"mar ja a[i, j]="<<a[i][j]<<"   a[i-1,j]="<<a[i-1][j]<<"\n";
	         }
	        }
	    }
	    
	    cout<<"Case #"<<k<<":\n";
	    for(i=0; i<r; i++)
	    {
	        for(j=0; j<c; j++)
	            cout<<a[i][j];
	        cout<<"\n";
	    }
	}
	
	return 0;
}
