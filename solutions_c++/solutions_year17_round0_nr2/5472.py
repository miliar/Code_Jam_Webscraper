#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, l, i, j, k;
	char a[20];
	cin>>t;
	for(k=1; k<=t; k++)
	{
	    cin>>a;
	    l = strlen(a);
	    char b[l-1];
	    //cout<<"l= "<<l<<"\n";
	    while(1)
	    {
	        for(i=1; i<l; i++)
	        {
	            if(a[i] < a[i-1])
	            {
	                a[i-1]--;
	                for(j=i; j<l; j++)
	                    a[j] = '9';
	                break;
	            }
	        }
	        
	        if(i==l)
	            break;
	    }
	    if(a[0] == '0')
	    {
	        for(i=1; i<l; i++)
	            b[i-1] = a[i];
	       // b[l] = '\0';
	        cout<<"Case #"<<k<<": ";
	        for(i=0; i<l-1; i++)
	            cout<<b[i];
	        cout<<"\n";
	    }
	    else cout<<"Case #"<<k<<": "<<a<<"\n";
	}
	return 0;
}
