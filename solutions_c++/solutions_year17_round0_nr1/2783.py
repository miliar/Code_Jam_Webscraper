#include <iostream>
#include <string.h>
#include<stdio.h>
using namespace std;
int main() {
  int t,k;
  freopen("a.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  char s[1010];
  cin >> t;
  for (int i = 1; i <= t; ++i) {

    cin >> s >> k;  // read n and then m.
    int l = strlen(s);
    int tt=0;
    //cout<<s<<k<<endl;
    for(int z=0;z<l;z++)
    {
        if(s[z]=='-')
        {
            if(z+k>l)
            {
                tt=-1;
                break;
            }
            tt++;
            for(int x=z;x<=z+k-1;x++)
                if(s[x]=='+')
                    s[x]='-';
                else
                    s[x]='+';
        }
        //cout<<z<<" "<<s<<" "<<tt<<endl;
    }
    if(tt==-1)
        cout << "Case #" << i << ": IMPOSSIBLE"<< endl;
    else
        cout << "Case #" << i << ": " << tt<< endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}
