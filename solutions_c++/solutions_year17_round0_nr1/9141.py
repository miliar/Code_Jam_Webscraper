#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <stack>
#include <cmath>

#define llt long long int
#define pi 3.14159265358979323846
#define mod 1000000007
#define tsolve int t; cin>>t; while(t--)

#define ind(x) scanf("%d" , &x)
#define inlld(x) scanf("%lld" , &x)
#define outd(x) printf("%d\n" , x)
#define outlld(x) printf("%lld\n" , x)

#define newl printf('\n')
#define spce printf(' ')

using namespace std;

int check(string s,int n,int l,int j1){
    int i=0,j,temp1=0;
    int count1=0;
    while(i<n){
        for(i=0;i<n;i++) {
        if(s[i]=='-') {
                if(i>=(n-l+1)) {
                    cout<<"Case #"<<j1<<": "<<"IMPOSSIBLE"<<endl;
                    temp1=1;
                    break;
                }
            j=i;
            while(j<i+l) {
                if(s[j]=='+') {
                    s[j]='-';
                }
                else {
                    s[j]='+';
                }
                j++;
            }
            count1++;
        }
    }
    if(temp1==1) {
        break;
    }
    }
    if(temp1!=1) {
    cout<<"Case #"<<j1<<": "<<count1<<endl;
    }
    return 0;
}
int main() {
    freopen("in.in" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    string s;
    int t;
    cin>>t;
    int j=1;
    for(;j<=t;) {
        int l;
        cin>>s;
        cin>>l;
        int n=s.length();
        int temp=check(s,n,l,j);
        j++;
    }
    return 0;
}
