#include <iostream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

int main()
{
    int N;
    string s;
    cin>>N;
    
    for(int i=0; i<N; ++i){
            cin>>s;
            for(int j=s.length()-1; j; --j){
                        if(s[j]>=s[j-1])
                                continue;
                        if(s[j-1]!='0'){
                             s[j-1] = char(s[j-1]-1);   
                             for(int t=j; t<s.length(); ++t)
                                     s[t] = '9';
                        } else {
                             for(int t=j-1; t>=0; --t){
                                     if(s[t]!='0'){
                                        s[t] = char(s[t]-1);   
                                        for(int k=t+1; k<s.length(); ++k)
                                             s[k] = '9';
                                        j = t;
                                        break;
                                     }
                             }
                        }
            }
            while(s.length() && s[0]=='0'){
                s=s.substr(1, s.length()-1);
            }
            cout<<"Case #"<<i+1<<": "<<s<<"\n";
    }
return 0;
}
 
