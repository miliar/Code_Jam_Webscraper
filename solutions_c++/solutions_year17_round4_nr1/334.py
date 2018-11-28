#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,b,a) for (int i=(b);i>=(a);i--)

typedef pair<int, int> ii;
typedef long long ll;

int match[100100];
bool flag[100100];
vector<int> grafo[100100];
int n;

void solvre2(int p, int n){
    int x;
    int ans = 0;
    int cont = 0;
    rep(i, 0, n){
        cin>>x;
        if(x & 1) cont++;
        else ans++;
    }
    ans = ans + (cont+1)/2;
    cout<<ans<<endl;
}

void solvre3(int p, int n){
    int x;
    int ans = 0;
    int a = 0, b = 0;
    rep(i, 0, n){
        cin>>x;
        if(x%3==0){
            ans++;
        }else if(x%3==1){
            a++;
        }else{
            b++;
        }
    }
    if(a<b) swap(a, b);
    a-=b;
    ans = ans + b + ((a+2)/3);
    cout<<ans<<endl;
}

void solvre4(int p, int n){
    int x;
    int ans = 0;
    int a = 0, b = 0, c = 0;
    rep(i, 0, n){
        cin>>x;
        if(x%4==0){
            ans++;
        }else if(x%4==1){
            a++;
        }else if(x%4==2){
            b++;
        }else{
            c++;
        }
    }
    if(a<c) swap(a, c);
    a-=c;
    x = 0;
    if(b%2==1 && a%4!=0){
        x = 1;
    }
    ans = ans + c + (a+3)/4 + (b+1)/2 - x;
    cout<<ans<<endl;
}


void solvre(){
    int p, n, x;
    int ans = 0;
    int cont = 0;
    cin>>n>>p;
    if(p==2) solvre2(p, n);
    else if(p==3) solvre3(p, n);
    else solvre4(p, n);
}

int main(){
    int t;
    cin>>t;
    REP(i, 1, t){
        printf("Case #%d: ", i);
        solvre();
    }
}