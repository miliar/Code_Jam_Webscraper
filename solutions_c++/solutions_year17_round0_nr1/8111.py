#include<iostream>
using namespace std;

bool forwrd(string &s,int &k,int &c1)
{
     for(int j=0;j<s.size();j++)
        {
            int t=j;
            if(s[j]=='+')
                continue;
            if(s[j]=='-')
            {
                if(j+k-1>=s.size()){
                    //cout<<j+k-1<<endl;
                    break;
                }
                c1++;
                s[j]='+';


                for(int h=1;h<=k-1;h++)
                {
                    j++;
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                j=t;
                //cout<<j<<endl;
            }
        }
        //cout<<c1<<" "<<s<<endl;
        for(int h=s.size();h>=0;h--)
        {
            if(s[h]=='-'){
                return false;
            }
        }
        return true;
}

int main()
{
    int t;
    cin>>t;
    int c1,c2;
    for(int i=1;i<=t;i++)
    {
        c1=0;
        c2=0;
        bool f1,f2;
        string s;
        string temp;
        cin>>s;
        temp=s;
        int k;
        cin>>k;
        f1=forwrd(s,k,c1);

        cout<<"Case #"<<i<<": ";
        if(f1==0)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<c1<<endl;
    }
    return 0;
}
