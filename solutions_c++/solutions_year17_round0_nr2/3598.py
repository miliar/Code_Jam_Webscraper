#include<bits/stdc++.h>

using namespace std;

int main(){
    long long n;
    int i,j,t,T;
    string s;
    cin>>T;
    for(t=1;t<=T;t++){
        cin>>s;

        for(i=0;i<s.size()-1;i++){
            if(s[i]>s[i+1])break;
        }
        if(i >= s.size()-1){
            printf("Case #%d: %s\n",t,s.c_str());
            continue;
        }
        //cout<<"hh "<<i<<endl;
        while(i>=0 && s[i]>s[i+1]){
            s[i]--,i--;
        }
        i++;
        //cout<<"hb "<<i<<endl;
        n=0;
        for(j=0;j<=i;j++){
            n = 10 * n + s[j] - '0';
        }
        for(;j<s.size();j++){
            n = 10 * n + 9;
        }
        printf("Case #%d: %lld\n",t,n);
    }
    return 0;
}

