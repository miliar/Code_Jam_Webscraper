#include <bits/stdc++.h>
using namespace std;

vector<int> get(int n)
{
    vector<int> s;
    while(n!=0) {
        s.push_back(n%10);
        n/=10;
    }
    return s;
}

int check(vector<int> s)
{
//    cout<<">>>> ";
//    for(int i=s.size()-1; i>=0; i--) {
//        cout<<s[i];
//    }
//    cout<<endl;
    for(int i=0; i<s.size()-1; i++) {
        if(s[i]<s[i+1]) return 0;
    }
    return 1;
}

int func(int n)
{
    for( ; n>=10; n--) {
        vector<int> s=get(n);
        if(check(s)==1) {
            return n;
        }
    }
    return n;
}

int main ()
{
    freopen("output.txt", "w", stdout);
    int cs; cin>>cs;
    for(int t=1; t<=cs; t++) {
        int n;
        cin>>n;
        int ans=func(n);
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
