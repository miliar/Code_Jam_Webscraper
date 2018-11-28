#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A.out");

    int t;
    fin>>t;
    for(int c=1;c<=t;c++)
    {
        string cake;
        int k;
        fin>>cake>>k;
        int n=cake.size();
        int ans=0;
        bool isPossible=true;
        for(int i=0;i<n;i++)
        {
            if(cake[i]=='-')
            {
                for(int j=i;j<i+k;j++)
                {
                    if(j>=n)
                    {
                        isPossible=false;
                        break;
                    }
                    cake[j]=cake[j]=='-' ? '+' : '-';
                    //cout<<cake[j];
                }
                //cout<<endl;
                ans++;
            }
            if(!isPossible)
                break;
        }
        if(isPossible)
        {
            fout<<"Case #"<<c<<": "<<ans<<endl;
        }
        else
        {
            fout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
        }

    }
    return 0;
}
