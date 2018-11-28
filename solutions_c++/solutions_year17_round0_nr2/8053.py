#include <stdio.h>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
#define II ({int a; scanf("%d",&a); a;})
#define fo(x,y) for (int x=0;x<y;x++)
#define p(n) printf("%d\n",n)
bool arr[10]={0};
int k;
string str;
void flip(int i){
    for(int k=i;k<str.size();k++)
        str[k]='9';
}
int main (){
    freopen("B-large.in.txt","r",stdin);
    freopen("B-large.out.txt","w",stdout);
    int tc=II;
    int tc1=tc;
    while (tc--){
        cin>>str;
        for(int i=(int)str.size()-1;i>0;i--){
            if(str[i]<str[i-1])
                str[i-1]--,flip(i);
        }
        if(str[0]=='0')str.erase(0,1);
        printf("Case #%d: %s\n",tc1-tc,str.c_str());
    }
}
