#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
string s;
void work() {
    bool flag=0;
    int l=s.length();
    for(int i=0;i<l-1;i++) {
        if(s[i]>s[i+1]) {
            flag = 1;
            s[i]--;
            for(int j=i+1;j<l;j++)s[j]='9';
            break ;
        }
    }
    if (flag)work();
}
int main() {
    int n;
    // freopen("B-large.in","r",stdin);
    // freopen("B-large.out","w",stdout);
    cin>>n;
    for(int i=1;i<=n;i++) {
        printf("Case #%d: ",i);
        cin>>s;
        work();
        int l = s.length();
        long long int sum = 0;
        for(int i=0;i<l;i++){
            sum*=10;
            sum+=s[i]-'0';
        }
        cout<<sum<<endl;
    }
}