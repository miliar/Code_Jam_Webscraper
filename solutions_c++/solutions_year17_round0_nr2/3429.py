#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
vector<int>v;

void numToArray(ull N)
{
    int c;
    while(N)
    {
        c = N%10;
        v.insert(v.begin(),c);
        N = N/10;
    }
}


void solve(int t)
{
    int n = v.size();
    for(int i=n-1;i>0;i--)
    {
        if(v[i-1] > v[i])
        {
            v[i] = 9;
            v[i-1]--;
        }
    }

    for(int i=0;i<n-1;i++)
    {
        if(v[i] > v[i+1])
            v[i+1] = v[i];
    }

    cout <<"Case #" << t << ": ";
    bool leading = true;
    for(int i=0;i<v.size();i++){
        if(v[i] == 0 && leading)
            continue;
        cout << v[i];
        leading = false;
    }
    cout <<"\n";
}



int main(void)
{
    int T;
    ull N;

    cin >> T;

    for(int t=1; t<=T;t++)
    {
        cin >> N;
        v.clear();
        numToArray(N);
        solve(t);
    }
    return 0;
}
