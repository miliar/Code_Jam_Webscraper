#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main() {
    long long int t;
    cin>>t;
	for (long long int j=0;j<t;j++)
    {
    double ss,kk,hh,pp,max=0,pp1;
    long long int na,da,ia;
    cin>>da>>na;
 
    for(ia=0;ia<na;ia++)
    {cin>>kk>>ss;
    pp=da-kk;
    hh=(da-kk)/ss;
    if(hh>max)
    max=hh;
 
    }
     pp1=da/max;
   cout<<std::fixed;
    cout<<std::setprecision(6);
cout<<"Case #"<<j+1<<": "<<pp1<<std::endl;
cout.flush();
    }
	// your code goes here
	return 0;
}