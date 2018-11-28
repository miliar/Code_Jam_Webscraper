#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large output.in","w",stdout);
    int t,j,i,r;
    cin>>t;
    string a;

    for(int c=1;c<=t;c++)
    {
        cin>>a;
        i=a.length();
        reverse(a.begin(),a.end());
        for(j=i-1;j>0;j--)
        {
            if(a[j]>a[j-1])
            {
                while(j<(i-1) && a[j]==a[j+1])
                {
                    j++;
                }
                a[j]--;
                j--;
                while(j!=-1)
                {
                    a[j]='9';
                    j--;
                }
                break;
            }
        }
        cout<<"Case #"<<c<<": ";
        if(a[i-1]!='0')
        {
            cout<<a[i-1];
        }
        for(j=i-2;j>=0;j--)
        {
            cout<<a[j];
        }
        cout<<endl;
    }
    return 0;
}
