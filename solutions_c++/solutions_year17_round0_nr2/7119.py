#include <bits/stdc++.h>
#define MAX 1e15
#define pb push_back
#define mk make_pair
#define f first
#define s second
#define pii pair<int,int>
using namespace std;
typedef long long int ll;
const ll mod=1000000009;
ll arr[100005];
int main(){
    freopen("g.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll tst;
    ll k=0;
    cin>>tst;
    while(tst--){
    k++;
    string str;
    cin>>str;
    cout<<"Case #"<<k<<": ";
    if(str.length()==1)cout<<str<<endl;
    else{
        int len=str.length();
        int i=len-1;
        bool flag=0;
        while(str[i]=='0'){
            str[i]='9';
            i--;
            flag=1;
        }
        if(flag)str[i]--;
        //i--;
        //cout<<str<<endl;
        while(i-1>=0){
               flag=0;
               if(str[i]-'0'>=str[i-1]-'0'){
                 // i--;
                  //continue;
               }
               else{
                  str[i]='9';
                  str[i-1]=str[i-1]--;
                  flag=1;

               }
               /*if(i==1&&flag==1){
                  for(int k=0;k<len-1;k++)
                    cout<<"9";
                  return 0;
               }*/
               i--;
              // cout<<str<<endl;
        }
        flag=0;
        if(str[0]=='0'){
            for(int i=1;i<len;i++){
                if(!flag){
                  if(str[i]=='9')flag=1;
                  cout<<str[i];
                }
                else
                    cout<<"9";

            }
            cout<<endl;
         //   return 0;
        }
        else{
           for(int i=0;i<len;i++){
                if(!flag){
                  if(str[i]=='9')flag=1;
                  cout<<str[i];
                }
                else
                    cout<<"9";

            }
            cout<<endl;
        }

    }

    }
   return 0;
}
