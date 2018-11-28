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

vector<int> v;
int main(){
   freopen("AA.in", "r", stdin);
   freopen("out.txt", "w", stdout);
   int tst;
   cin>>tst;
   int j=1;
   while(tst--){
        cout<<"Case #"<<j<<":"<<endl;
        j++;
    int r,c;
    cin>>r>>c;
    string str[30];
    int f=-1;
    for(int i=0;i<r;i++){
        cin>>str[i];
        int len=str[i].length();
        int j=0;
        while(str[i][j]=='?'&&j<=len-1){
            j++;

        }
        if(j==len){
            v.pb(i);
        }
        else{
            if(f==-1)f=i;
            int k=j;
            int ss;
            while(j>=0){       //filling first;
                str[i][j]=str[i][k];

                j--;
            }
            int cntr=k;
            while(cntr<len){
                if(str[i][cntr]!='?'){
                    ss=cntr;
                    cntr++;
                }
                else{

                    while(str[i][cntr]=='?'&&cntr<len){
                        str[i][cntr]=str[i][ss];
                        cntr++;
                    }
                }
            }
        }
    }
    for(int i=0;i<v.size();i++){
        if(f!=-1&&v[i]<=f){
            str[v[i]]=str[f];
        }
        else
            str[v[i]]=str[v[i]-1];
    }
    v.clear();
    for(int i=0;i<r;i++){
            cout<<str[i];
                cout<<endl;
    }

   }

   return 0;
}
