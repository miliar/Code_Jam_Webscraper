#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
typedef long long int ll;

#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
typedef long long int ll;

string s;

void dec(int a){
    if(a==0){
        if(s[0]=='1')
            s.erase(s.begin());
        else
            s[0]--;
    }else{
       if(s[a]=='0'){
           s[a] = '9';
           dec(a-1);
       }else{
           s[a]--;
       }
    }
    
}

int main(){
	int n;
    cin>>n;
    for(int i = 1;i<=n;i++){
        cin>>s;
        cout<<"Case #"<<i<<": ";
        if(s.size()==1){
            cout<<s<<endl;
            continue;
        }
        bool d = 0;
        for(int i = s.size()-1;i>1;i--){
            if(s[i]<s[i-1]){
                d = 1;
                s[i] = '9';
                dec(i-1);
                
            }
        }
        if(s[1]<s[0]){
            d = 1;
            s[1] = '9';
            if(s[0]=='0'||s[0]=='1')
                s.erase(s.begin());
            else
                s[0]--;
        }
        for(int i = 1;i<s.size();i++){
            if(s[i]<s[i-1])
                s[i] = '9';
        }
        cout<<s<<endl;
    }
    return 0;
}



