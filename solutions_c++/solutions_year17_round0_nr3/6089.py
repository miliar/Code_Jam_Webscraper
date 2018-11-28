#include<bits/stdc++.h>
using namespace std;
int main()
{int z,t;
cin>>t;//input
for(z=0;z<t;z++)//testcases
{vector<int> a;
int b,c,d,e,i,f;
cin>>e;
a.push_back(e);
cin>>b;
for(i=0;i<b;i++)//loop
{reverse(a.begin(),a.end());
    c=a[0]/2;
d=(a[0]-1)/2;

   a.push_back(c);
   a.push_back(d);
   sort(a.begin(),a.end());
   a.pop_back();
}
 cout<<"Case #"<<z+1<<":"<<" "<<c<<" "<<d<<"\n";   

}
}

