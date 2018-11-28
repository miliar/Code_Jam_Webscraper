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
    freopen("ss.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll tst;
    ll kkk=0,k;
    cin>>tst;
    while(tst--){
        kkk++;
        string str;
        cin>>str;
        cin>>k;
        int len=str.length();
        bool flag=0;
        int ans=0;
        int i=0;
        cout<<"Case #"<<kkk<<": ";
        while(i<len&&!flag){
            if(str[i]=='+')
                    i++;
            else{
                if(len-i<k){
  //                      cout<<" i"<<i<<endl;
                        cout<<"IMPOSSIBLE"<<endl;
                        flag=1;
                }
                else{
                        int cnt=1;
                        ans++;
                        bool bb=0;
                        int j;
                        str[i]='+';
                        for(j=i+1;cnt<k;j++){
                            cnt++;
                            if(str[j]=='+'){
                                str[j]='-';
                                if(!bb)i=j;
    //                                cout<<" i "<<i<<endl;
                                bb=1;
                            //    break;
                            }
                            else
                             str[j]='+';

                        }
                        //cout<<str<<endl;
                        if(!bb)i=j;


                }  //inner else ki
            } //bahar else ki
            //cout<<i<<endl;
        }  //while ki
       if(!flag)
       cout<<ans<<endl;
    } //main ki
   return 0;
}
