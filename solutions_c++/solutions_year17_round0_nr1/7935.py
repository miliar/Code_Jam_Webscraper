#include <bits/stdc++.h>
using namespace std;

int main() {
    long long int T,k,length,i,j,c,f,y;string s;
    y=1;
	cin >> T;
	while(T--)
	{
	    cin >> s >> k;c=0;f=1;
	    length=s.length();
	    for(i=0;i<length;i++)
	    {
	    
	       if(s[i]=='-'&& i>length-k){f=0;break;}
	        if(s[i]=='-')
	        {c++;
	          for(j=0;j<k;j++)
	          {
	              if(s[i+j]=='-') s[i+j]='+';
	              else            s[i+j]='-';
	          }
	        }
	        
	    }
	 
	    if(f==0) cout << "Case #"<< y << ": " << "IMPOSSIBLE" << endl;
	    else cout << "Case #"<< y << ": " << c << endl;
	    y++;
	    
	    
	}
	
	
	
	
	
	
		return 0;
}
