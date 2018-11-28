#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    int l[20];
    string s;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        for (int j=0;j<20;j++)
            l[j]=0;
        int x=19;
        cin >> s;
        for (int j=s.length()-1;j>=0;j--)
        {
            l[x]=int(s[j])-48;
            x--;
        }
        /*for (int j=0;j<=19;j++)
            cerr << l[j];
        cerr << "\n";*/
        int it=19;
        while (it>0)
        {
            if(l[it-1]<=l[it])
                it--;
            else if(l[it-1]>l[it])
            {
                l[it-1]--;
                for (int j=it;j<=19;j++)
                    l[j]=9;
            }
        }
        cout << "Case #" << i+1 << ": ";
        bool wyp=false;
        for (int j=0;j<20;j++)
        {
            if(wyp||l[j]>0)
            {
                wyp=true;
                cout << l[j];
            }
        }
        cout << "\n";
        /*for (int j=0;j<20;j++)
            cerr << l[j];
        cerr << "\n";*/
    }
    return 0;
}
