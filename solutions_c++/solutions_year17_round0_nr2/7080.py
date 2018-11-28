#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

bool check_if_asc(char* s, int l){
    int i = 0;
    while(i < l-1){
        if(s[i] > s[i+1])
            return false;
        i++;
    }
    return true;
}

int main()
{
    int t,g,l;
    scanf("%d", &t);
    long long int n, m, ans;
    g = t;
    while(t--){
        scanf("%lld", &n);
        m =  n;
        l=0;
        char* s = new char[30];
        while(m>0){
        	s[l++] = ('0' + m%10);
        	m = m/10;
        }
        reverse(s,s+l);
        bool x = check_if_asc(s,l);
        if(x){
            printf("Case #%d: %lld\n",(g-t),n);
            continue;
        }
        int idx = 0;
        int i = 0;
        while(i < l - 1){
            if(s[i] < s[i+1])
                idx = i+1;
            else if(s[i] > s[i+1])
                break;
            i++;
        }
        ans = 0;
        i = 0;
        while(i < l){
            if(i != idx){
                ans = ans*10 + (s[i] - '0');
                i++;
            }
            else{
                ans = ans*10 + (s[i] - '0' - 1);
                for(int j = i+1; j <l; j++){
                    ans = ans*10 + 9;
                }
                break;
            }
        }
        printf("Case #%d: %lld\n",(g-t),ans);
    }
}
