#include <bits/stdc++.h>

using namespace std;

int a[20], len;

void dec(int i);

void print_ans() {
    int i;
    for(i=19; i>=0; i--)
        if(a[i]!=0)
            break;

    for(; i>=0; i--)
        cout<<a[i];
    cout<<endl;
}

void check(int i) {
    if(a[i+1]==0 || a[i]>=a[i+1])
        return;
    a[i] = 9;
    dec(i+1);
}

void dec(int i) {
    a[i]--;
    check(i);
}

void fun() {
    for(int i=len; i>0; i--) {
        if(a[i]>a[i-1]) {
            dec(i);
            for(int j=i-1; j>=0; j--)
                a[j] = 9;
        }
    }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin>>t;

    for(int test=1; test<=t; test++) {
        long long int num;
        cin>>num;
        int l=0;
        while(num!=0) {
            a[l] = num%10;
            num = num/10;
            l++;
        }
        len = l-1;
        for(int i=l; i<20; i++)
            a[i] = 0;

        fun();

        cout<<"Case #"<<test<<": ";
        print_ans();
    }

    return 0;
}
