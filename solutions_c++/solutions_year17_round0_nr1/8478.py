#include<bits/stdc++.h>
using namespace std;

int main()
{
    int z;
    cin>>z;
    for(int t=1; t<=z; t++)
    {
        string ch;
        int k;
        cin>>ch>>k;
        int n=ch.length();
        int it=0;
        while(1)
        {
            int mi=0;
            for(int i=0; i<n; i++)
            {
                if(ch[i]=='-')
                    mi+=1;
            }
            if(mi==0)
                break;
            else if((mi==1&&k>1)||it>n)
            {
                it=-1;
                break;
            }
            int i;
            for(i=0; i<n; i++)
            {
                if(ch[i]=='-')
                    break;
            }
            if(n-i<k)i=n-k;
            for(int j=i; j<i+k; j++)
            {
                if(ch[j]=='-')ch[j]='+';
                else ch[j]='-';
            }
            it+=1;
        }
        if(it==-1)
        cout<<"Case #"<<t<<": IMPOSSIBLE\n";
        else
           cout<<"Case #"<<t<<": "<<it<<endl;
    }
}

