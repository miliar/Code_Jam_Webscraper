#include <iostream>
#include <list>
#include <algorithm>
#include <map>

using namespace std;

void pr(list<long long int> l)
{
    for (auto x: l){cout << x << ' ';}
    cout << endl;
}

int main()
{
    freopen("a","r",stdin);
    freopen("b","w",stdout);
    int n;
    cin >> n;
    for (int izx=1;izx<=n;izx++)
    {
        cout << "Case #" << izx << ": ";
        long long int n,k;
        cin >> n >> k;
        map<long long int,long long int> kol;
        kol[n]=1;
        while(1)
        {
            auto it=kol.rbegin();
            long long int m=it->first;
            long long int x=it->second;
            long long int a1=(m-1)/2;
            long long int b1=m-a1-1;
            if (x<k)
            {
                k-=x;
                kol[a1]+=x;
                kol[b1]+=x;
                kol.erase(m);
            }
            else
            {
                cout << max(a1,b1) << ' ' << min(a1,b1) << endl;
                break;
            }
        }
    }
    return 0;
}
