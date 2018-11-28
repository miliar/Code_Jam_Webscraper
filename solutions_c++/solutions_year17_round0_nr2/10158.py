#include<bits/stdc++.h>
using namespace std;
template <class T>
inline std::string to_string (const T& t)
{
    std::stringstream ss;
    ss << t;
    return ss.str();
}
main()
{
freopen("B-small-attempt0.in","r",stdin);
freopen("outputtidy.txt","w",stdout);
    int t;
    cin>>t;
    int j =1;
    while(t--)
    {

        long long n,temp;
        cin>>n;
        temp=n;
        //cout<<temp;
        bool ans = true;
        while(ans)
        {   string x;
            x=to_string(temp);
            //cout<<x;
            int i;
            for(i = 0;i < x.length()-1;i++)
            {
                if(x[i] <= x[i+1])
                    continue;
                else
                {
                    temp--;
                    break;
                }
            }
            if(i == x.length()-1)
                ans=false;
        }
        cout<<"Case #"<<j<<": "<<temp<<endl;
        j++;
    }
}


