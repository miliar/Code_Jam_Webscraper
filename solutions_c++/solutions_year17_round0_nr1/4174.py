#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;

    for(int i=0;i<t;i++)
    {
        string s;
        int k;

        cin>>s>>k;
        int flag=0;
        int cnt=0;

        for(int j=0;j<s.size();j++)
        {
            if(s[j]=='-')
            {
                cnt++;
                if(j+k>s.size())
                {
                    flag=1;
                    break;
                }



                else
                {
                    for(int y=j;y<j+k;y++)
                    {
                        if(s[y]=='-')
                        {
                            s[y]='+';
                        }

                        else
                        {
                            s[y]='-';
                        }
                    }
                }
            }
        }

        for(int j=0;j<s.size();j++)
        {
            if(s[j]=='-')
            {
                flag=1;
                break;
            }
        }

        if(flag==1)
            cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<cnt<<endl;


    }
    return 0;
}
