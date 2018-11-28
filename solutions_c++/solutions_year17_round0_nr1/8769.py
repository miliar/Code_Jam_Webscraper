#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("input.in");
    ofstream cout("output.txt");
    int t;
    cin >>t;
    for (int iii=1; iii<=t; iii++)
    {
        string s;
        int k;
        cin >>s>>k;
        int d=s.size();
        int ans=0;
        for (int i=0; i<d-k+1; i++)
            if (s[i]=='-')
            {
                ans++;
                for (int j=i; (j-i+1)<=k; j++)
                    if (s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
            }
        bool ok=true;
        for (int i=0; i<d; i++)
            if (s[i]=='-')
            {
                ok=false;
                break;
            }
        if (ok)
            cout <<"Case #"<<iii<<": "<<ans<<"\n";
        else
            cout <<"Case #"<<iii<<": IMPOSSIBLE\n";
    }
    return 0;
}
