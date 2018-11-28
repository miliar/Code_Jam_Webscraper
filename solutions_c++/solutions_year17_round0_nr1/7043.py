#include <bits/stdc++.h>
#define MAX 1100

using namespace std;

int main()
{
    //freopen("input.txt","r", stdin);
    //freopen("output.txt","w", stdout);
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		string s;
		cin>>s;
		int k;
		cin>>k;
		int flip[MAX];
		for(int i=0;i<MAX;i++)
            flip[i]=0;
        int ans=0;
		for(int i = 1; i<=s.length(); i++){
            char cur;
            cur=s[i-1];
            flip[i]+=flip[i-1];
            if(flip[i]%2){
                if(cur=='+')
                    cur='-';
                else
                    cur='+';
            }
            if(cur=='-'){
                if(i+k>s.length()+1){
                    ans=-1;
                    //cout<<endl<<"break "<<i<<endl;
                    break;
                }
                ans++;
                flip[i]++;
                flip[i+k]--;
            }
        }
       // for(int i=0;i<=s.length();i++)
       //     cout<<flip[i]<<' ';
       // cout<<endl;
        if(ans==-1)
            cout<<"Case #"<<cas<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<cas<<':'<<' '<<ans<<endl;
	}
    return 0;
}
