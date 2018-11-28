#include <iostream>
using namespace std;

void go(string n)
{//cout<<"entering "<<n<<endl;
    
    if(n[0]=='0'&&n.size()>1)
    {
     go(n.substr(1,n.size()-1));}
    else
    {int fl=1;
	string ans;
	for(int i =0;i<n.size()-1;i++)
		{char f=n[i]; //cout<<f<<" ";
		char l =n[i+1];//cout<<l<<" ";
		if(f-l>0)
			{//cout<<"f>l";
            fl=0;//cout<<f;
				ans=n.substr(0,i);
			ans+=f-1;
			while(i++<n.size()-1)
			ans+="9";
				
			}
		}
// cout<<ans;
		if(fl)
		cout<<n<<endl;
		else
		go(ans);
    }
}

int main() {
	int t;
    cin>>t;
    
    for(int i=1;i<=t;i++)
        {cout<<"Case #"<<i<<" :";
    string n ;
	cin>>n;
        go(n);}
	// your code goes here
	return 0;
}