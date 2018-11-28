/* 
 * Prob:  
 * Author: sameerpandit
 *
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>
#include <map>
#include <cmath>
#include <unistd.h>

using namespace std;
#define ull unsigned long long

vector<int> twoDigitTidyNums;
vector<int> ::iterator low;

string getLess(string num){
    string s="";
    int i=num.size()-1;
    while(num[i]=='0' && i>=0){
        s.push_back('9');
        i--;
    }
    s.push_back(num[i]-1);
    i--;
    while(i>=0){
        s.push_back(num[i]);
        i--;
    }
    string rev="";
    i=s.size()-1;
    while(s[i]=='0' && i>=0)
        i--;        
    for(;i>=0;i--){
        rev.push_back(s[i]);            
    }
    return rev;
}

string getTidy(string num){
    char prev=num[0];
    string ans="";
    ans.push_back(prev);
    int i;
//    cout<<"checking "<<num<<endl;
    for(i=1;i<num.size();i++){
        if(prev>num[i]){
            if(ans=="1"){
                ans="";
                break;
            }
            ans = getTidy(getLess(ans));
            break;
        }else{    
            ans.push_back(num[i]);
        }
//        cout<<tidyNum<<endl;
        prev=num[i];            
    }
//    cout<<i<<endl;
    for(;i<num.size();i++){
        ans+='9';
    }
//    cout<<num<<":ans="<<ans<<endl;
    return ans;
}

bool isTidy(ull num){
//    cout<<"checking "<<num<<endl;
    int prev=10;
    int d;
    bool tidy=true;
    while(num){
        d=num%10;
        if(d>prev){
            tidy=false;
            break;
        }
        num/=10;
        prev=d;
    }
    return tidy;
}

/*int main() {
    int T;
    cin>>T;
    int t = T;
    vector<ull> sequence;
    for(int i=1;i<1001;i++)
        if(isTidy(i))
            sequence.push_back(i);
    while (T--) {
        ull n;
        cin>>n;
        cout << "Case #" << t - T << ": ";
        vector<ull>::iterator low;        
        low=lower_bound(sequence.begin(),sequence.end(),n);
        if(*low!=n)
            --low;
        cout<<*(low);
        cout << endl;
    }
    return 0;
}*/

int main() {
    int T;
    cin>>T;
    int t = T;
    while (T--) {
        string n;
        cin>>n;
        cout << "Case #" << t - T << ": ";
        cout<<getTidy(n);
        cout << endl;
    }
    return 0;
}
