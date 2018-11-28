// Recursive approach to determine whether an array can be separated into two sets having equal sum


#include<bits/stdc++.h>
using  namespace std;


int main()
{

    int t;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        string s;
        cin>>s;
        bool sorted = false;
        while(!sorted)
        {
            sorted = true;
            for(int i=0;i<s.size()-1;i++)
            {
                if(s[i] > s[i+1])
                {
                    s[i]-=1;
                    for(int j=i+1;j<s.size();j++)
                        s[j]='9';
                    sorted = false;
                    break;
                }

            }

        }
        if(s[0]!='0')
            cout<<s;
        else
            for(int i=1;i<s.size();i++)
            cout<<s[i];
        cout<<endl;

    }

    return 0;


}
