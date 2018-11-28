#include <bits/stdc++.h>
using namespace std;
#define ll long long

int a[1005];
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out2017.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int K=1; K<=t; K++){
        string s;
        cin>>s;

        if(s.size()>1){
            for(int i=s.size()-2; i>=0; i--){
                if(s[i]>s[i+1]){
                    s[i+1]='9';
                    s[i]=s[i]-1;
                    for(int j=i+2; j<s.size(); j++)
                        s[j]='9';
                }
                else if(s[i]=='0' && s[i+1]=='0'){
                    s[i]=s[i+1]='9';
                    for(int j=i+2; j<s.size(); j++)
                        s[j]='9';
                    if(s[i-1]>'0')
                        s[i-1]--;
                }
            }
        }

        printf("Case #%d: ", K);
        //cout<<s<<"\n";
        int k=0;
        while(s[k]=='0') k++;
        for(; k<s.size(); k++)
            cout<<s[k];
        cout<<"\n";
    }
    return 0;
}
