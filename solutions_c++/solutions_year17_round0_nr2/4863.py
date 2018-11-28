#include<bits/stdc++.h>
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define N 200000
#define inf 2000000000
#define F first
#define S second
#define mod 1000000007
#define ll long long int
#define CLEAR(a) memset(a,0,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define fr freopen("input.in", "r", stdin);
#define fw freopen("output.txt", "w", stdout);
using namespace std;

//bool cmp(const pair<int,pii>& lhs, const pair<int,pii>& rhs)
//    return lhs.first < rhs.first;

main(){
    fr;fw;
    int t,i,j,cnt=1;
    string s;
    ios::sync_with_stdio(0);
    cin>>t;
    while(t--){
        cin>>s;
        for(i=s.length()-1;i>0;i--){
            if(s[i-1]>s[i]){
                s[i-1] = s[i-1]-1;
                for(j=i;j<s.length();j++)
                    s[j]='9';
            }
        }
        if(s[0]=='0')
            i=1;
        else
            i=0;
        cout<<"Case #"<<cnt<<": "<<s.substr(i,s.length()-i)<<"\n";
        cnt++;
    }

    return 0;
}

