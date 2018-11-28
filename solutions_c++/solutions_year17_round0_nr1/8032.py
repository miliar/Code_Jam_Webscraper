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
bool flip(int i){
    if(i+k>str.size())return false;
    for(int j=i;j<i+k;j++) if(str[j]=='+') str[j]='-';
    else str[j]='+';
    return true;
}
int main (){
    freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    int tc=II;
    int tc1=tc;
loop: while (tc--){
    cin>>str>>k;
        int count=0;
        fo(i,str.size()){
            if(str[i]=='-'){
                if(!flip(i)) {
                    printf("Case #%d: IMPOSSIBLE\n",tc1-tc);
                    goto loop;
                }
            count++;
            }
        }
    printf("Case #%d: %d\n",tc1-tc,count);
    }
}
