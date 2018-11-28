#include <bits/stdc++.h>
using namespace std;
int main() {
  int t,k,z;
  cin >> t;
  char s[2000];


  for(int j=1;j<=t;j++) {
    cin>>s;
    cin>>k;
      z=strlen(s);
      int ctr=0,c=0;
    for(int i=0;i<=z-k;i++)
    {
        if(s[i]=='-')
        {
            c++;
            s[i]='+';
            for(int m=i+1;m<i+k;m++)
            {
                if(s[m]=='-')
                s[m]='+';
            else
                s[m]='-';
            }
        }

    }
    for(int i=z-k+1;i<z;i++)
    {
        if(s[i]=='-')
        {
            ctr++;
            break;
        }
    }
    if(ctr==0)
    cout << "Case #" << j << ": " << c<< endl;
    else
        cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
  }
return 0;
}
