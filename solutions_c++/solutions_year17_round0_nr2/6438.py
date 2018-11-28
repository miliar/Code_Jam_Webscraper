#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;


void answ(string &n)
{
    for (int i = 1; i < n.length(); i++)
      if (n[i] < n [i-1])
      {
        int k = i-1;
        while(k > 0 && n[k] == n[k-1]) k--;
        n[k]--;
        for (int j = k+1; j < n.length(); j++)
          n[j] = '9';

        if (n[k] == '0' && n.length() > 1)
          n = n.substr(1);
      }
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("ou.txt", "w", stdout);

    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        string n;
        cin>>n;
        answ(n);
        cout<<"Case #"<< tt <<": "<<n<<endl;
    }
}

