#include<iostream>
#include<string>
using namespace std;
bool isTidy(string n)
{
    if(n.length()==1)return true;
    char counter=n[0];
     for(int x=1;x<n.length();x++)
    {
        if(counter>n[x])
            return false;
        counter = n[x];
    }
    return true;
}

int main()
{
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        string n;
        cin>>n;
        int len = n.length();
        while(!isTidy(n))
        {
            for(int i=len-1;i>0;i--)
            {
                if(n[i]<n[i-1])
                {
                    if(n[i-1]!='0')
                        n[i-1]--;
                    else
                    {
                        int index = i;
                        while(n[--index]=='0')
                        {
                            n[index]='9';
                        }
                        n[index]--;
                    }
                    for(int h=i;h<len;h++)
                        n[h]='9';      
                }
            }
        }
        if(n[0]=='0')
            n=n.substr(1);
        cout<<"Case #"<<tc<<": "<<n<<endl;
    }
    
    return 0;
}
