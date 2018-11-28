#include <bits/stdc++.h>
using namespace std;
int test;
int R, C;
string s[31];
int main()
{
    cin>>test;
    for(int tt=1; tt<=test; tt++)
    {
        cin>>R>>C;
        for(int i=0; i<R; i++)
        {
            cin>>s[i];
        }
        while(1)
        {
            bool jo=false;
            for(int i=0; i<R; i++)
            {
                for(int j=0; j<C; j++)
                {
                    if(i+1<R && s[i][j]=='?' && s[i+1][j]!='?')
                    {
                        s[i][j]=s[i+1][j];
                        jo=true;
                        break;
                    }
                }
                if(jo) break;
            }
            if(!jo) break;
        }
        while(1)
        {
            bool jo=false;
            for(int i=0; i<R; i++)
            {
                for(int j=0; j<C; j++)
                {
                    if(i-1>=0 && s[i][j]=='?' && s[i-1][j]!='?')
                    {
                        s[i][j]=s[i-1][j];
                        jo=true;
                        break;
                    }
                }
                if(jo) break;
            }
            if(!jo) break;
        }
        while(1)
        {
            bool jo=false;
            for(int i=0; i<R; i++)
            {
                for(int j=0; j<C; j++)
                {
                    if(j+1<C && s[i][j]=='?' && s[i][j+1]!='?')
                    {
                        s[i][j]=s[i][j+1];
                        jo=true;
                        break;
                    }
                }
                if(jo) break;
            }
            if(!jo) break;
        }
        while(1)
        {
            bool jo=false;
            for(int i=0; i<R; i++)
            {
                for(int j=0; j<C; j++)
                {
                    if(j-1>=0 && s[i][j]=='?' && s[i][j-1]!='?')
                    {
                        s[i][j]=s[i][j-1];
                        jo=true;
                        break;
                    }
                }
                if(jo) break;
            }
            if(!jo) break;
        }
        cout<<"Case #"<<tt<<":"<<endl;
        for(int i=0; i<R; i++)
        {
            for(int j=0; j<C; j++)
            {
                cout<<s[i][j];
            }
            cout<<endl;
        }
    }

    return 0;
}
