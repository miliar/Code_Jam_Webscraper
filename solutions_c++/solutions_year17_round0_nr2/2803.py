#include <bits/stdc++.h>
#define ll long long
using namespace std;
void go(int cnum)
{
    string n;
    cin >> n;
    cout << "Case #" << cnum << ": ";
    for(int i=n.size()-2; i>=0; i--)
    {
        if(n[i] > n[i+1])
        {
            n[i]--; //guaranteed to not be 0, so don't need to do carrying
            for(int j=i+1; j<n.size(); j++)
                n[j] = '9';
        }
    }
    while(n[0] == '0')
        n.erase(n.begin());
    cout << n << "\n";
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i=1; i<=t; i++)
        go(i);
    return 0;
}
