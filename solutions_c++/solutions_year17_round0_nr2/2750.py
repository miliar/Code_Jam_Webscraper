#include <iostream>
#include <string.h>
#include<stdio.h>
using namespace std;
int main() {
  int t;
  freopen("a.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  char s[20];
  char ans[20];
  cin >> t;
  for (int i = 1; i <= t; ++i) {

    cin >> s ;
    int l =strlen(s);
    int ansl=0;
    for(int i=0;i<l;i++)
    {
        int eq_ok = true;
        for(int j=i+1;j<l;j++)
        {
            if(s[j]>s[i])break;
            if(s[j]<s[i])eq_ok =false;
        }
        if(eq_ok)
            ans[i]=s[i];
        else
        {
            ans[i]=s[i]-1 ;
            for(i=i+1;i<l;i++)
                ans[i]='9';
        }
    }
    ans[l]='\0';
    if(ans[0]=='0')
    {
        for(int i=0;i<l;i++)
            ans[i]=ans[i+1];
    }
    cout << "Case #" << i << ": " <<ans<< endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}
