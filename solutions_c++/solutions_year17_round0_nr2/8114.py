#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void calculate(string n)
{
    
    if(n[0]=='0'&&n.size()>1)
    {
     calculate(n.substr(1,n.size()-1));}
    else
    {
       int ff=1;
	string ans;
	for(int i =0;i<n.size()-1;i++)
		{
        char f_first=n[i]; 
		char f_next =n[i+1];
		if(f_first-f_next>0)
			{
            ff=0;
			ans=n.substr(0,i);
			ans+=f_first-1;
			
            while(i++<n.size()-1)
			ans+="9";
				
			}
		}

		if(ff)
		cout<<n<<endl;
		else
		calculate(ans);
    }
}

int main(){
    int t;
    cin>>t;
    
    for(int tt=1;tt<=t;tt++)
        {
		cout<<"Case #"<<tt<<" :";
    string n ;
	cin>>n;
        calculate(n);}
    return 0;
}