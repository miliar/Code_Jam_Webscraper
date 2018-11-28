//
// Created by Kapil Dolas on 08-04-2017.
//
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<vector>
#include<map>
#include<string>
#include<string.h>
#include<algorithm>
#include<set>
#define PI acos(-1.0)
#define SZ 1007
#define Fi(a,n) for(int i=a;i<n;i++)
#define Fj(a,n) for(int j=a;j<n;j++)
#define Fk(a,n) for(int k=a;k<n;k++)
#define ri(a) scanf("%d",&a)
#define pb push_back
#define mp make_pair
using namespace std;
typedef vector<int> vi;
typedef vector<vi > vii;
typedef long long ll;
typedef vector<ll> vll;

int main() {
    int t;
    long long n;
    char num[20];
    ri(t);
    for(int c=1; c<=t; c++) {
        scanf("%s", &num);
        int len = strlen(num);
        Fi(0, len-1) {
            if(num[i]>num[i+1]) {
                int j=i;
                while(j>0 && num[j]==num[j-1]) {
                    j--;
                }
                num[j] = (char)(num[j]-1);
                Fk(j+1, len) num[k] = '9';
            }
        }
        printf("Case #%d: %s\n", c, (num[0]=='0' && len>1)?num+1:num);
    }
    return 0;
}