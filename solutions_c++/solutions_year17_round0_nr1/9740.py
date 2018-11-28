#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t,x=0;
    cin>>t;

    while(t--)
    {
        x++;
        string s;
        int k,len,len2,c=0;

        int flag =0;

        cin>>s>>k;
        int l = s.size();

        for(int i=0;i<l;i++)
        {
            if(s[i]=='+')
            {
                if(i==l-1)
                {
                    flag=1;
                }
                continue;
            }
            else
            {
                len = i;
                break;
            }
        }
        if(flag == 1)
        {
            cout<<"Case "<<"#"<<x<<": 0"<<endl;
        }
        else
        {
            for(int i = len;i<(l-k+1);i++)
            {
                if(s[i]=='-')
                {
                    for(int j=i;j<(i+k);j++)
                    {
                        if(s[j]=='+')
                        {
                            s[j]='-';
                        }
                        else
                        {
                            s[j]='+';
                        }
                    }
                    c++;
                }
        //        cout<<s<<endl;
            }
            for(int i = 0; i<l;i++)
            {
             //   cout<<s[i];

                if(s[i]=='-')
                {
                    flag =2;
                    break;
                }


            }
            //cout<<endl;

            if(flag ==2)
            {
                cout<<"Case "<<"#"<<x<<": IMPOSSIBLE"<<endl;
            }
            else
            {
               cout<<"Case "<<"#"<<x<<": "<<c<<endl;
            }

        }


    }

    return 0;
}
