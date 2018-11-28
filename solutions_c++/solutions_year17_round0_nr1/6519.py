#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
	int T,i,j,k,l,m,count;
	string s;
	cin>>T;
	for(m=1;m<=T;m++)
	{
	    cin>>s;
	    l=s.size();
	    cin>>k;
	    count=0;
	    for(i=0;i+k<=l;i++)
	    {
	        if(s[i]=='-') 
	        {
	            count++;
	            for(j=0;j<k;j++)
	            {
	            if(s[i+j]=='-')  s[i+j]='+';
	            else s[i+j]='-';
	            }
	        }
	    }
	    cout<<"Case #"<<m<<": ";
	    int temp=1;
	    for(j=l-1;j>=i;j--)
	    if(s[j]=='-') {cout<<"IMPOSSIBLE\n"; temp=0; break;}
	    if(temp) cout<<count<<"\n";
	}
	return 0;
}

