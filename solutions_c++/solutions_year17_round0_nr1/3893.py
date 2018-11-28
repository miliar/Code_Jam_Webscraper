#include <iostream>
#include<string>
using namespace std;

int main()
{
   int t;
   cin >>t;
   for(int e=1;e<=t;e++)
   {
        string S;
        int k;
        cin >> S>>k;
        int count =0;
        for(int x=0;x<S.length()-k+1;x++)
        {
            if(S[x]=='-')
            {
                count++;
                for(int i =0;i<k;i++)
                    if(S[x+i]=='-')
                        S[x+i]='+';
                    else 
                        S[x+i]='-';
            }
        }
        bool isSolvable=true;
        for(int x=0;x<S.length();x++)
            if(S[x]=='-')isSolvable = false;
        if(isSolvable)
            cout<<"Case #"<<e<<": "<<count<<endl;
        else
            cout<<"Case #"<<e<<": IMPOSSIBLE"<<endl;
        
   }
   
   return 0;
}

