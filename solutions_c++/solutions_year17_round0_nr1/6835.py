#include <bits/stdc++.h>
#define f(i,a,b) for(int i=(a);i<=(b);i++)
using namespace std;
int t,k,x,y,ok1,ok2;
string s,f;
bool all(char c){
    f(i,0,s.length()-1){
        if(s[i]!=c)return false;
    }
    return true;
}
void setf(){
    f(i,0,s.length()-1)f[i]='+';
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    f(tt,1,t){
        cin>>s>>k;
        /*if(all('+')){
            cout<<"Case #"<<tt<<": "<<0<<endl;
            continue;
        }
        if(all('-')){
            x=s.length()/k;
            cout<<"Case #"<<tt<<": "<<x<<endl;
            continue;
        }*/
        f=s,x=0;
        setf();
        //cout<<s<<" "<<f<<endl;
        f(i,0,s.length()-k){
            if(f[i]!=s[i]){
                f(j,0,k-1){
                    if(f[i+j]=='+')f[i+j]='-';
                    else f[i+j]='+';
                }
                x++;
            }
            //cout<<f<<endl;
        }
        ok1=(f==s);
        setf();
        y=0;
        for(int i=s.length()-1;i>=k-1;i--){
            if(f[i]!=s[i]){
                f(j,0,k-1){
                    if(f[i-j]=='+')f[i-j]='-';
                    else f[i-j]='+';
                }
                y++;
            }
        }
        ok2=(f==s);
        if(ok1==false && ok2==false) {
            //cout<<"case 1 ";
            cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        if(ok1==true && ok2==false){
            //cout<<"case 2 ";
            cout<<"Case #"<<tt<<": "<<x<<endl;
            continue;
        }
        if(ok2==true && ok1==false){
            //cout<<"case 3 ";
            cout<<"Case #"<<tt<<": "<<y<<endl;
            continue;
        }
        //cout<<"case 4 ";
        cout<<"Case #"<<tt<<": "<<min(x,y)<<endl;
    }
}
