#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long
#define F first
#define S second
#define pp pair<int,int>
using namespace std;
string s;
int k,answer;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin>>T;
    for(int t=1;t<=T;t++){

        cin>>s>>k;
        answer=0;

        for(int i=0;i+k-1<s.size();i++)
            if(s[i]!='+'){
                answer++;
                for(int j=i;j<=i+k-1;j++)
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
            }

        for(int i=0;i<s.size();i++)
            if(s[i]=='-'){
                    answer=-1;
                    break;
            }


        cout<<"Case #"<<t<<": ";
        if(answer==-1)
            cout<<"IMPOSSIBLE";
        else
            cout<<answer;
        cout<<endl;
    }

    return 0;
}
