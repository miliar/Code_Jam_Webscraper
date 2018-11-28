#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, p, i, j, k, l, count, flag;
	cin>>t;
	for(p=1; p<=t; p++)
	{
	    count = 0;
	    flag = 1;
	    char s[10001];
	    cin>>s>>k;
	    l = strlen(s);
	    //cout<<"l= "<<l<<"   "<<s<<"\n";
	    for(i=0; i<=(l-k); i++)
	    {
	        if(s[i] == '-')
	        {
                count++;
                for(j=i; j<(i+k); j++)
                s[j] = (s[j]=='-') ? '+' : '-';
            }
        }
	        
        for(i=0; i<l; i++)
            if(s[i] == '-')
            {
                flag = 0;
                break;
            }
	       //cout<<"lol\n";     
	   if(flag==1) cout<<"Case #"<<p<<": "<<count<<"\n";
	   else cout<<"Case #"<<p<<": IMPOSSIBLE\n";
	}
	return 0;
}
