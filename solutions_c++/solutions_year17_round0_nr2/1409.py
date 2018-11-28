#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
using namespace std;
ifstream fin("in.in");
ofstream fo("out.out");
int test,n;
string s;
void upd(int i){
    s[i]--;
    for(int j=i-1;j>=0;j--){
        if(s[j]>s[j+1]){
            s[j]=s[j+1];
            for(int ij=j+1;ij<=i;ij++){
                s[ij]='9';
            }
        }
    }
}
int main(){
    ios_base::sync_with_stdio(0);
    fin>>test;
    for(int t=1;t<=test;t++){
        if(t>1) fo<<"\n";
        fo<<"Case #"<<t<<": ";
        fin>>s;
        n=(int) s.length();
        for(int i=1;i<n;i++){
            if(s[i]<s[i-1]){
                for(int j=i;j<n;j++){
                    s[j]='9';
                }
                upd(i-1);
                break;
            }
        }
        if(s[0]=='0'){
            for(int i=0;i<n-1;i++) fo<<"9";
        }
        else{
            fo<<s;
        }
    }
}
