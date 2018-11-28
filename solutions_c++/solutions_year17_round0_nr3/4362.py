#include <bits/stdc++.h>
#define ll long long
using namespace std;
map<ll int,ll int>m;
int main()
{
    ll int n,a,b,t,i,j,k,l,u,y,z,o=0,ls,rs,min,max;
	ofstream myfile;
	    myfile.open ("ans3.txt");
    cin>>n;
    b=1;
    while(b<=n)
    {  o=0;
        u=0;
        min=0;
        max=9999999999;
      //  cout<<"*";
        cin>>i>>j;
      //  cout<<"*";
        m[i]=1;
        l=1;
        map<ll int,ll int>::iterator it;
        map<ll int,ll int>::iterator pt;
        while(l<=j)
        {   ls=0;
            u=0;
            rs=0;
            o=0;
            pt = m.end();
            pt--;
            z=pt->first;
            y=pt->second;
              a = z-1;
              if(a%2==0)
                  ls=a/2;
              else
                  ls = a/2+1;
              rs=a/2;
                 // cout<<a<<endl;
               //   cout<<"#"<<y<<" "<<a<<z<<endl;
               
               // cout<<ls<<" "<<rs<<endl;
                m[pt->first]--;
                if(m[pt->first]==0)
                   m.erase(pt,m.end()); 
                if(ls!=0)
                {
                    m[ls]++;
                }
                if(rs!=0)
                {
                    m[rs]++;
                }
                l++;
            //    cout<<l<<endl; 
        }
    //    cout<<"*";
        if(ls>rs)
        {
            max=ls;
            min=rs;
        }
        else
        {
            max=rs;
            min=ls;
        }
      //  cout<<"*";
	        myfile<<"Case #"<<b<<": "<<max<<" "<<min<<endl;
        m.clear();
        b++;
    }
	 myfile.close();
    return 0;
}   
