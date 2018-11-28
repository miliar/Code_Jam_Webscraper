#include <iostream>
#include <string>
using namespace std;


int main() {
    freopen ("/Users/utkarsh/Desktop/TidyNum/TidyNum/inp.txt","r",stdin);
    freopen ("/Users/utkarsh/Desktop/TidyNum/TidyNum/O.txt","w",stdout);
    long long t;
    cin>>t;
    for(long long a=1;a<=t;a++)
    {
        long long n;
        cin>>n;
        bool flag1=false;
        if(n==1 || n==0)
            cout<<"Case #"<<a<<": "<<n<<endl;
        else{
        
        string s;
        for(long long i=n;i>0;i=i/10)
        {
            if(!((i%10)==1 || (i%10)==0))
                flag1=true;
            
            s.insert(s.begin(),(char)('0'+(i%10)));
        }
        
        
        if(!flag1)
        {
            cout<<"Case #"<<a<<": ";
            for(long long i=n;i>1;i=i/10)
            {
                cout<<9;
            }
            cout<<endl;
        }
        else
        {
            
                s.insert(s.end(),'9');
                bool flag=false;
                for(int i=0;i<s.length()-1;i++)
                {
                    if(flag)
                    {
                        s[i]='9';
                    }
                    if(s[i]>s[i+1] && !flag)
                    {
                        flag=true;
                        int j=i;
                        int curr=s[i];
                        while(s[j]>curr-1 && j>=0)
                        {
                            j--;
                        }
                        s[j+1]=curr-1;
                        i=j+1;
                     }
                }
            
            long long ans=0;
            for(int i=0;i<s.length()-1;i++)
            {
                ans=10*ans+(s[i]-'0');
            }
            cout<<"Case #"<<a<<": ";
            cout<<ans<<endl;
            
        }
    }
    }
    
    
    
    
}
