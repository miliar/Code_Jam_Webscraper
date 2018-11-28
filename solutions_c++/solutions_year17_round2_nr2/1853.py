/// i am on fire
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <string.h>

using namespace std;

const int N=200005;
const int M=1005;

typedef long long ll;
typedef pair<ll,ll>ii;
typedef pair<int,ii>node;

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }

vector<int>pushAt(int idx,int val,vector<int> x){
 vector<int >ret;
 for(int i=0;i<idx;i++)
    ret.push_back(x[i]);
 ret.push_back(val);
 for(int i=idx;i<x.size();i++)
    ret.push_back(x[i]);
 return ret;
}
int main(){

      freopen("test.in","r",stdin);
      freopen("A.out","w",stdout);;
    int t,c=1;
    scanf("%d",&t);
    while(t--){
     int n,arr[7],sum=0,tmp[7];
     scanf("%d",&n);
     for(int i=0;i<6;i++){
        scanf("%d",&arr[i]);
        tmp[i]=arr[i];
        sum+=arr[i];
     }
        sort(arr,arr+6);
        reverse(arr,arr+6);
        string s="";
        if(arr[0]==tmp[0])s+="R",tmp[0]=-1;
        else if(arr[0]==tmp[2])s+="Y",tmp[2]=-1;
        else if(arr[0]==tmp[4])s+="B",tmp[4]=-1;
        if(arr[1]==tmp[0])s+="R",tmp[0]=-1;
        else if(arr[1]==tmp[2])s+="Y",tmp[2]=-1;
        else if(arr[1]==tmp[4])s+="B",tmp[4]=-1;
        if(arr[2]==tmp[0])s+="R",tmp[0]=-1;
        else if(arr[2]==tmp[2])s+="Y",tmp[2]=-1;
        else if(arr[2]==tmp[4])s+="B",tmp[4]=-1;
        vector<int>v;
        for(int i=0;i<sum&&arr[0]>0&&(arr[1]>0||arr[2]>0);i++){
            if(i%2){
                if(arr[1]){
                    v.push_back(1);
                    arr[1]--;
                }
                else{
                    arr[2]--;
                    v.push_back(2);
                }
            }
            else{
                arr[0]--;
                v.push_back(0);
            }
        }
        int order=0;
        while(arr[1]>0&&arr[2]>0){
            if(!order){
                arr[1]--;
                v.push_back(1);
            }
            else{
                arr[2]--;
                v.push_back(2);
            }
            order=1-order;
        }
        if(arr[1]){
            v.push_back(1);
        }
        else{
            if(v.size()>0&&v[v.size()-1]==0){
                if(arr[2]){
                    arr[2]--;
                    v.push_back(2);
                }
            }
        }
        int i=0;
        while(arr[2]>0){
            if(v[i]!=2&&v[(i+1)%v.size()]!=2){
                v=pushAt((i+1)%v.size(),2,v);
                arr[2]--;
            }
            i++;
        }
        bool damn=0;
        if(v.size()<sum)
            damn=1;
        for(int i=0;i<v.size();i++){
            if(v[i]==v[(i+1)%v.size()]){
                damn=1;
                break;
            }
        }
        if(!damn){
           cout<<"Case #"<<c<<": ";
          for(int i=0;i<v.size();i++)
            cout<<s[v[i]];
        cout<<endl;
        }
        else{
                cout<<"Case #"<<c<<": IMPOSSIBLE\n";
        }
        c++;
    }
    return 0;
}
