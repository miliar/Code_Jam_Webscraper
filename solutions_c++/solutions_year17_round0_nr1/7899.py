#include <bits/stdc++.h>

using namespace std;

int main()
{

   freopen("A-large.in","r",stdin);
     freopen("output.txt", "wt", stdout);
//ofstream outp("Asmallattempt.in");
    int t,n,k=1;
    string s;
    cin>>t;
    while(t--)
    {
        int nb=0;
        cin>>s>>n;
        if ((n==s.length())&&(s.find('-')<=s.length())&&(s.find('+')<=s.length()))
        {
            cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
            k++;
        }
        else
        {
            while(s.find('-')<=s.length()-n)
            {
            int pos=s.find('-');
                s[pos]='+';
                //outp<<s.find('-')<<endl;
                for(int i=1; i<n; i++)
                {
                    if(s[pos+i]=='-')
                    {
                        s[pos+i]='+';
                    }
                    else
                    {
                        s[pos+i]='-';
                    }
                                                 //   outp<<s<<endl;

                }
                nb++;

            }
            if(s.find('-')<=s.length())
            {
                cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
                k++;
            }
            else
            {
                cout<<"Case #"<<k<<": "<<nb<<endl;
                k++;
            }

        }

    }
    return 0;
}
