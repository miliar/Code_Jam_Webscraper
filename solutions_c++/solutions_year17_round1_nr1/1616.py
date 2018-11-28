#include <bits/stdc++.h>


using namespace std;

int main()
{

freopen("A-large.in","r",stdin);
freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int r=0;
    while(t--)
    {
        r++;
        int n,m;
        cin>>n>>m;
        vector<string> s;
        for(int i=0;i<n;i++)
        {
            string g;
            cin>>g;
            s.push_back(g);

        }
       // cout<<"akhkgw"<<endl;

        for(int i=0;i<n;i++)
        {
            char x='?';
            for(int j=0;j<m;j++)
            {

                if(s[i][j]!=x&&s[i][j]!='?')
                    x=s[i][j];
                else if(s[i][j]=='?'&&x!='?')
                    s[i][j]=x;
//            cout<<s[i][j];

            }
  //          cout<<endl;
        }
        for(int i=0;i<n;i++)
        {
            char x='?';
            for(int j=m-1;j>=0;j--)
            {

                if(s[i][j]!=x&&s[i][j]!='?')
                    x=s[i][j];
                else if(s[i][j]=='?'&&x!='?')
                    s[i][j]=x;


            }
        }
        for(int i=0;i<m;i++)
        {
            char x='?';
            for(int j=0;j<n;j++)
            {

                if(s[j][i]!=x&&s[j][i]!='?')
                    x=s[j][i];
                else if(s[j][i]=='?'&&x!='?')
                    s[j][i]=x;


            }
        }

        for(int i=0;i<m;i++)
        {
            char x='?';
            for(int j=n-1;j>=0;j--)
            {

                if(s[j][i]!=x&&s[j][i]!='?')
                    x=s[j][i];
                else if(s[j][i]=='?'&&x!='?')
                    s[j][i]=x;


            }
        }



            cout<<"Case #"<<r<<": "<<endl;

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {

         cout<<s[i][j];

            }
            cout<<endl;
        }
        }

    }
