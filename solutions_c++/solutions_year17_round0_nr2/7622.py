// author - vanshaj2608 jaypee institute of information technology.
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    freopen("codejaminput2.txt" , "r" , stdin);
    freopen("codejamoutput2.txt" , "w" , stdout);
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        long long int n=0;
        string s1;
        int s[20];
        cin>>s1;
        int l = s1.size(),i,j;
        for(i=0;i<l;i++)
            s[i]=(int)s1[i]-48;

        for(i=l-2;i>=0;i--)
        {
            if(s[i]>s[i+1])
            {
                s[i]--;
                for(j=i+1;j<l;j++)
                    s[j]=9;
            }
        }
        for(i=0;i<l;i++)
        {
            n=n*10+s[i];
        }
        cout<<"Case #"<<test<<": "<<n<<endl;

    }

    return 0;
}
