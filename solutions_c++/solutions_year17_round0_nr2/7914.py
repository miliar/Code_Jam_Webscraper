#include <bits/stdc++.h>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
bool isnot9 (char x) { return (x!='9'); }
int main()
{

   freopen("B-large.in","r",stdin);
    freopen("output.txt", "wt", stdout);
    int t,k=1;
    string n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        for(int i=n.length()-1; i>0; i--)
        {
         int a,b;
         a=n[i]-'0';
         b=n[i-1]-'0';
         if(a<b)
         {
         n[i-1]=(b-1)+'0';
         std::replace_if(n.begin()+i, n.end(), isnot9, '9');

         }
        }
        while(n[0]=='0'){n.erase(0,1);}
                    cout<<"Case #"<<k<<": "<<n<<endl;k++;

    }

//    std::replace_if(str.begin(), str.end(), [](char ch){ return ch != ' '; }, '_');
    return 0;
}
