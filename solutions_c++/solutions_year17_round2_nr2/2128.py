#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

int compare(const void *a,const void *b) {
    return ((const int *)a)[0] - ((const int *)b)[0];
}

int main() {
	std::ios::sync_with_stdio(false);
	long long int i, j, t, r, o, y, g, b, v, l, m, s, n;
	char ll, mm, ss;
	cin>>t;
	for(i=1; i<=t; i++)
	{
	    cin>>n>>r>>o>>y>>g>>b>>v;
	    if(r>y)
	    {
	        if(r>b)
	        {
	            l = r;
	            ll = 'R';
	            if(y>b)  
	            {
	                m = y; mm= 'Y';
	                s = b; ss='B';
	            }
	            else
	            {
	                m = b; mm = 'B';
	                s = y; ss= 'Y';
	            }
	        }
	        else
	        {
	            l = b;
	            ll = 'B';
	            m = r;
	            mm = 'R';
	            s = y;
	            ss = 'Y';
	        }
	    }
	    else
	    {
	        if(y>b)
	        {
	            l = y; ll = 'Y';
	            if(r>b)
	            {
	                m=r; mm= 'R';
	                s = b; ss = 'B';
	            }
	            else
	            {
	                m = b; mm = 'B';
	                s = r; ss='R';
	            }
	        }
	        else
	        {
	            l = b; ll = 'B';
	            m = y; mm = 'Y';
	            s= r; ss = 'R';
	        }
	    }
	    //cout<<"l="<<l<<" m="<<m<<" s="<<s<<" ll="<<ll<<" mm="<<mm<<" ss="<<ss<<"\n";
	    if(l>(m+s))
	        cout<<"Case #"<<i<<": IMPOSSIBLE\n";
	   else
	   {
	       int flag=0;
	       cout<<"Case #"<<i<<": ";
	       for(j=0; j<(m-s); j++)
	        cout<<ll<<mm;
	       l = l - m +s;
	       m = s;
	       flag = l;
	       while(l)
	       {
	           cout<<ll<<mm;
	           l--;
	           m--;
	           if(l)
	           {
	               cout<<ll<<ss;
	               l--;
	               s--;
	           }
	       }
	    while(m)
	    {
	        if(flag%2 == 0)
	            cout<<mm<<ss;
	       else cout<<ss<<mm;
	        s--;
	        m--;
	    }
	      if(s) cout<<ss;
	      cout<<"\n";
	   }
	}
	return 0;
}
