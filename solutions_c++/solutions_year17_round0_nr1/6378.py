#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        string a;
        int k;
        int w=0;
        cin>>a>>k;
        int n=a.size();
        for(int j=0;j<n-k+1;j++)
        {
            if(a[j]=='-')
            {
                for(int l=0;l<k;l++)
                {
                    if(a[j+l]=='+')
                        a[j+l]='-';
                    else
                        a[j+l]='+';
                }
                w++;
            }
        }
        bool czy=true;
        for(int z=0;z<k;z++)
            if(a[n-z-1]=='-')
                czy=false;
        if(czy)
            cout<<"Case #"<<i+1<<": "<<w<<endl;
        else
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
