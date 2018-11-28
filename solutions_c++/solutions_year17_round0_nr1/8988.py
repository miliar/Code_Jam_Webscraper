#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("output.out");

    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        string s;
        int mf;

        cin>>s>>mf;

        int plus1=0;
        int minus1=0;
        int count=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='+')
                plus1++;
            else
                minus1++;
        }

        if(minus1==0)
        {
            cout<<"Case #"<<k<<": "<<0<<endl;
            continue;
        }
        bool answer = false;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                if(i+mf<=s.size())
                {
                    int temp=mf;
                    int j=i;
                    while(temp--)
                    {

                        if(s[j]=='-')
                        {
                            s[j]='+';
                            plus1++;
                            minus1--;
                        }
                        else
                        {
                            s[j]='-';
                            minus1++;
                            plus1--;
                        }

                        j++;

                    }

                    count++;

                    if(minus1==0)
                    {
                        cout<<"Case #"<<k<<": "<<count<<endl;
                        answer = true;
                        break;
                    }
                }

                else
                {
                    break;
                }
            }
        }

        if(!answer)
            cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<endl;
    }
}

