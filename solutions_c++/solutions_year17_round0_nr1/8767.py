#include <iostream>
#include<bits/stdc++.h>
using namespace std;
typedef vector <int> vi;
typedef vector <long long> vill;

#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%I64d",&a)
#define pf(a) printf("%d\n",a)
#define pfll(a) printf("%I64d\n",a)
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define pb(a) push_back(a)
#define fore(i,a,b) for(i=a;i<b;i++)
#define PI 3.14159265



int main(){
    freopen("Pancake.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,k=0;
    cin>>t;
    while(t--){
        k++;
        int counter=0,flag=0,l;
        string s;
        cin >> s >>l;
        for(int i=0;i<=s.length()-l;i++){
            if(s[i]=='-'){
                counter++;
                for(int j=0;j<l;j++){
                    if(s[i+j]=='+'){
                       s[i+j] = '-';
                    }else{
                        s[i+j] = '+';
                    }
                }
            }
            //cout<<s<<i<<"\n";
        }
        for(int i=s.length()-l;i<s.length();i++){
            if(s[i]=='-'){
                flag=1;
            }
        }
        if (flag==0)
            cout<<"Case #"<<k<<": "<<counter<<"\n";
        else
            cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<"\n";
    }
    return 0;
}
