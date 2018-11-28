#include <iostream>
#include<string>

using namespace std;

int main() {
    int t,k;
    string s;
    int success,count;
    cin>>t;
    while(t--)
    {
        success=count=0;
        cin>>s;
        cin>>k;
        int l=s.length();
        string idle(s);
        for(int i=0;i<l;i++)
           idle.at(i)='+';
            
        for(int i=0;i<l-k+1;i++) 
        {
            if(s==idle)
            {
                success=1;
                //cout<<count;
                break;
            }
            
            if(s.at(i)=='-')
            {
                s.at(i)='+';
                count++;
                for(int j=i+1;j<i+k;j++)
                {
                    char ch=s.at(j)=='+'?'-':'+';
                    s.at(j)=ch;
                }        
            }
        
           // cout<<s<<endl;
        }
        
        if(s==idle)
        {
        success=1;
        cout<<"Case #"<<t<<": "<<count<<endl;
        }
        if(success==0)
        cout<<"Case #"<<t<<": IMPOSSIBLE\n";
    }
    
	return 0;
}
