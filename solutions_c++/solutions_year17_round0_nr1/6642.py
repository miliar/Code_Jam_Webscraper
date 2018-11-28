#include<bits/stdc++.h>
using namespace std;
string s;

int main(){
freopen("alar.in","r",stdin);
freopen("alarans.in","w",stdout);
int t,i,testcases,l,j,k;
bool f;
scanf("%d",&t);
for(testcases=1;testcases<=t;testcases++){
    int c=0;
    s.clear();
    cin>>s;
    cin>>k;
    l=s.length();
    for(i=0;i<l-k+1;i++){
            //cout<<i<<" ";
       if(s[i]=='-'){
           for(j=i;j<(i+k);j++){
            if(s[j]=='-')
                s[j]='+';
            else if(s[j]=='+')
                s[j]='-';
        }
        c++;
        }
        /* for(j=0;j<l;j++)
            cout<<s[j];
         cout<<endl;*/
    }
    f=0;
    for(i=0;i<l;i++)
        if(s[i]=='-'){
            f=1;
            break;
    }
    if(f)
        cout<<"Case #"<<testcases<<": IMPOSSIBLE\n";
    else
        cout<<"Case #"<<testcases<<": "<<c<<"\n";
}
return 0;
}
