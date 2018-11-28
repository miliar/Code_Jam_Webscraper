#include <bits/stdc++.h>
using namespace std;

int main() {
int t,T,k,counter,pcount,ncount;
cin>>T;
t=1;;
while(T--)
{
    counter=0;
    string S;
    cin>>S>>k;
   // cout<<S<<" ";
    //cout<<k<<" ";
    //cin>>k;
    int len=S.length();
   pcount=0;
   ncount=0;
    for(int i=0;i<len;i++)
    {
        if(S[i]=='+')
        pcount++;
        else if(S[i]=='-')
        ncount++;
        
    }
  //  cout<<len<<" "<<pcount<<" "<<ncount<<endl;
    if(pcount==len)
    cout<<"Case #"<<t<<": 0"<<endl;
    else if(ncount==len)
    {
        if(ncount%k)
        cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
        else
         cout<<"Case #"<<t<<": "<<ncount/k<<endl;
    }
    
    /*else if(ncount<k)
    cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;*/
    else
    {
        for(int i=0;i<=len-k;i++)
        {
            if(S[i]=='-')
            {
                for(int j=i;j<i+k;j++)
                {
                    if(S[j]=='+')
                    {S[j]='-';ncount++;pcount--;}
                    else
                    {S[j]='+';ncount--;pcount++;}
                }
                counter++;
            }
            
        }
        if(pcount!=len)
        cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
        else
        cout<<"Case #"<<t<<": "<<counter<<endl;
    }
    t++;
}
    return 0;
}
