#include <bits/stdc++.h>
#define M 1009
using namespace std;



int a[M];

bool is (int n){
    stringstream ss;
    ss << n;
    string s;
    ss >> s;
    string tmp = s;
    sort(tmp.begin(),tmp.end());
    return s==tmp;
}




int main (){
//
//    freopen("i.txt","r",stdin);
//    freopen("o.txt","w",stdout);

    int mx = -1;

    for(int i=1; i<=1000; i++){
        if(is(i)){
            mx = i;
        }
        a[i] = mx;
    }

    int tests;

    scanf("%d", &tests);

    for(int t=1; t<=tests; ++t){
        int b;
        scanf("%d",&b);
        ///Case #1:
        printf("Case #%d: %d\n",t,a[b]);
    }

}
