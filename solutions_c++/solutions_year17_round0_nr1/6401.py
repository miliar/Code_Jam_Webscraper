#include <bits/stdc++.h>
#define ll long long int
#define sc scanf
#define pf printf
using namespace std;
string s;
int checker(int x){
    for(;x<s.size();x++){
        if(s[x]=='-')return x;
    }
    return -1;
}
void runner(int x,int y){
    //int u=0;
    for(int j=0;j<y;j++){
        if(s[x+j]=='-')s[x+j]='+';
        else s[x+j]='-';
    }
}
int main(){
    freopen("C:\\Users\\mukhter\\Desktop\\graph\\A-large.in","r",stdin);
    freopen("C:\\Users\\mukhter\\Desktop\\graph\\outputFileName2.txt","w",stdout);
    int t;
    sc("%d",&t);
    getline(cin,s);
    for(int i=1;i<=t;i++){
        int counter=0;
        getline(cin,s);
      // cout<<s<<endl;
        stringstream ss;
        ss<<s;
        int p;
        ss>>s;
        ss>>p;
        int x=0;
        for(;x<s.size();){
            //cout<<x<<endl;
            //cout<<s<<endl;
            x=checker(x);
            if(x==-1)break;
            else if(x+p<=s.size())
            runner(x,p);
            else break;
            counter++;
        }
        if(x!=-1){
        /*    int pluss,minuss=0;
            for(;x<s.size();x++){
                if(s[x]=='+')pluss=1;
                else minuss=1;
            }
            if(pluss==1 && minuss==0){
                cout<<s<<" 1"<<endl;
                pf("Case #%d: %d\n",i,counter);

            }else{*/
                //cout<<s<<" 2"<<endl;
                pf("Case #%d: IMPOSSIBLE\n",i);
           // }
        }else{
            //cout<<s<<" 3"<<endl;
            pf("Case #%d: %d\n",i,counter);
        }
        //cout<<endl;
    }

}
