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
	string str;
	cin>>test;
	for(k=1;k<=test;k++){
        cin>>str;
        //cout<<str<<" ";
        cout<<"Case #"<<k<<": ";
        string answer;
        if(str.length()==1){
            cout<<str<<endl;
            continue;
        }
        lld st=0,en=0;
        for(i=0;i<str.length();i++){
            if(str[i]>str[i+1]){
                break;
            }
            else if (str[i]==str[i+1]){
                en++;
            }
            else{
                en++;
                st++;
            }
        }
        //cout<<i<<endl;
        if(i==str.length()-1){
            cout<<str<<endl;
        }
        else{
            if(st==0 && str[0]=='1'){
                for(i=0;i<str.length()-1;i++){
                    cout<<'9';
                }
                cout<<endl;
            }
            else{
                for(i=st;i<str.length();i++){
                    if(i==st){
                        str[i]=str[i]-1;
                    }
                    else{
                        str[i]='9';
                    }
                }
                cout<<str<<endl;
            }
        }
	}
	return 0;
}
