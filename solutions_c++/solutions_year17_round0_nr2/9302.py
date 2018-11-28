#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output-B.txt","w",stdout);
   int tt,j=1;
   cin>>tt;
   while(tt--)
   {
       int l=0;
       string s;
       cin>>s;
       cout<<"Case #"<<j++<<": ";
       string rv=s;
       sort(rv.begin(),rv.end());
       if(rv==s)
       {
           cout<<rv<<endl;
           continue;
       }
       for(int i=0; i<s.size(); i++)
       {
           if((s[i]-'0')<(s[i+1]-'0'))
           {
            cout<<s[i];
            l++;
           }
           else
           {
               int nn=s[i]-'0';
               if((nn-1!=0))
               cout<<nn-1;
               int len=s.size()-l;
               l+=len;
               len--;
               for(int j=0; j<len; j++)
                cout<<"9";

                break;
           }
       }
       cout<<endl;
   }
}
