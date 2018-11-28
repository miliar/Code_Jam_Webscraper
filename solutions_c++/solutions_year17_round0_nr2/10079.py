#include<bits/stdc++.h>
using namespace std;


bool check(long long int n)
{
    int f = 0;
    ostringstream ss;
     ss << n;
     string s = ss.str();
   //  cout<<s<<endl;
  //  string s = to_string(n);
    for(int i=1;i<s.size();i++)
    {
        if(s[i-1]<=s[i])
        {
            continue;
        }
        else
        {
            return false;
        }
    }
    return true;
}

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int t,z=0;
    long long int x,i;

    cin>>t;

    while(t--)
    {
        z++;
         bool flag= false;
        cin>>x;
        if(x>=0 && x<=9)
        {
            cout<<"Case #"<<z<<": "<<x<<endl;
        //    cout<<x<<endl;
        }
        else if(x==10)
        {
            cout<<"Case #"<<z<<": "<<9<<endl;
        }
        else
        {
            for(i=x;i>=1;i--)
            {
               flag = check(i);
               if(flag== true)
               {
                   cout<<"Case #"<<z<<": "<<i<<endl;
                   break;
               }
            }


        }

    }
    return 0;
}
