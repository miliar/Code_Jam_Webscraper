#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

long long int GetNumberOfDigits (long long int i)
{
    return i > 0 ? (int) log10 ((double) i) + 1 : 1;
}
int main()
{
   long long int t,n;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {   
        cin>>n;
        cout<<"Case #"<<tt<<": ";
        if(GetNumberOfDigits(n)==1){
            
            cout<<n<<"\n";
            continue;
        }
        
        int flag=1;
        while(flag)
        {
            vector<int> v,vr;
          long long int x=n;
            while(x!=0)
            {
               long long int r=x%10;
                v.push_back(r);
                x/=10;

            }
           reverse(v.begin(),v.end());
            vr=v;
            sort(v.begin(),v.end());
           int r=-1;
       if(vr==v)
         {    
           for(int i=0;i<vr.size();i++){
                    
             cout<<v[i];}
          cout<<"\n";
                break;
         }
            else
                {
                n--;
            }
        }}
    return 0;
}

