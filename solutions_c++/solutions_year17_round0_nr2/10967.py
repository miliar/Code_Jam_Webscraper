#include<bits/stdc++.h>
#include<string>
#include<algorithm>
using namespace std;


int main()
{

int t;
cin>>t;
int cnt=1;
while(t--)
{
    long long n;
    cin>>n;
    string s;
   for(int i=n;i>=0;i--)
   {
       s=to_string(i);

        if(is_sorted(s.begin(),s.end()))
            break;


   }

   cout<<"Case #"<<cnt<<": "<<s<<endl;
    cnt++;



}




return 0;
}

