#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define llu long long unsigned
#define lld long long
#define ld long
int main() {
	// your code goes here
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	lld test,n,i,j,k;
    cin>>test;
   // cout<<test<<endl;
    string str;
    for(lld t=1;t<=test;t++){
        cin>>str>>k;
        lld count=0;
        for(i=0;i<=str.length()-k;i++){
            if(str[i]=='-'){
                count++;
                for(j=i;j<i+k;j++){
                    str[j]=(str[j]=='+')?'-':'+';
                }
            }
        }
        j=0;
        for(i=0;i<str.length();i++){
            if(str[i]=='-'){
                j=1;
                break;
            }
        }
        if(j==1){
            cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #"<<t<<": "<<count<<endl;
        }
    }


	return 0;
}
