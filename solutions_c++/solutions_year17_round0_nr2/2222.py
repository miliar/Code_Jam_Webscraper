#include <bits/stdc++.h>
#define mx 100011
#define mp make_pair
#define pb push_back
#define ppb pop_back
#define mod 1000000009
#define ff first
#define ss second
#define ll long long
#define PII pair<int,int>
#define inf 1000000000000000
#define RIGHT 131072
#define SIZE 262144
using namespace std;
string solve(string s){
    if(s.length()==1)return s;
    string ans = "";
    if(s[0]=='1'){
        for(int i=0;i<s.length()-1;i++){
            if(s[i+1]<s[i]){
                if(s[i]=='1'){
                    for(int j=0;j<s.length()-1;j++)ans+='9';
                    return ans;
                }
                else{
                    for(int j=0;j<i;j++){
                        ans += s[j];
                    }
                    char c = s[i]-1;
                    ans += c;
                    for(int j=i;j<s.length()-1;j++)ans+='9';
                    int flag=s.length();
                    for(int j=ans.length()-2;j>=0;j--){
                        if(ans[j]>ans[j+1]){
                            ans[j]--;
                            flag=j;
                        }
                    }
                    for(int i=flag+1;i<ans.length();i++){
                        ans[i]='9';
                    }
                    return ans;
                }
            }
        }
        return s;
    }
    else{
        for(int i=0;i<s.length()-1;i++){
            if(s[i+1]<s[i]){
                for(int j=0;j<i;j++){
                    ans += s[j];
                }
                char c = s[i]-1;
                ans += c;
                for(int j=i;j<s.length()-1;j++)ans+='9';
                int flag=s.length();
                for(int j=ans.length()-2;j>=0;j--){
                    if(ans[j]>ans[j+1]){
                        ans[j]--;
                        flag=j;
                    }
                }
                for(int i=flag+1;i<ans.length();i++){
                        ans[i]='9';
                    }
                return ans;
            }
        }
        return s;
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int caseno=0;
    while(t--){
        string s;
        cin>>s;
        string str = solve(s);

        cout<<"Case #"<<++caseno<<": ";
        cout<<str<<endl;
    }
    return 0;
}
