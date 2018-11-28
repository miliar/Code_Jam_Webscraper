#include<bits/stdc++.h>
using namespace std;

int main(){
int T;
cin>>T;
for(int n=1;n<=T;n++){
string s;
cin>>s;
int k;
cin>>k;
int N=s.length();
int c=0;
while(s.find('-')!=std::string::npos){
        size_t found=s.find('-');
        if(found+k < (unsigned)N){
           c++;
        for(int t=found;t<found+k && t<N;t++){
        if(s[t]=='-')
            s[t]='+';
        else
            s[t]='-';
                   }
           }
        else
            break;
    }
    if((count(s.begin(),s.end(),'-'))%k==0){
       c=c+((count(s.begin(),s.end(),'-'))/k);
       cout<<"Case #"<<n<<": "<<c<<"\n";
    }
    else
        cout<<"Case #"<<n<<": "<<"IMPOSSIBLE\n";
}
return 0;
}

