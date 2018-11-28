#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int t,l=1;
    cin>>t;
    while(l<=t)
    {
        string s;
        cin>>s;
        char d;
        int i,j,k,p,w;
        k=s.size();
        for(i=0;i<k-1;i++)
        {
            j = s[i]-48;
            p = s[i+1]-48;
            if(j>p)
            {
                for(w=i+1;w<s.size();w++)
                {
                    s[w] = '9';
                }
                d = j+47;
                s[i] = d;
                for(w=i;w>0;w--)
                {
                    j = s[w];
                    p = s[w-1];
                    if(p>j)
                    {
                        s[w] = '9';
                        d = p-1;
                        s[w-1] = d;
                    }
                }
            }
        }
            cout<<"Case #"<<l<<": ";
            for(i=0;i<s.size();i++)
            {
                if(s[i]=='0')
                    continue;
                else
                    cout<<s[i];
            }
            cout<<endl;
                l++;
    }
}
