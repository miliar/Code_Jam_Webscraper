#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in", "r" , stdin);
    freopen("output.out", "w", stdout);
    int caseno=0,t;
    cin>>t;
    while(caseno++<t)
    {
        long long int n;
        string no;
        cin>>no;
        cout<<"Case #"<<caseno<<": ";
        int len=0,i,j;
        len=no.length();
        reverse(no.begin(),no.end());
        for(i=len-2;i>=0;i--)
        {
            if(no[i]<no[i+1])
                break;
        }
        if(i>=0)
        {
            no[i+1]--;
            for(j=i;j>=0;j--)
                no[j]='9';
            i++;
            for(;i<len-1;i++)
            {
                if(no[i]<no[i+1])
                {
                    no[i]='9';
                    no[i+1]--;
                }
                else
                    break;
            }
        }
        for(i=len-1;i>=0&&no[i]=='0';i--)
        {}
        for(;i>=0;i--)
        {
            if(no[i]<0)
                cout<<9;
            else
                cout<<no[i];
        }
        cout<<"\n";
    }
    return 0;
}
