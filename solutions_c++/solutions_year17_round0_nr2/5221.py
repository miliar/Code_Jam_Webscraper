    #include <bits/stdc++.h>
    using namespace std;

    int main()
    {
        ios::sync_with_stdio(false);
        int t;
        cin>>t;

        for(int i=0; i<t; i++)
        {
            string s,ats;
            cin>>s;
            ats=s;

            for(int j=s.size()-1;j>0;j--)
                if(s[j] < s[j-1])
            {
                for(int k=j;k<s.size();k++)
                s[k]='9';
                s[j-1]--;
            }

            while(s[0]=='0')
                s.erase(s.begin());

            cout<<"Case #"<<i+1<<": ";
                cout<<s<<"\n";
        }

    }

