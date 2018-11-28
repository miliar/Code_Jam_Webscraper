#include <iostream>
#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <time.h>
#include <vector>
#include <map>
#include <set>
#include <list>
#define pb push_back
#define ll long long
#define mp make_pair
#define pll pair<long,long>
#define plll pair<long,long>
#define F first
#define S second
#define INF 1000000000
#define MAXN 100500*4

using namespace std;

int main()
{
    #ifdef LOCAL
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    long n;
    cin>>n;
    for(int i=0;i<n;i++){
        string s;
        cin>>s;
        cout<<"Case #"<<i+1<<": ";
        bool flag=false,res=false;
        long long ans = 0;
        for(int j=1;j<s.length();j++){
            if(s[j-1]>s[j]){
                for(int k=j-1;k>=0;k--){
                    if(s[k]<s[j-1]){
                        for(int f=0;f<k+1;f++){
                            ans=(s[f]-'0')+ans*10;
                        }
                        ans = (s[j-1]-'0')-1+ans*10;
                        for(int f=0;f<s.length()-j+(j-1)-k-1;f++){
                            ans = ans*10+9;
                        }
                        flag=true;
                        break;
                    }
                }
                if(!flag){
                    ans = (s[0]-'0')-1;
                    for(int k=0;k<s.length()-1;k++){
                        ans = ans*10+9;
                    }
                }
                res=true;
                cout<<ans<<endl;
                break;
            }
        }
        if(!res){
            cout<<s<<endl;
        }
    }
    return 0;
}
