#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream cin("B-small-attempt0.in");
    ofstream cout("output.out");
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        string s,temp_s;
        cin>>s;
        temp_s=s;
        sort(temp_s.begin(),temp_s.end());
        if(s==temp_s)
        {
            cout<<"Case #"<<k<<": "<<s<<endl;
            continue;
        }

        for(int i=0;i<s.size()-1;i++)
        {
            if(s[i]>=s[i+1])
            {
                if(s[i]!='0')
                s[i]--;
                else
                s[i]='9';
                i++;
                while(i<s.size())
                {
                    s[i]='9';
                    i++;
                }

                break;
            }
        }

        int point=0;

        for(int i=0;i<s.size();i++)
        {
            if(s[i]!='0')
            {
                point=i;
                break;
            }
        }

        cout<<"Case #"<<k<<": ";
        for(int i=point;i<s.size();i++)
            cout<<s[i];

        cout<<endl;


    }
}
