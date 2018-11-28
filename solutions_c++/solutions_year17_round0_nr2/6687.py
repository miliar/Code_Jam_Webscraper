#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main() {
    int t,z;
    cin>>t;
    for(z=0;z<t;z++)
    {long long int n,temp,num=0,a,b,flag=0,i,j,temp1;
    cin>>n;
    temp=n;
    do {
     ++num; 
     n /= 10;
} while (n);
   n=temp; 
    for(i=n;i>0;i--)
    {
   std::string s = std::to_string(i);
   std::string st = std::to_string(i);
    std::sort(st.begin(), st.end());
    if(s==st)
    {
        cout<<"Case #"<<z+1<<":"<<" "<<i<<"\n";
        break;
    }
        
    }
   
    }
	// your code goes here
	return 0;
}
