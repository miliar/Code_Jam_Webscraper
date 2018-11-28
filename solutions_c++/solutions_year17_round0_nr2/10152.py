#include<bits/stdc++.h>
using namespace std;

int main()
    {
    
    int t;
    string a;
    
    cin>>t;
    while(t)
        {
        cin>>a;
       // cout<<n;
        //vector<char> vt;
       
        
        /*vector<int> :: iterator i;
        for (i = vt.begin(); i != vt.end(); ++i)
        cout << *i ;
        
         vector<int> :: reverse_iterator j;
        for (j = vt.rbegin(); j!= vt.rend(); ++j)
        cout << *j ;*/
        int i,j;
        int flag=0;
       for(i = 0;i<a.size()-1;i++)
           {
           
           if(a[i]=='1' && a[i+1]=='0')
               flag = 1;
           
           if(a[i]>a[i+1])
               {
               a[i]--;
               for(j=i+1;j<a.size();j++)
                   a[j]='9';
               i=-1;
           }
       }
       
        
        
        if(flag ==1)
           {
            int i=1;
            while(i<a.size())
            {cout<<a[i];
             i++;
            }
            cout<<"\n";
        }
       else 
        cout<<a<<"\n";
        
        
        t--;
    }
    
    return 0;
}