#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
    for(int i=1;i<=t;i++)
    {
        //char  n[20],ans[19];
        string n;
        cin>>n;
       // int l=strlen(n);
        int l=n.size();
        {
          //  ans[0]=n[0];
            //ans[1]='\0';
        }
       if(l!=1)
        {
            for(int k=1;k<l;k++)
            {
                int f1=0;
                for(int j=k;j<l;j++)
                {
                    if(n[j]>n[k-1])
                    {
                        break;
                    }
                    if(n[j]<n[k-1])
                    {
                        f1=1;
                        break;
                    }
                }
                if(f1==1)
                {
                  n[k-1]--; 
                  while(k<l)
                  {
                     
                      n[k]='9';
                       k++;
                  }
                  break;
                   
                }
            }
        }
        cout<<"Case #"<<i<<": ";
        int p=-1;
        while(p++<l)
        {
            if(n[p]=='0')
            continue;
            cout<<n[p];
            //p++;
        }
        cout<<"\n";
    }
	return 0;
}
