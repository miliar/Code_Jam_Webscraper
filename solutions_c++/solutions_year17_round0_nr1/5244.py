    #include <bits/stdc++.h>
    using namespace std;

    int main()
    {
        ios::sync_with_stdio(false);
        int t;
        cin>>t;

        for(int i=0; i<t; i++)
        {
            string s,goal;
            cin>>s;
            goal = string(s.size(),'+');
            int k;
            cin>>k;
            int flips = 0;

            for(int j=0; j+k<=s.size();j++)
            {
                if(s[j]=='-')
                {
                    for(int x=j;x<j+k;x++)
                    s[x]= (s[x]=='-' ? '+' : '-');
                    flips++;
                }
            }

            cout<<"Case #"<<i+1<<": ";
            if(goal==s)
                cout<<flips<<"\n";
            else
                cout<<"IMPOSSIBLE\n";
        }

    }

