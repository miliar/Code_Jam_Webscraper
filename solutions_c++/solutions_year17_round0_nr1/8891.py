#include<iostream>
#include<algorithm>
#include<bits/stdc++.h>
using namespace std;
string s;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("j.txt","w",stdout);
    int t,k,i,n,c,l,j,jam,y=1;
//freopen("A-small-attempt0.in","r",stdin);
  //  freopen("jay.txt","w",stdout);
    cin>>t;
    while(t--)
    {
         jam=0;
        cin>>s;
        cin>>k;
        n=s.length();
        for(j=0;j<n;j++)
        {
            if(s[j]=='-' && j+k<=n)
            {
             for(int o=j;o<j+k;o++)
             {
                 if(s[o]=='-'){s[o]='+';}
                 else{s[o]='-';}
             }
          //   cout<<s<<endl;
             ++jam;
            }
        }
       /* for(j=0;j<n;j++)
{
              string m=s.substr(j,k);
            int v=count(m.begin(),m.end(),'-');
             int ka=count(m.begin(),m.end(),'+');
            // cout<<m<<"\t"<<v<<endl;
            if(v==0){
                    j=j+k;


                    }
           else if(v==k-1 || ka==k-1)
            {
                if(s[j]==s[j+1])
                {
                    ++jam;
                     for(int o=j;o<j+k;o++)
                    {if(s[o]=='-'){
                            s[o]='+';}
                            else{s[o]='-';}


                     }

                }
                else if(s[j+k-1]==s[j+k-2])
                {
                    ++jam;
                    for(int o=j;o<j+k;o++)
                    {if(s[o]=='-'){
                            s[o]='+';}
                            else{s[o]='-';}


                     }
                }
            }


           else if(v==k)
            {
                for(int o=j;o<j+k;o++){s[o]='+';}
               // cout<<s<<endl;
            j=j+k;
            ++jam;
            }


}*/
//cout<<s<<endl;
  if(s.find('-')==string::npos){cout<<"case #"<<y<<": "<<jam<<endl;}
        else{cout<<"case #"<<y<<": "<<"IMPOSSIBLE"<<endl;}
        ++y;
    }

}
