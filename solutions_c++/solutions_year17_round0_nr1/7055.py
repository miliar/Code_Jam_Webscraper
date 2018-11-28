#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    int a, b, c, d, k, e, f=1, t;
    string s;
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
 //   cin>>t;
    fin>>t;
    while(f<=t)
    {
//        cin>>s>>k;
        fin>>s>>k;
        cout<<s<<"  "<<k<<"\n";
        b=s.size();
        int ans=0;
        for(a=0; a<=b-k; a++)
        {
            if(s[a]=='-')
            {
                for(c=a; c<a+k; c++)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }
        for(a=b-1; a>=k-1; a--)
        {
            if(s[a]=='-')
            {
                for(c=a; c>a-k; c--)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }
        for(a=0; a<=b-k; a++)
        {
            if(s[a]=='-')
            {
                for(c=a; c<a+k; c++)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }
        for(a=b-1; a>=k-1; a--)
        {
            if(s[a]=='-')
            {
                for(c=a; c>a-k; c--)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }
        for(a=0; a<=b-k; a++)
        {
            if(s[a]=='-')
            {
                for(c=a; c<a+k; c++)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }
        for(a=b-1; a>=k-1; a--)
        {
            if(s[a]=='-')
            {
                for(c=a; c>a-k; c--)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }
        for(a=0; a<=b-k; a++)
        {
            if(s[a]=='-')
            {
                for(c=a; c<a+k; c++)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }
        for(a=b-1; a>=k-1; a--)
        {
            if(s[a]=='-')
            {
                for(c=a; c>a-k; c--)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }
        for(a=b-1; a>=k-1; a--)
        {
            if(s[a]=='-')
            {
                for(c=a; c>a-k; c--)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }for(a=b-1; a>=k-1; a--)
        {
            if(s[a]=='-')
            {
                for(c=a; c>a-k; c--)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }for(a=b-1; a>=k-1; a--)
        {
            if(s[a]=='-')
            {
                for(c=a; c>a-k; c--)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }for(a=b-1; a>=k-1; a--)
        {
            if(s[a]=='-')
            {
                for(c=a; c>a-k; c--)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }for(a=b-1; a>=k-1; a--)
        {
            if(s[a]=='-')
            {
                for(c=a; c>a-k; c--)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                ans++;
            }
        }
        bool yo=true;
        for(a=0; a<b; a++)
            if(s[a]=='-')
                yo=false;
//        cout<<"Case #"<<f<<": ";
        fout<<"Case #"<<f<<": ";
        if(yo==false)
//            cout<<"IMPOSSIBLE \n";
            fout<<"IMPOSSIBLE \n";
        else
//            cout<<ans<<"\n";
            fout<<ans<<"\n";
        f++;
    }
    return 0;
}
