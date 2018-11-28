#include <bits/stdc++.h>

using namespace std;

int main(){
     int t;
    cin>>t;
    long long int n;
    int q=1;
    while(q<=t)
    {
    cin>>n;
    string s=to_string(n);
   while(!is_sorted(s.begin(),s.end()))
   { n=stoll(s);
    n--;
       s=to_string(n);
      }
    cout<<"Case #"<<q<<": "<<s<<endl;
        q++;
    }
    // Write Your Code Here
    return 0;
}
